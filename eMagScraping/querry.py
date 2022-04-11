from database import get_database
from database import write_many_to_collection
from database import delete_many_from_collection

database = 'user_products_database'

dbname = get_database(database)

top_fav = dbname.top_favorite

item = {
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance"
}

products = top_fav.find()

delete_many_from_collection([products[0]['_id'], products[1]['_id']], 'top_favorite', dbname)


for product in products:
    print(product)
