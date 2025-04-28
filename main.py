import functools
from flask import Flask, request
from flask import render_template
from flask import redirect, url_for, session
from database import DBconnection # Importation de la classe DBconnection pour gérer la connexion à la base de données
from bokeh.resources import CDN # Importation de CDN pour charger les ressources de Bokeh
from plot import * # Importation des fonctions liées aux graphiques (evolutionTemp, plotex, etc.)

# Création de l'application Flask
app = Flask(__name__)
app.secret_key = 'luka' 

"""
Décorateur créée pour debugger en cas d'érreur
"""
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Appel de la fonction : {func.__name__}") # affiche le nom de la fonction
        return func(*args, **kwargs)
    return wrapper

# Objet instancié
db = DBconnection()
# Connexion a la DB
db.connect()


"""
Route /login qui renvoie vers un formulaire de connexion
"""
@app.route('/login', methods=["GET", "POST"])
@trace
def login():
    if request.method == "POST":
        # Enregistre les données du formulaire
        username = request.form["username"]
        password = request.form["password"]

        #permet de faire une requete
        user = db.fetch_one("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if user:      
            session["username"] = username # Stockage du nom d'utilisateur dans la session
            return redirect(url_for("dash")) # redirection vers la route du dashboard
        else:
            """
            Si la session n'est pas authentifié alors je renvoie vers la meme page
            """
            return render_template("login/login.html") 
    return render_template("login/login.html")

"""
Route pour permettre au Technicien de se connecter pour configurer l'IHM
"""
@app.route('/loginTech', methods=["GET", "POST"])
@trace
def loginTech():
    if request.method == "POST":
        # Enregistre les données du formulaire
        username = request.form["username"]
        password = request.form["password"]

        # Requete stocker dans user qui cherche le mdp et l'user
        user = db.fetch_one("SELECT * FROM techniciens WHERE username = %s AND password = %s", (username, password))
        db.close() #fermeture de la db
        if user:      
            session["username"] = username
            return redirect(url_for("configTech"))
        else:
            """
            Si la session n'est pas authentifié alors je renvoie vers la meme page
            """
            return render_template("login/loginTech.html", message="identifiant incorrect")
    return render_template("login/loginTech.html")



#rediriger vers /login/
@app.route('/')
@trace
def home():
    return redirect(url_for('login'))

"""
Route vers le Dashboard
"""
@app.route('/dashboard')
@trace
def dash():
    if "username" in session: # vérification si l'utilisateur est connecté
        # Requête pour récuperer la moyenne des températures
        moyTemp = db.fetch_one("SELECT AVG(temperature) AS moyenne_temperature FROM temp_data", ()) 
        tempMoyenne = moyTemp[0] # récuperation de la valeur tuple et stocker dans une variable
        tempMoyenne = round(tempMoyenne, 2) # arrondis de la valeur a 2 decimales
        
        #génération des graphiques Bokeh
        bokeh_components = evolutionTemp()
        bokeh_components2 = evolutionTemp2()

        """
        Renvoie de la page avec :
            - les graphiques (script, script2,div, div2)
            - la moyenne de température
        """
        return render_template("dashboard/dashboard.html", username=session["username"],ressources=CDN.render(), 
                               script=bokeh_components["script"], 
                               div=bokeh_components["div"],
                               script2=bokeh_components2["script"], 
                               div2=bokeh_components2["div"],
                               tempMoyenne=tempMoyenne)
    else:
        """
        Si la session est pas authentifié on renvoie vers login
        """
        print("no session")
        return redirect(url_for("login"))


"""
Route pour le chemin de déconnexion
"""
@app.route('/logout')
@trace
def logout():
    session.pop("username", None)  # Supprime l'utilisateur de la session
    return redirect(url_for("login")) # Retourne vers login

"""
Route pour afficher les graphiques des capteurs
"""
@app.route('/graphique')
@trace
def graph():
    if "username" in session :
        bokeh_components = plotex()
        script = bokeh_components["script"]
        div = bokeh_components["div"]
        print(session["username"])
        return render_template("graphique.html",ressources=CDN.render(), script=script, div=div)
    else:
        return redirect(url_for("login"))

"""
Route pour la localisation des capteurs
"""
@app.route('/localisation')
@trace
def localisation():
    if "username" in session :
        print(session["username"])
        return render_template("localisation.html")
    else:
        return redirect(url_for("login"))

"""
Route qui renvoie vers la page de configuration pour le technicien
"""
@app.route('/configTech', methods=["GET", "POST"])
@trace
def configTech():
    if "username" in session:
        print(session["username"])
        return render_template("login/config.html", username=session["username"])
    else:
        return redirect(url_for("loginTech"))

if __name__ == '__main__':
    app.run(debug=True)