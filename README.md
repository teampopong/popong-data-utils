# POPONG Data Utils

Data utility for POPONG models

## Installation

    $ pip install git+https://github.com/teampopong/popong-data-utils.git

## Usage Example

    from popong_data_utils import connect_db, guess_person
    connect_db('postgresql+psycopg2://MY_ID:MY_PASSWORD@localhost/SOME_DB')
    person = guess_person(name=u'고승덕', assembly_id=18)

