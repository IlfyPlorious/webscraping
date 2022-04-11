def get_database(database):
    connection_string = "mongodb+srv://dev:PaSSw0rd@realmcluster.xvmm3.mongodb.net/ProductsDatabase?retry \
    Writes=true&w=majority"

    from pymongo import MongoClient
    client = MongoClient(connection_string)

    return client[database]


def get_products_in_collection(collection, database):
    collection_name = database[collection]

    item_details = collection_name.find()

    product_list = []

    for item in item_details:
        product_list.append(item)

    return product_list


def write_one_to_collection(item, collection, database):
    db_collection = database[collection]
    db_collection.insert_one(item)


def write_many_to_collection(item, collection, database):
    db_collection = database[collection]
    db_collection.insert_many(item)


def delete_one_from_collection(item_id, collection, database):
    db_collection = database[collection]
    db_collection.delete_one({'_id': item_id})


def delete_many_from_collection(items_id, collection, database):
    for item_id in items_id:
        delete_one_from_collection(item_id, collection, database)


if __name__ == "__main__":
    # used to create database by running database.py separately

    dbname = get_database('user_products_database')

    top_favorite_collection = dbname["top_favorite"]

    item_1 = {
        'produs': 'telefon',
        'categorie': 'top favorite',
        'link': 'link'
    }

    top_favorite_collection.insert_one(item_1)
