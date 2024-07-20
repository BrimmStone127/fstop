from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['mongodbVSCodePlaygroundDB']
collection = db['photos']

@app.route('/photos')
def get_photos():
    photos = collection.find()
    return jsonify(list(photos))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)