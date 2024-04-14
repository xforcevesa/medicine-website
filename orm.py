import sqlalchemy as sql
from sqlalchemy.orm import Session

import db

engine = sql.create_engine('sqlite:///medicine.db', echo=True)
db.Medicine.metadata.create_all(engine)


def add_medicine(medicine: dict):
    for key in medicine.keys():
        if key not in db.fields.keys():
            medicine.pop(key)
    medicine_object = db.Medicine(**medicine)
    with Session(engine) as session:
        session.add(medicine_object)
        session.commit()


def get_all_medicines():
    with Session(engine) as session:
        query = session.query(db.Medicine).all()
        return query
