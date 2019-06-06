import pymongo

def getTexts():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        return myclient["Sports"]["SportsNews"].find({}, {"_id": 0})












