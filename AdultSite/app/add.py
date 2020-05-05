import pymongo
client = pymongo.MongoClient()
db = client.Models

import datetime
for _ in range(10):
    
    post = {
        'content': 'templates/imgs/111.jpg',
        'premium': True,
        'date': datetime.datetime.utcnow()
    }

    db['Juli_Annee'].insert_one(post)

'''
model = db['Peta_Jensen']

for i in model.find():
    print(i['_id'])
'''