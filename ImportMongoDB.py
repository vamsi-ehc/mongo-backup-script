from pymongo import MongoClient
import json
import os

def import_json_to_database(connection_string, db_name, input_dir):
    client = MongoClient(connection_string)
    db = client[db_name]

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".json"):
            collection_name = file_name.split(".")[0]
            with open(os.path.join(input_dir, file_name), "r") as json_file:
                documents = json.load(json_file)
                collection = db[collection_name]
                collection.insert_many(documents)

    client.close()

# Example usage:
connection_string = "mongo_connection_string/database_name"
import_json_to_database(connection_string, "database_name", "path_of_database_jsons")
