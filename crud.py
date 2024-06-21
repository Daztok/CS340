#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient


# In[1]:


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self):
        # Initialize the MongoClient and connect to the database
        self.client = MongoClient('mongodb://aacuser:qwer1234@nv-desktop-services.apporto.com:31959')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def create(self, data):
        """Insert a document into the collection"""
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print("An error occurred:", e)
            return False

    def read(self, query):
        """Query documents from the collection"""
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print("An error occurred:", e)
            return []

    def update(self, query, new_values):
        """Update document(s) in the collection"""
        try:
            result = self.collection.update_many(query, {'$set': new_values})
            return result.modified_count
        except Exception as e:
            print("An error occurred:", e)
            return 0

    def delete(self, query):
        """Delete document(s) from the collection"""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("An error occurred:", e)
            return 0

