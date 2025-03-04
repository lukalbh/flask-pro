from flask import Flask, request
from flask import render_template
from flask import redirect, url_for, session
import mysql.connector

# Création de l'application Flask
app = Flask(__name__)
app.secret_key= "key"

db = mysql.connector.connect(user = "lambrech",password = "lambrech",host = "babylone",database = "lambrech", ssl_disabled=True)

mycursor = db.cursor()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #enregistrez les données de session
        username = request.form["username"]
        password = request.form["password"]

        mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = mycursor.fetchone()
        if user:      
            session["username"] = username
            return redirect(url_for("dash"))
        else:
            return render_template("login.html", message="identifiant incorrect")
    return render_template("login.html")

#rediriger vers /login/
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/dashboard')
def dash():
    if "username" in session :
        print(session["username"])
        return render_template("dashboard.html")
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

if __name__ == '__main__':
    app.run(debug=True)


