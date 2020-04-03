import os
from app import app
from flask import render_template, request, redirect, session, url_for


from flask_pymongo import PyMongo

app.secret_key = b' _5y2L"F4Q8z\n\xec]?'

# name of database
app.config['MONGO_DBNAME'] = 'events'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:aY9m2EzN9qAH2nf3@cluster0-1mug4.mongodb.net/events?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX


@app.route('/index')

def index():
    # session['']
    #connect to the database
    collection = mongo.db.events
    #query the database
    #store those events as a list of dictionaries called events
    events = list(collection.find({}))
    print (events)
    #print the events

    return render_template('index.html', events = events)

#TRYING TO SHOW ALL THE USER'S EVENTS
#@app.route('/name/<name>')
#def name(name):
    #session['']
    #connect to the database
    #collection = mongo.db.events
    #query the database
    #store those events as a list of dictionaries called events
    #events = list(collection.find({"user": name}))
    #print (events)
    #print the events

    return render_template('index.html', events = events)

@app.route('/display')
# CONNECT TO DB, ADD DATA
def display():
    #connect to the database
    collection = mongo.db.events
    #query the database
    #store those events as a list of dictionaries called events
    events = list(collection.find({}))
    print (events)
    #print the events

    return render_template('display.html', events = events)

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events

    # insert new data
    collection.insert({"event_name": "test", "event_date": "today"})

    # return a message to the user
    return "you added an event to the database."

@app.route('/results', methods = ["get", "post"])

def results():
    # store userinfo from the form
    user_info = dict(request.form)
    print(user_info)
    # get the event_name and the event_date and store them
    event_time = user_info["event_time"]
    print("the event time is", event_time)
    event_date = user_info["event_date"]
    print("the event date is", event_date)

    borough = user_info["category"]
    print(borough)

    # connect to the database
    collection = mongo.db.events

    x = list(collection.find({"borough": borough}))
    print (x)


    # return a message to the user
    return render_template("display.html", events = x)

@app.route("/secret")
def secret():
    #connect to the database
    collection = mongo.db.events
    #delete everything from the database
    #invoke the delete_many method on the collection
    collection.delete_many({})
    return redirect('/index')


@app.route("/Manhattan")
def Manhattan():
    collection = mongo.db.events
    Manhattan = list(collection.find({"event_location": "Manhattan"}))
    print (Manhattan)
    return render_template('Manhattan.html', events = Manhattan)

@app.route("/Brooklyn")
def Brooklyn():
    collection = mongo.db.events
    Brooklyn = list(collection.find({"event_location": "Brooklyn"}))
    print (Brooklyn)
    return render_template('Brooklyn.html', events = Brooklyn)

@app.route("/Queens")
def Queens():
    collection = mongo.db.events
    Queens = list(collection.find({"event_location": "Queens"}))
    print (Queens)
    return render_template('Queens.html', events = Queens)

@app.route("/The_Bronx")
def TheBronx():
    collection = mongo.db.events
    TheBronx = list(collection.find({"event_location": "The Bronx"}))
    print (The_Bronx)
    return render_template('The_Bronx.html', events = The_Bronx)

@app.route("/Staten_Island")
def StatenIsland():
    collection = mongo.db.events
    StatenIsland = list(collection.find({"event_location": "Staten Island"}))
    print (Staten_Island)
    return render_template('Staten_Island.html', events = Staten_Island)

@app.route("/admin")
def admin():
    return render_template('newevent.html')

@app.route("/newevent", methods = ["get", "post"])
def newevent():
    user_info = dict(request.form)
    print(user_info)

    number = user_info["number"]
    print("the amount of people that can fit is", number)

    starttime = user_info["starttime"]
    print("this class is starting at", starttime)

    date = user_info["date"]
    print("the date of the event is", date)

    endtime = user_info["endtime"]
    print("this class is ending at", endtime)

    address = user_info["address"]
    print("the address of this class is:", address)

    level = user_info["level"]
    print("the level of this class is", level)

    borough = user_info["category"]
    print("this class is in:", borough)
    #connect to my MONGO
    collection = mongo.db.events

    collection.insert({"number": number, "starttime": starttime, "endtime": endtime, "address": address, "level": level, "borough": borough, "date": date})
    #insert all info to MONGO
    return render_template('newevent.html')

@app.route("/handle")
def handle():
    collection = mongo.db.events
@app.route('/', methods = {"GET", "POST"})

@app.route('/signup', methods = {"GET", "POST"})
def signup():
    #has the user filled out the form yet?
    if request.method == "POST":
        # store the info from the form
        users = mongo.db.users
        print (dict(request.form))
        existing_user = users.find_one({"name" : request.form["name"]})

        if existing_user is None:
            users.insert({"name" : request.form["name"], "password": request.form["password"]})
            session["username"] = request.form['name']
            return redirect(url_for("index"))

        return render_template("login.html")

    return render_template("signup.html")
        #connect to the database, users collection
        #check to see if the emial is in the database

@app.route('/login', methods = {"POST"})
def login():
    #has the user filled out the form yet?
    if request.method == "POST":
        users = mongo.db.users
        login_user = users.find_one({"name" : request.form["username"]})

        if login_user:
            if request.form["password"]== login_user["password"]:
                session["username"] = request.form["username"]
                return redirect(url_for("index"))
        return "Invalid username/password combination"


    return render_template("signup.html")
