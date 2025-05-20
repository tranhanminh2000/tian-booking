import json
from shared.repositories.crud.base import BaseCRUDRepository

class RedisCacheCRUDRepository(BaseCRUDRepository):
    def __init__(self, repo: BaseCRUDRepository, redis_client: redis.Redis, cache_ttl=300):
        self.repo = repo
        self.redis = redis_client

    def _cache_key(self, id):
        return f"{self.repo.model.__name__}:{id}"

    def get(self, id):
        key = self._cache_key(id)
        cached = self.redis.get(key)
        if cached:
            print("Get from cache")
            data = json.loads(cached)
            return data

        obj = self.repo.get(id)
        if obj:
            self.redis.setex(key, self.cache_ttl, json.dumps(obj_data))
        return obj

    def get_all(self):
        return self.repo.get_all()

    def create(self, obj):
        created = self.repo.create(obj)
        return created

    def update(self, obj):
        updated = self.repo.update(obj)
        key = self._cache_key(obj.id)
        obj_data = obj.to_dict()
        self.redis.setex(key, self.cache_ttl, json.dumps(obj_data))
        return updated

    def delete(self, id):
        deleted = self.repo.delete(id)
        key = self._cache_key(id)
        self.redis.delete(key)
        return deleted
