from flask import Flask,render_template,request
import pymongo
app = Flask(__name__)

con  = pymongo.MongoClient()
db = con['flaskproject']
col = db['flask']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/welcome',methods=['GET','POST'])
def welcome():
    name1 = request.form.get('fname')
    name2 = request.form.get('lname')
    col.insert_one({'fname':name1,'lname':name2})
    return render_template("welcome.html")

app.run()
