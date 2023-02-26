from config.client import Client
db = Client().get_db("practice")

documents = db.restaurants.find({
    "address.building": {"$exists": True}
})

for doc in documents:
    print(doc)
