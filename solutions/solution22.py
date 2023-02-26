from config.client import Client
db = Client().get_db("practice")

documents = db.restaurants.find().sort([("cuisine", 1), ("borough", -1)])

for doc in documents:
    print(doc)
