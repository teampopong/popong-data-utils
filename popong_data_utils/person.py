# -*- coding: utf-8 -*-

from popong_models import Candidacy, Person

from .db import DbNotInitiatedError


__all__ = ['guess_person', 'guess_person_name']


def guess_person_name(string, **kwargs):
    try:
        q = Person.query
    except AttributeError as e:
        raise DbNotInitiatedError()

    for f in ('assembly_id', 'is_elected'):
        if f in kwargs:
            q = q.join(Person.candidacies)
    if 'assembly_id' in kwargs:
        q = q.filter(Candidacy.assembly_id == kwargs['assembly_id'])
    if 'is_elected' in kwargs:
        q = q.filter(Candidacy.is_elected == kwargs['is_elected'])

    candidacies = []
    for person in q:
        if person.name in string:
            candidacies.append(person.name)

    if not candidacies:
        raise GuessFail()

    candidacies = sorted(candidacies, key=lambda s: len(s), reverse=True)
    return candidacies.pop(0)


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

    # candidacy-related things
    for f in ('assembly_id', 'is_elected'):
        if f in kwargs:
            q = q.join(Person.candidacies)
    if 'assembly_id' in kwargs:
        q = q.filter(Candidacy.assembly_id == kwargs['assembly_id'])
    if 'is_elected' in kwargs:
        q = q.filter(Candidacy.is_elected == kwargs['is_elected'])
    return q.one()


class GuessFail(Exception):
    pass

