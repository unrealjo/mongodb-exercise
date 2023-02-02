from config.client import Client
db = Client().get_db("practice")

documenets  = db.restaurants.find({"borough":"Brooklyn"})
for doc in documenets :
    print(doc)

