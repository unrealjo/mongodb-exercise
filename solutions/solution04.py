from config.client import Client
db = Client().get_db("practice")

options = {
    "_id":0,
    "address.zipcode":1,
}

documents  = db.restaurants.find({},options)
for doc in documents :
    print(doc)

