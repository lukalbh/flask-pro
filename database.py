import mysql.connector
from mysql.connector import Error

class DBconnection:
    def __init__(self, host="babylone",database="lambrech",user="lambrech",password="lambrech", ssl_disabled=True):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.ssl_disabled = ssl_disabled
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            ssl_disabled=self.ssl_disabled  # Désactiver SSL
        )
        if self.connection.is_connected():
            print("connecter a la bd")
        else:
            print("pas connecter")

    def fetch_one(self, query, params):
        """Exécute une requête SQL et récupère la première ligne du résultat."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()  # Utilise fetchone pour récupérer la première ligne
            return result  # Retourne la première ligne
        except Error as e:
            print(f"Erreur lors de la récupération des données : {e}")
            return None
        finally:
            cursor.close()
