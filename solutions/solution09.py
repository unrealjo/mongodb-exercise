from config.client import Client
db = Client().get_db("practice")

documenets  = db.restaurants.find(
    {"grades":
    {"$elemMatch":
    {"score":{"$gt":7,"$lt":10}}}}
)

for doc in documenets :
    print(doc)

