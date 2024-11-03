import pymongo

Mongo_Client = pymongo.MongoClient(host='coinbase_mongodb',
                        port=27017,
                        username='root',
                        password='example',
                        authSource="admin")
Mongo_Database = Mongo_Client["coinbase"]

ETH_Collection = Mongo_Database["ETH"]