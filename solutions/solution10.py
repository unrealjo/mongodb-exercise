from config.client import Client
db = Client().get_db("practice")

documents  = db.restaurants.find(
    {
    "cuisine":{"$ne":"American"},
    "grades.score":{"$gt":7}
    }
)

for doc in documents :
    print(doc)

