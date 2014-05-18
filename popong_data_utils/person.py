# -*- coding: utf-8 -*-

from popong_models import Candidacy, Person

from .db import DbNotInitiatedError


__all__ = ['guess_person']


def guess_person(**kwargs):
    try:
        q = Person.query
    except AttributeError as e:
        raise DbNotInitiatedError()

    if 'name' in kwargs:
        q = q.filter_by(name=kwargs['name'])
    if 'name_kr' in kwargs:
        q = q.filter_by(name=kwargs['name_kr'])
    if 'name_cn' in kwargs:
        q = q.filter_by(name_cn=kwargs['name_cn'])
    if 'birthyear' in kwargs:
        q = q.filter_by(birthday_year=kwargs['birthyear'])
    if 'birthday_year' in kwargs:
        q = q.filter_by(birthday_year=kwargs['birthday_year'])
    if 'birthday' in kwargs:
        q = q.filter_by(birthday=kwargs['birthday'])
    if 'assembly_id' in kwargs:
        q = q.join(Person.candidacies)\
             .filter(Candidacy.assembly_id == kwargs['assembly_id'])
    return q.one()

