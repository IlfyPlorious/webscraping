from database import get_database
from database import write_many_to_collection
from database import delete_many_from_collection

database = 'user_products_database'

db = get_database('user_products_database')

db.createUser(
   {
     'user': "accountUser",
     'pwd': "PaSSw0rd",
     'roles': ["readWrite", "dbAdmin"]
   }
)

item = {
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance"
}


