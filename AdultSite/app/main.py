from flask import Flask, render_template
import pymongo

# Создаём обьект класса Flask
app = Flask(__name__)
# Подключаем MongoDB
db = pymongo.MongoClient().Models


# Что будет, если перейти по этому пути
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    model = db['Juli_Annee']
    posts = []
    for i in model.find():
        posts.append(i)
    return render_template('posts.html', posts=posts)


# Запуск
if __name__ == '__main__':
    app.run(debug=True)