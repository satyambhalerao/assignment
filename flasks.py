from flask import Flask,request,jsonify
from databaseconnection import database

app = Flask(__name__)


@app.route('/search',methods=['GET','POST'])
def home():
    data = request.get_json()
    query = data.get('query','')
    result = database(query)
    result = {key: result[0][key] for key in result[0].keys()
       & {'Title', 'Category','SubCategory','Frequency','ParentExists','Child','Discontinued'}}
    return {query:result}







if __name__ == '__main__':
    app.run()
