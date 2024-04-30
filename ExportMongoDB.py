from pymongo import MongoClient
import json
import os

def clone_database_to_json(connection_string, db_name, output_dir):
    client = MongoClient(connection_string)
    db = client[db_name]

    # Create a directory for the output if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        documents = collection.find()
        with open(f"{output_dir}/{collection_name}.json", "w") as json_file:
            json.dump(list(documents), json_file, default=str)

    client.close()

# Example usage:
connection_string = "mongo_connection_string/database_name"
clone_database_to_json(connection_string, "database_name", "output_directory")
