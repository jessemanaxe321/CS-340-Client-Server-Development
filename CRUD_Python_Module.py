# CRUD Python Module for the AAC Animal Shelter database

from pymongo import MongoClient


class AnimalShelter:
    """Provides Create and Read operations for the AAC animals collection."""

    def __init__(self, username, password):
        """Initialize the MongoDB connection using the supplied credentials."""

        self.client = MongoClient(
            host="localhost",
            port=27017,
            username=username,
            password=password,
            authSource="admin"
        )

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert one document into the animals collection."""

        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except Exception as error:
            print(f"Create error: {error}")
            return False

    def read(self, query):
        """Return documents matching the supplied MongoDB query as a list."""

        if not isinstance(query, dict):
            return []

        try:
            return list(self.collection.find(query))
        except Exception as error:
            print(f"Read error: {error}")
            return []