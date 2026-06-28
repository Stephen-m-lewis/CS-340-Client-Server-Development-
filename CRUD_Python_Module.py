# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    
    def create(self, data):

        # Make sure data was provided
        if data is not None:
            try:
                # Insert the document into the animals collection
                self.collection.insert_one(data)

                # Return True if insert was successful
                return True

            except Exception as e:
                print("Error inserting document:", e)
                return False

        # Return False if no data was passed in
        return False


    # This method reads documents from the MongoDB collection
    def read(self, query):

        # Make sure a query was provided
        if query is not None:
            try:
                # Find all documents that match the query
                data = self.collection.find(query)

                # Convert cursor results to a list and return them
                return list(data)

            except Exception as e:
                print("Error reading documents:", e)
                return []

        # Return an empty list if no query was provided
        return []
    
    
    # This method updates documents in the MongoDB collection
        
    def update(self, query, new_values):

        # Make sure both arguments were provided
        if query is not None and new_values is not None:
            try:
                # Update all documents that match the query
                result = self.collection.update_many(query, {"$set": new_values})

                # Return the number of documents that were changed
                return result.modified_count

            except Exception as e:
                print("Error updating documents:", e)
                return 0

        # Return 0 if the query or new values were missing
        return 0


    # This method deletes documents from the MongoDB collection
    def delete(self, query):

        # Make sure a query was provided
        if query is not None:
            try:
                # Delete all documents that match the query
                result = self.collection.delete_many(query)

                # Return the number of documents deleted
                return result.deleted_count

            except Exception as e:
                print("Error deleting documents:", e)
                return 0

        # Return 0 if no query was provided
        return 0