import sqlite3

DB_FILE="discobandit.db" # db used for this project. delete file if you want to remove all data/login info.


def create_tables():
    db = sqlite3.connect(DB_FILE) # Open if file exists, otherwise create
    c = db.cursor()

    c.execute("CREATE TABLE if not exists user_info(username TEXT PRIMARY KEY, password TEXT, preferences TEXT)")
    c.execute("CREATE TABLE if not exists recipes(user TEXT, title TEXT, ingredients TEXT, instructions TEXT, images TEXT)")

    db.commit()

    db.close()

def add_user(username, password):
    ''' insert credentials for newly registered user into database '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO user_info VALUES(?, ?, ?)", (username, password, "none"))

    db.commit() #save changes
    db.close() #close database

def check_user(username):
    ''' check if a username has already been taken when registering '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for entry in c.execute("SELECT user_info.username FROM user_info"):
        if(entry[0] == username):
            db.close()
            return True

    db.close()
    return False

def auth_user(username, password):
    ''' authenticate a user attempting to log in '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for entry in c.execute("SELECT user_info.username, user_info.password FROM user_info"):
        if(entry[0] == username and entry[1] == password):
            db.close()
            return True

    db.close()
    return False

def add_recipe(username,name,ingred, instruct, pics):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("INSERT INTO recipes VALUES(?,?,?,?,?)", (username, name, ingred, instruct, pics))
    db.close()
    return True

def user_recipes():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    recipes = {}
    for num in c.execute("SELECT * FROM recipes"):
        title = num[1]

        recipes[title] = [
            num[0],
            num[2],
            num[3],
            num[4],
        ]
    db.close()
    return recipes


create_tables()
