# импортируем pymongo
import pymongo

# соединяемся с сервером базы данных 
# (по умолчанию подключение осуществляется на localhost:27017)
client = pymongo.MongoClient()

# выбираем базу данных
db = client.table11

# Создаём коллекцию
#collection = db.test_collection

# Создаём документ
import datetime
author = 'Mike'
post = {"author": author,
		"text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"],
		"date": datetime.datetime.utcnow()}

# Добавляем документ
posts = db.posts
post_id = posts.insert_one(post).inserted_id

# Берем документ из Mongo БД
print(posts.find_one())