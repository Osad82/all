import pymongo
client = pymongo.MongoClient()
db = client.Names

'''
namesdata = []
for _ in range(2):
	subdata = [input('Enter name: '), input('Enter password: ')]
	namesdata.append(subdata)
print(namesdata)


data = {}
for i, d in enumerate(namesdata):
	subdata = {}
	subdata['user{}'.format(i)] = {'name' : d[0], 'pass' : d[1],}
	data.update(subdata)


'''

names = db['names-collection']
new_name = { "$set": { 'Name' : 'Ivan2' }}
#names_id = names.insert_one(data).inserted_id
for i in names.find():
	names.update_one(i, new_name)
for i in names.find():
	names.delete_one(i)
