from config.client import Client
db = Client().get_db("practice")

documenets  = db.restaurants.find(
    {"borough":"Brooklyn"}
).limit(5)

for doc in documenets :
    print(doc)

