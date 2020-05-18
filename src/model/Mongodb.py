import pymongo

from datetime import date


class MongoDBHandle:

    def __init__(self):

        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

        try:
            self.analytics_db = self.client['user']
            self.extract_coll = self.analytics_db['key']
        except pymongo.errors.ServerSelectionTimeoutError as e:
            print("Could not connect to server: %s" % e)
            self.client = None

    def save_new_user(self, user_id, user_key):
        result = self.extract_coll.insert_one({"date": str(date.today()),
                                               "user": user_id,
                                               "user_key": user_key})
        return result.inserted_id
