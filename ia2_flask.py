from flask import Flask, redirect, url_for, request,render_template
from ia2_sqlite3 import *

app=Flask(__name__)
users={"test1":"pass1"}

@app.route("/")
def view_form():
        return render_template("loginpageun.html")

@app.route('/login')
def loginpage():
    return render_template("loginpageun.html")

@app.route("/loggingin",methods=["POST"])
def handlelogin():

    if request.method=="GET":
        return (render_template("loginpageun.html"))
    
    elif request.method=="POST":
        uname=request.form["username"]
        pwd=request.form["password"]

        if uname in users and users[uname]==pwd:
            return(render_template("unoteshome.html"))
    
        else:
            return (render_template("loginpageun.html",a="Invalid Credentials"))

@app.route("/home",methods=["GET","POST"])
def getcontactinfo():

    if request.method=="GET":
        return (render_template("unoteshome.html"))
    
    
    fname=request.form["fname"]
    lname=request.form["lname"]
    phoneno=request.form["phoneno"]
    emailid=request.form["emailid"]

    ctiobj=CIS()
    ctiobj.ConnectDB()
    ctiobj.CreateTable()

    if(request.form["action_button"]=="Submit"):
         ctiobj.AddInfo(fname,lname,phoneno,emailid)
         print("Yay")
         pass


    return(render_template("unoteshome.html",fn=fname,ln=lname,pn=phoneno,em=emailid))

if __name__=="__main__":
    app.run(port=9000)