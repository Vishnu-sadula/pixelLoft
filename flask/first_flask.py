import json
from flask import Flask, render_template

app = Flask(__name__)
database_list = 'list.json'

def get_data():
    with open(database_list, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    
    return render_template('index.html', team_list=get_data())

@app.route('/api')
def get_api():
    
    return get_data()

if __name__ == '__main__':
    app.run(debug=True)

