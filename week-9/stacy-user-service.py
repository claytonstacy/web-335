# ============================================
# Title: Assignment 9.2
# Author: Professor Krasso
# Date: 24 June 2020
# Modified By: Clayton Stacy
# Description: Querying and Creating Documents
# ============================================

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335
user = {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}
user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))