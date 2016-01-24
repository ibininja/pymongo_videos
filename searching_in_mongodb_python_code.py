import pymongo

URI = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(URI)
DB= client['testdb']
video = DB.video

def search():
    word="video"
    query = {"length":25, "$text":{"$search":word}}

    result = video.find(query)
    print result.count()
    for r in result:
        print r

search()
