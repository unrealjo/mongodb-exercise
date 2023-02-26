from config.client import Client
db = Client().get_db("practice")

options = {
    "restaurant_id":1,
    "name":1,
    "borough":1,
    "cuisine":1
}

documents  = db.restaurants.find(
    { "name":{"$regex":"Food$" } },
    options
)

for doc in documents :
    print(doc)

