from shared.repositories.crud.base import BaseCRUDRepository


class MySQLRepository(BaseCRUDRepository):
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def get(self, id):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.db.query(self.model).all()

    def create(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, obj):
        self.db.merge(obj)
        self.db.commit()
        return obj

    def delete(self, id):
        obj = self.get(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
        return obj
