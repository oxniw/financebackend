from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import date
from datetime import datetime

mon = {
        "1":{
            "data":{
                "1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]},"31":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        },
        "2":{
            "data":{
                "1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
        },

        "3":{

            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]},"31":{"data":[]}},
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        },
        "4":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
        },
        "5":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]}

            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
        },
        "6":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
        },
        "7":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]},"31":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        },
        "8":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]},"31":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        },
        "9":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
        },
        "10":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]},"31":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        },
        "11":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]    
        },
        "12":{
            "data":{"1":{"data":[]},"2":{"data":[]},"3":{"data":[]},"4":{"data":[]},"5":{"data":[]},"6":{"data":[]},"7":{"data":[]},"8":{"data":[]},"9":{"data":[]},"10":{"data":[]},"11":{"data":[]},"12":{"data":[]},"13":{"data":[]},"14":{"data":[]},"15":{"data":[]},"16":{"data":[]},"17":{"data":[]},"18":{"data":[]},"19":{"data":[]},"20":{"data":[]},"21":{"data":[]},"22":{"data":[]},"23":{"data":[]},"24":{"data":[]},"25":{"data":[]},"26":{"data":[]},"27":{"data":[]},"28":{"data":[]},"29":{"data":[]},"30":{"data":[]},"31":{"data":[]}
            },
            "set":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        },
    }
uri = "mongodb+srv://oo6139116:SzWWT4wcCRputGjU@cluster1.kuekvv6.mongodb.net/?retryWrites=true&w=majority&ssl=true&tlsAllowInvalidCertificates=true&appName=Cluster1"
app = Flask(__name__)
CORS(app, origins="*")
client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    socketTimeoutMS=3600000,
    connectTimeoutMS=3600000
)

db = client["myfirst"]
usersdata = db["usersdatatest"]
usersnameandpassword = db["usersnameandpasswordtest"]
usersname = db["usersnametest"]
userandwin = db["userandwintest"]
@app.route("/")
def home():
    return "Flask App is Running!", 200
def checkpassword(password:str,storewhy):
    c=True
    #if len(password)<8 or len(password)>20:
    #    storewhy.append("password must be at least 8 characters")
    #    c=False
    #if not any(char in "1234567890" for char in password):
    #    storewhy.append("password must have number at least 1 character")
    #    c=False
    #if not any(char.isupper() for char in password):
    #    storewhy.append("password must uppercase 1 character")
    #    c=False
    #if not any(char.islower() for char in password):
    #    storewhy.append("password must lowercase 1 character")
    #    c=False
    #if not any(char in "!@#$%^&*()-_=+[{]};:,<.>/?~`" for char in password):
    #    storewhy.append("password must have special character at least 1 character")
    #    c=False
    return c,storewhy
def checkusername(username:str,storewhy:any):
    d = None
    if len(username.split(" ")) <= 1:
        d = True
        return d,storewhy
    else:
        d = False
        storewhy.append("username must not have space")
        return d,storewhy
def exits(username:str,storewhy:any):
    d = None
    if usersname.find_one({"username": username}) is None:
        d = True
        return d,storewhy
    else:
        d = False
        storewhy.append("username already exists")
        return d,storewhy
@app.route("/api/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                return jsonify({"message":"ok","data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"name":f"{myusername}"})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})

    return jsonify({"ok":True})
@app.route("/api/signin",methods=["GET", "POST"])
def signin():

    startdat={
        "sources": {
            "money": 100,
            "win":0,
            "winstreak":0,
            "date":f"{date.today()}",
            "totaldate":{
                "y":f"{date.today()}".split("-")[0],
                "m":f"{date.today()}".split("-")[1],
                "d":f"{date.today()}".split("-")[2]
            },
            "year":{
                "2024":mon,
                "2025":mon
            },"balance":{
                "totalbalance":{
                    "mounth":{},
                    "year":{},
                    "day":{}
                }
            },
            "goal" :{
                "store":[],
                "goal":{}
            },
            "notes":[]
            }
}
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        storewhy = []
        ok,storewhy = checkpassword(myusername,storewhy)
        oks,storewhy = checkusername(myusername,storewhy)
        okss,storewhy = exits(myusername,storewhy)
        if okss and ok and oks:
            userandwin.insert_one({"win":{myusername:0,"c":"c","username":myusername}})
            usersname.insert_one({"username": myusername})
            usersnameandpassword.insert_one({myusername:mypassword})
            usersdata.insert_one({myusername:startdat})
            return jsonify({"message":"ok", "data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"name":f"{myusername}"})
        else:
            if not oks or not ok or not okss:
                return jsonify({"message":"notok","why":storewhy})
@app.route("/api/pulldata",methods=["GET", "POST"])
def pulldata():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        print(myusername,mypassword)
        if checkusername is not None:
            print(2)
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                print(3)
                return jsonify({"message":"ok","data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"name":f"{myusername}"})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/pullyear",methods=["GET", "POST"])
def pullyear():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myyear = data["year"]
        mymount = data["mounth"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            print(2)
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                print(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"][f"{mymount}"])
                print(len(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"][f"{mymount}"]))
                day = len(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"][f"{mymount}"])
                dayanddata = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"][f"{mymount}"]
                return jsonify({"data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"d":dayanddata})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/getdata",methods=["GET", "POST"])
def getdata():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myday = data["day"]
        myyear = data["year"]
        mymount = data["mounth"]
        myincome = 0
        myexpense = 0
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                print(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"])
                for i in usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]:
                    myincome += i["income"]
                    myexpense += i["expense"]
                return jsonify({"message":"OK",
                                "data":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"],
                                "totalexpense":myexpense,
                                "totalincome":myincome})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/updatedata",methods=["GET", "POST"])
def updatedatad():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myname = data["name"]
        myday = data["day"]
        myyear = data["year"]
        mymount = data["mounth"]
        myexpense = data["expense"]
        myincome = data["income"]
        mydescription = data["description"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                day_data = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]
                
                new_entry = {"name": myname, "expense": myexpense, "income": myincome, "description":mydescription}
                day_data.append(new_entry)
                update_query = { myusername: {"$exists": True} }
                update_data = { "$set": { f"{myusername}.sources.year.{myyear}.{mymount}.data.{myday}.data": day_data } }
                usersdata.update_one(update_query, update_data)
                for i in usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]:
                    myincome += i["income"]
                    myexpense += i["expense"]
                return jsonify({"message":"OK",
                                "data":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"],
                                "totalexpense":myexpense,
                                "totalincome":myincome})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/deletedata",methods=["GET", "POST"])
def deletedata():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myposition = data["position"]
        myday = data["day"]
        myyear = data["year"]
        mymount = data["mounth"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                day_data = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]
                print(day_data)
                del day_data[int(myposition)]
                update_query = { myusername: {"$exists": True} }
                update_data = { "$set": { f"{myusername}.sources.year.{myyear}.{mymount}.data.{myday}.data": day_data } }
                usersdata.update_one(update_query, update_data)
                return jsonify({"message":"ok","data":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/moveposition",methods=["GET", "POST"])
def moveposition():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myposition = data["position"]
        myday = data["day"]
        myyear = data["year"]
        mymount = data["mounth"]
        moveto = data["moveto"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                day_data = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]
                
                item = day_data.pop(int(myposition))
                day_data.insert(int(moveto), item)
                print(day_data)
                update_query = { myusername: {"$exists": True} }
                update_data = { "$set": { f"{myusername}.sources.year.{myyear}.{mymount}.data.{myday}.data": day_data } }
                usersdata.update_one(update_query, update_data)
                return jsonify({"message":"ok","data":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/getcost",methods=["GET", "POST"])
def getcost():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myday = data["day"]
        myyear = data["year"]
        mymount = data["mounth"]
        myincome = 0
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                name_dict = {}  # Dictionary to track indices
                name = []
                cost = []
                income = []
                percent = []
                for i in usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]:
                    if i["name"] not in name_dict:
                        name_dict[i["name"]] = len(name)
                        name.append(i["name"])
                        cost.append(0)
                        income.append(0)

                    index = name_dict[i["name"]]
                    cost[index] += i["expense"]
                    income[index] += i["income"]
                for i in usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"][f"{myday}"]["data"]:
                    myincome += i["income"]
                for i in cost:
                    percent.append(float("".join([ob for i, ob in enumerate(str((i / myincome) * 100)) if i < 5])))
                print(income,cost,name,percent)
                return jsonify({"data":{"name":name,"cost":cost,"percent":percent,"income":income}})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/returnusename",methods=["GET", "POST"])
def forgetpassword():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            doc = usersnameandpassword.find_one({ myusername: { "$exists": True } })
            print(doc)
            for username, password in doc.items():
                if username == myusername:
                    return jsonify({"message":"ok","password":password})
                print(f"{username}:{password}")
        else:
            return jsonify({"message":"notok","password":"username incorrect"})
@app.route("/api/pullmounth",methods=["GET", "POST"])
def pullmounth():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        mounthdata = [1,2,3,4,5,6,7,8,9,10,11,12]
        if checkusername is not None:
            print(2)
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                #print(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"])
                #mounth = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"]
                #for mounth,i in mounth.items():
                #    mounthdata.append(mounth)
                #print(mounthdata) 
                #print(len(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"]))
                #day = len(usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"][f"{mymount}"])
                #dayanddata = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{int(2023 + int(myyear))}"][f"{mymount}"]
                return jsonify({"data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"d":mounthdata})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/pullmounth3",methods=["GET", "POST"])
def pullmounth3():
    if request.method == "POST":
        print(1)
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        myyear = data["year"]
        mymount = data["mounth"]
        totalincome = 0
        totalexpense = 0
        checkusername = usersname.find_one({"username": myusername})
        count = 0   
        datastore = {}
        name_dict = {}
        name = []
        cost = []
        income = []
        datastore2={}
        if checkusername is not None:
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                if myyear is not None or mymount is not None:
                    mounthdata = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"][f"{myyear}"][f"{mymount}"]["data"]
                    #print(mounthdata)
                    for left1 , rights in mounthdata.items():
                        for leftt , rightd in rights.items():
                            #print(rightd)
                            if len(rightd) > 0:
                                for sourcesdata in rightd:
                                    for left , right in sourcesdata.items():
                                        if left == "income":
                                            totalincome += right
                                        if left == "expense":
                                            totalexpense += right

                    for left1 , right in mounthdata.items():
                        for (leftt , right) in (right.items()):
                            count += 1
                            datastore[f"{count} , {myyear}"] = []
                            if len(right) > 0:
                                for sourcesdata in right:
                                    #print(sourcesdata)
                                    datastore[f"{count} , {myyear}"].append(sourcesdata)
                    datastore2 = datastore.copy()
                    for left1, right in datastore.items():
                        if right == []:
                            del datastore2[left1]
                    #print(datastore2)
                    for day , data in datastore2.items():
                        for obj1 in data:
                            if not obj1["name"] in name_dict:
                                name_dict[obj1["name"]] = len(name)
                                name.append(obj1["name"])
                                cost.append(0)
                                income.append(0)
                            index = int(name_dict[obj1["name"]])
                            cost[index] += obj1["expense"]
                            income[index] += obj1["income"]
                            #print(name,cost,income)
                year:dict = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"]
                totalbalance = 0
                totalexpenseinyear = 0
                totalincomeinyear = 0
                for year,mounth in year.items():
                    for mounth,day in mounth.items():
                        for day,daydata in day["data"].items():
                            for obj in daydata["data"]:
                                #print("expense",obj["expense"])
                                #print("income",obj["income"])
                                totalbalance += (obj["income"] - obj["expense"])
                                totalexpenseinyear += obj["expense"]
                                totalincomeinyear += obj["income"]
                #print("totalbalance",totalbalance)
                update_query = { myusername: {"$exists": True} }
                update_data = { "$set": { f"{myusername}.sources.balance.totalbalance.mounth" : {f"{mymount}/{myyear}" : totalincome-totalexpense} } }
                usersdata.update_one(update_query, update_data)
                return jsonify({"data":{"totalincome":totalincome,
                                        "totalexpense":totalexpense,
                                        "datastore":datastore2,
                                        "name":name,
                                        "expense":cost,
                                        "income":income,
                                        "percent":[float("".join([ob for i, ob in enumerate(str((i / totalincome) * 100)) if i < 5])) for i in cost],
                                        "goal":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"],
                                        "store":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"]["store"],
                                        "totalbalance":totalbalance,
                                        "totalincomeinyear":totalincomeinyear,
                                        "totalexpenseinyear":totalexpenseinyear,
                                        }})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/add",methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        goalname = data["goalname"]
        price = int(data["price"])
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                store:list = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"]["store"]
                goal:dict = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"]["goal"]
                goal[goalname] = price
                goal.update(goal)
                update_query = { myusername: {"$exists": True} }
                update_data = { "$set": { f"{myusername}.sources.goal" : {"store":store,"goal":goal} } }
                usersdata.update_one(update_query, update_data)
                year:dict = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["year"]
                totalbalance = 0
                totalexpense = 0
                totalincome = 0
                for year,mounth in year.items():
                    for mounth,day in mounth.items():
                        for day,daydata in day["data"].items():
                            for obj in daydata["data"]:
                                totalbalance += (obj["income"] - obj["expense"])
                                totalexpense += obj["expense"]
                                totalincome += obj["income"]
                return jsonify({"message":"ok","data":usersdata.find_one({myusername:{"$exists":True}})[myusername],"name":f"{myusername}",
                                "goal":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"],
                                "store":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"]["store"],
                                "totalbalance":totalbalance,
                                "totalincome":totalincome,
                                "totalexpense":totalexpense})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route("/api/deletegoalname",methods=["GET", "POST"])
def deletegoalname():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        goalname = data["goalname"]
        price = int(data["price"])
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                goal:dict = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"]["goal"]
            
                if goalname in goal:
                    del goal[goalname]
                    update_query = { myusername: {"$exists": True} }
                    update_data = { "$set": { f"{myusername}.sources.goal.goal" : goal }}
                    usersdata.update_one(update_query, update_data)
                    return jsonify({"message":"ok",
                                    "goal":usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["goal"]})
                else:
                    return jsonify({"message":"notok","why":"goalname not found"})
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})

@app.route('/submit-note', methods=['POST'])
def submit_note():
    data = request.get_json()
    content = data.get('content', '').strip()
    myusername = data["username"]
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                if content:
                    note_doc = {
                        "content": content,
                        "timestamp": datetime.utcnow()
                    }
                    if "notes" in usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]:
                        notes:list = usersdata.find_one({myusername:{"$exists":True}})[myusername]["sources"]["notes"]
                        notes.append(note_doc)
                        print(notes)
                        update_query = { myusername: {"$exists": True} }
                        update_data:dict = { "$set": { f"{myusername}.sources.notes" : notes } }
                        result = usersdata.update_one(update_query, update_data)
                        return {"message": "Note stored", "id": str(result.upserted_id)}, 200
                    else:
                    
                        update_query = { myusername: {"$exists": True} }
                        update_data:dict = { "$set": { f"{myusername}.sources.notes" : [note_doc] } }

                        result = usersdata.update_one(update_query, update_data)
                        return {"message": "Note stored", "id": str(result.upserted_id)}, 200
                else:
                    return {"error": "Empty note"}, 400
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route('/get-notes', methods=['POST'])
def get_notes():
    data = request.get_json()
    myusername = data.get("username")
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        print(1)
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            print(2)
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            print(checkpassword)
            if checkpassword is not None:
                print(3)
                user_doc = usersdata.find_one({myusername: {"$exists": True}})
                if user_doc:
                    print(4)
                    notes = user_doc[myusername]["sources"]["notes"]
                    notes_without_id = [{k: v for k, v in note.items() if k != '_id'} for note in notes]
                    print(notes_without_id)
                    return {"notes": notes_without_id}, 200
                else:
                    return {"error": "User not found"}, 404
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
@app.route('/delete-note', methods=['POST'])
def delete_note():
    if request.method == "POST":
        data = request.json
        myusername = data["username"]
        mypassword = data["password"]
        checkusername = None
        checkusername = usersname.find_one({"username": myusername})
        if checkusername is not None:
            checkpassword = None
            checkpassword = usersnameandpassword.find_one({myusername:mypassword})
            if checkpassword is not None:
                data = request.get_json()
                myusername = data.get("username")
                note_content = data.get("content")
                print(myusername,note_content)
                if not myusername or not note_content:
                    return {"error": "Username and note content are required"}, 400
                user_doc = usersdata.find_one({myusername: {"$exists": True}})

                if user_doc:
                    notes = user_doc[myusername]["sources"]["notes"]
                    updated_notes = [note for note in notes if note.get("content") != note_content]
                    usersdata.update_one(
                        {myusername: {"$exists": True}},
                        {"$set": {f"{myusername}.sources.notes": updated_notes}}
                    )

                    return {"message": "Note deleted successfully"}, 200
                else:
                    return {"error": "User not found"}, 404
            else:
                return jsonify({"message":"notok","why":"password incorrect or username incorrect"})
        else:
            return jsonify({"message":"notok","why":"username incorrect"})
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)