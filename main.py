from flask import Flask,render_template,request
import pymongo
app = Flask(__name__)

con  = pymongo.MongoClient()
db = con['flaskproject']
col = db['flask']

@app.route('/')
def register():
    return render_template("stud_detail.html")

@app.route('/welcome',methods=['GET','POST'])
def welcome():
    name1 = request.form.get('fname')
    name2 = request.form.get('lname')
    email = request.form.get('email')
    phno = request.form.get('phno')
    col.insert_one({'fname': name1, 'lname': name2, 'email': email, 'phno': phno})
    return render_template("welcome.html")

app.run()
