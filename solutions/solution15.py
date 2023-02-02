from config.client import Client
db = Client().get_db("practice")

documenets  = db.restaurants.find(
    {
        "borough":"Bronx",
        "$or":[
        {"cuisine":"American"},
        {"cuisine":"Chinese"}
        ]
    }
)

for doc in documenets :
    print(doc)

