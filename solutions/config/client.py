import os
from pymongo import MongoClient
class Client:
    def __init__(self) -> None:
        self._url = os.environ.get("MONGODB_HOST")
        self._usrname = os.environ.get("MONGODB_USER")
        self._passowrd = os.environ.get("MONGODB_PASSWORD")
    def get_db(self,dbname):
        client = MongoClient( host="mongodb://localhost:27017/",
                            username="root", 
                            password="HQDQD28E62Y")
        return client.get_database(dbname) 

