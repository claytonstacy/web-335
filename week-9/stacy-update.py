# ============================================
# Title: Assignment 9.3
# Author: Professor Krasso
# Date: 24 June 2020
# Modified By: Clayton Stacy
# Description: Updating and Deleting Documents
# ============================================

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335
db.users.update_one(
    {"employee_id": "0000008"},
    {
        "$set": {
            "email": "cdstacy@my365.bellevue.edu"
        }
    }
)
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))