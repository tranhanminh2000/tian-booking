from shared.repositories.crud.base import BaseCRUDRepository


class MongoCRUDRepository(BaseCRUDRepository):
    """
    Base class for MongoDB CRUD repositories.
    """

    def __init__(self, collection):
        self.collection = collection

    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get(self, query):
        return self.collection.find(query)

    def get_all(self):
        return self.collection.find()

    def update(self, query, update_data):
        result = self.collection.update_one(query, {"$set": update_data})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count