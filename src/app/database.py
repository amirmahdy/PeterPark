from app import db
from sqlalchemy import text


def search_lev(model, search_text, lv_dist):
    data = model.query.filter(
        text(f"levenshtein(replace(plate, '-', ''), '{search_text}') <= {lv_dist}")).order_by(text("id")).all()
    return data


def get_all(model):
    data = model.query.all()
    return data


def insert_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()


def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()


def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()


def commit_changes():
    db.session.commit()

