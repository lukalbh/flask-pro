from flask import Flask, request
from flask import render_template
from flask import redirect, url_for, session
import mysql.connector
from database import DBconnection

# Création de l'application Flask
app = Flask(__name__)

app.secret_key= "key"

db = DBconnection()
db.connect()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #enregistrez les données de session
        username = request.form["username"]
        password = request.form["password"]

        #permet de faire une requete
        user = db.fetch_one("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if user:      
            #vérifie la session si le username est = au username
            session["username"] = username
            return redirect(url_for("dash"))
        else:
            return render_template("login/login.html", message="identifiant incorrect")
    return render_template("login/login.html")


@app.route('/loginTech', methods=["GET", "POST"])
def loginTech():
    if request.method == "POST":
        #enregistrez les données de session
        username = request.form["username"]
        password = request.form["password"]

        #permet de faire une requete
        user = db.fetch_one("SELECT * FROM techniciens WHERE username = %s AND password = %s", (username, password))
        db.close()
        if user:      
            session["username"] = username
            return redirect(url_for("configTech"))
        else:
            return render_template("login/loginTech.html", message="identifiant incorrect")
    return render_template("login/loginTech.html")



#rediriger vers /login/
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/dashboard')
def dash():
    if "username" in session:
        return render_template("dashboard/dashboard.html", username=session["username"]) #username est une variable de la page dashboardMain.html pour mettre le nom
    else:
        print("no session")
        return redirect(url_for("login"))
        
@app.route('/logout')
def logout():
    session.pop("username", None)  # Supprime l'utilisateur de la session
    return redirect(url_for("login"))

@app.route('/graphique')
def graph():
    if "username" in session :
        print(session["username"])
        return render_template("graphique.html")
    else:
        return redirect(url_for("login"))

@app.route('/localisation')
def localisation():
    if "username" in session :
        print(session["username"])
        return render_template("localisation.html")
    else:
        return redirect(url_for("login"))


@app.route('/configTech', methods=["GET", "POST"])
def configTech():
    if "username" in session:
        print("coucou")
        return render_template("login/config.html", username=session["username"])
    else:
        return redirect(url_for("loginTech"))

if __name__ == '__main__':
    app.run(debug=True)