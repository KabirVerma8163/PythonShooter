import pymongo
import urllib.parse as parse

password = parse.quote("MongoDB@01212004")
print(password)
cluster = pymongo.MongoClient(f"mongodb+srv://Mongo_Anyone:{password}@cluster0.rvtwf.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["PracticePrograms"]
col = db["ShootingGame"]

# data1 = {
#     "_id": "First",
#     "name": "Player1",
#     "score": 1
# }

name = input("What is your name?")
name = name.strip(" ")[0].upper() + name.strip(" ")[1:].lower()


def enter_name(player_name, got_name):
    post = col.find_one({"name": name})
    if post is not None:
        score = post["score"]
    else:
        col.insert_one({
            "name": name,
            "score": 0
        })
        score = 0
        print("name inserted")
    return got_name, score

"""
get name
if not get name then just play as guest and everything else is has no value

if name in database, then just get their score
if name not in database, just add it and set their score to 0



compare score to highscore, if score is bigger than their score replace the score in database
if not leave it be
let them run it again




"""