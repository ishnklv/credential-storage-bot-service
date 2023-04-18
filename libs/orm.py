from pymongo.collection import Collection


class Orm:
    def __init__(self, collection: Collection):
        if collection is None:
            raise ValueError('Collection param not provided')
        else:
            self._collection = collection

    def create(self, data: dict):
        document = self._collection.insert_one(data)

        return document.inserted_id

    def create_many(self, items: list):
        documents = self._collection.insert_many(items)

        return documents.inserted_ids

    def update_by_id(self, _id, data):
        updated_instance = self._collection.update_one({'_id': _id}, data, upsert=True)

        return updated_instance.upserted_id

    def soft_delete_by_id(self, _id) -> None:
        self._collection.update_one({'_id': id}, {'is_deleted': True})

    def delete_by_id(self, _id) -> None:
        self._collection.delete_one({'_id': _id})

    def find_one(self, query: dict):
        instance = self._collection.find_one(query)

        return instance
