from async_pymongo import AsyncClient


class DBHandler:
    @classmethod
    def set_db(cls, uri, db_name):
        cls.client = AsyncClient(uri)
        cls.database = cls.client[db_name]

    @classmethod
    def get_cli(cls):
        return cls.client if hasattr(cls, "client") else None

    @classmethod
    def get_db(cls):
        return cls.database if hasattr(cls, "database") else None
