from config.client import Client
db = Client().get_db("practice")

documents  = db.restaurants.find(
    {
    "borough":{"$ne":"Brooklyn"},
    "cuisine":{"$ne":"American"},
    "grades.grade":"A"
    }
).sort("cuisine",-1)

for doc in documents :
    print(doc)

