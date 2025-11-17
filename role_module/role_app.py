from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        
        password="root75",
        database="hrm_db"
    )

 

@app.route("/")
def dashboard():
    db = get_db(); c=db.cursor(dictionary=True)
    c.execute("SELECT * FROM role WHERE status=1")
    roles = c.fetchall()
    db.close()
    return render_template("dashboard.html", roles=roles)

@app.route("/create", methods=["GET","POST"])
def create():
    if request.method=="POST":
        name=request.form["name"]
        desc=request.form["desc"]
        db=get_db(); c=db.cursor()
        c.execute("INSERT INTO role(role_name,description,created_at,updated_at,status) VALUES (%s,%s,%s,%s,1)",
                  (name,desc,datetime.now(),datetime.now()))
        db.commit(); db.close()
        return redirect("/")
    return render_template("create.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    db=get_db(); c=db.cursor(dictionary=True)
    if request.method=="POST":
        name=request.form["name"]
        desc=request.form["desc"]
        c2=db.cursor()
        c2.execute("UPDATE role SET role_name=%s, description=%s, updated_at=%s WHERE role_id=%s",
                   (name,desc,datetime.now(),id))
        db.commit(); db.close()
        return redirect("/")
    c.execute("SELECT * FROM role WHERE role_id=%s",(id,))
    role=c.fetchone()
    db.close()
    return render_template("edit.html", role=role)

@app.route("/delete/<int:id>")
def delete(id):
    db=get_db(); c=db.cursor()
    c.execute("UPDATE role SET status=0 WHERE role_id=%s",(id,))
    db.commit(); db.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)