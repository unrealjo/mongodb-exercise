from config.client import Client
db = Client().get_db("practice")

options = {
    "restaurant_id":1,
    "name":1,
    "borough":1,
    "cuisine":1
}

documents  = db.restaurants.find(
    {"grades.score":{"$lt":10}},
    options
)

for doc in documents :
    print(doc)

