from config.client import Client
db = Client().get_db("practice")

documenets  = db.restaurants.find(
    {
    "borough":{"$ne":"Brooklyn"},
    "cuisine":{"$ne":"American"},
    "grades.grade":"A"
    }
).sort("cuisine",-1)

for doc in documenets :
    print(doc)

