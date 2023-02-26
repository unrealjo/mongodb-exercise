from config.client import Client
db = Client().get_db("practice")

options = {
    "restaurant_id":1,
    "name":1,
    "borough":1,
    "cuisine":1
}

documents  = db.restaurants.find(
    {"borough":
        {"$nin":["Staten Island","Queens","Bronx","Brooklyn"]}
    },
    options
)

for doc in documents :
    print(doc)

