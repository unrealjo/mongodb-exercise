from config.client import Client
db = Client().get_db("practice")

documenets  = db.restaurants.find()
for doc in documenets :
    print(doc)

