import pymongo
import excel_to_dictnory


def database(query):
    pipeline = [
    {
        '$search': {
            'index': 'default', 
            'text': {
                'query': query, 
                'path': 'Tags'
            }
        }
    }, {
        '$limit': 1
    }
]
    client = pymongo.MongoClient("mongodb+srv://satyambhalerao24:muOZSSYsXxbHebiK@cluster0.wxtvpz6.mongodb.net/?retryWrites=true&w=majority")
    if(client):
        print("Succes")
    else:
        print("failed")
    print(client.list_database_names())
    db = client["dataset"]
    collection = db["MetaDatasample"].aggregate(pipeline)
        # mydict = { "name": "John", "address": "Highway 37" }
        # collection.insert_one(mydict)
        # data = excel_to_dictnory.dataset()
        # for x in data:
        #     collection.insert_one(x)
    return (list(collection))

