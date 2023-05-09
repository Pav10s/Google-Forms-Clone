import pymongo
from django.utils import timezone
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['GoogleForms']
col = db['GoogleForms']

class Form:
    def create(self):
        obj = col.insert_one({
            'created': timezone.now()
        })
        return str(obj.inserted_id)
    
    def find(self,pk):
        query = {
            '-id':ObjectId(pk)
        }
        print(col.find(query))
        print(type(col.find(query)))
        return col.find(query).next()
