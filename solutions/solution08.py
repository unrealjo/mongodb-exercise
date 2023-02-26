from config.client import Client
db = Client().get_db("practice")

documents  = db.restaurants.find(
    {"grades.score":{"$gt":7}}
    #{"grades":{"$elemMatch":{"score":{"$gt":10}}}}
)

for doc in documents :
    print(doc)

