from pymongo import MongoClient
from pprint import pprint
client = MongoClient()

if __name__ == '__main__':
    print("Modify me")
    # establishing connection 
    # to the database
    client = MongoClient("mongodb://localhost:27017/") 
    
    # Database name 
    db = client["mongo_db_lab"] 
    
    # Collection name 
    col = db["definitions"] 
  
    # if we don't want to print id then pass _id:0
    for document in col.find({}, {}): 
        pprint(document)
