#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the important packages

import pymongo
import pprint
import json
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#Connecting with MongoClient

client = pymongo.MongoClient('mongodb://localhost:27017')


# In[28]:


#Creating a database

database = client['project_0']


# In[29]:


#Creating Collection

database.create_collection("Meal_Information")


# In[5]:


Meal_collection = database.get_collection("meal_info")


# In[30]:


#Load the meal_info Json file into my collection 

with open("meal_info.json") as f:
    file_data = json.load(f)


# In[31]:


#Insert single document using inset_one() method

single_doc={'meal_id':1010,'category':"frenchfries","cuisine":"Indian"}
Meal_collection.insert_one(single_doc)


# In[32]:


#Count the no of documents in the collection using count() method

Meal_collection.find().count()


# In[33]:


#Insert many documents using inset_many() method

Meal_collection.insert_many(file_data)


# In[34]:


#Count the no of documents in the collection using count() method

Meal_collection.find().count()


# In[35]:


#Finding the single document in the collection using find_one() method

Meal_collection.find_one()


# In[36]:


#Finding the all document in the collection using find() method and also using slice,limit,etc..

for meal_infor in Meal_collection.find():
    print(meal_infor)


# In[37]:


#Limit
#Get first 5 documents using Limit() method 

for meal in Meal_collection.find().limit(5):
    print(meal)


# In[38]:


#Update the single document using update_one() method

Meal_collection.update_one({"meal_id":"1885"},{"$set":{"meal_id":"1886"}})


# In[39]:


#Update the single document using update_many() method

Meal_collection.update_many({},{"$set":{"category":"PURE_VEG"}})


# In[40]:


for meal_infor in Meal_collection.find():
    print(meal_infor)


# In[44]:


#Delete the single documet using delete_one() method

Meal_collection.delete_one({"meal_id" : "1885"})


# In[47]:


#Delete the many documet using delete_many() method

Meal_collection.delete_many({ "cuisine": {"$regex": "^c"}})


# In[51]:


# Sort the meal_id in ascending order using sort method
for i in Meal_collection.find().sort("meal_id",1):
    print(i)


# In[ ]:




