from config.client import Client
db = Client().get_db("practice")

documents  = db.restaurants.find(
    {
        "borough":"Bronx",
        "$or":[
        {"cuisine":"American"},
        {"cuisine":"Chinese"}
        ]
    }
)

for doc in documents :
    print(doc)

