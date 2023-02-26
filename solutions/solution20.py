from config.client import Client
db = Client().get_db("practice")

documents = db.restaurants.find({},{}).sort([("name",1)])

for doc in documents:
    print(doc)
