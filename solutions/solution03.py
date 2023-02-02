from config.client import Client
db = Client().get_db("practice")

options = {
    "_id":0,
    "restaurant_id":1,
    "name":1,
    "borough":1,
    "cuisine":1
}

documenets  = db.restaurants.find({},options)
for doc in documenets :
    print(doc)

