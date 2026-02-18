import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.todo_db
collection = db['todo_items']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        item_id = request.form.get('itemId')
        item_uuid = request.form.get('itemUuid')        
    
        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description,
            "itemId": item_id,
            "itemUuid": item_uuid
        })
        
        print(f"Successfully inserted: {item_name}")
        return redirect('/') 
        
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', error="Failed to insert item")


if __name__ == '__main__':
    app.run(debug=True)

