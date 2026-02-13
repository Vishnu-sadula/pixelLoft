import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.userlist
collection = db['flask-users']

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_button():
    try:
        
        name = request.form.get('name')
        role = request.form.get('role')
        user_id = request.form.get('id')

        collection.insert_one({
            "id": user_id,
            "name": name,
            "role": role
        })
        
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        return redirect('/success')
    
    #show error
    except Exception as e:
        print(e)
        return render_template('index.html', error=str(e))

@app.route('/success')
def success():
    return "<h1>Data submitted successfully!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
