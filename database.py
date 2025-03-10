import mysql.connector
from mysql.connector import Error


#Class pour le singleton
class Singleton(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'): 
            org = super(Singleton, cls)  
            cls._instance = org.__new__(cls, *args, **kw) 
        return cls._instance

class DBconnection(Singleton):

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
            self.connect()

            # Exécuter la requête SQL avec les paramètres donnés
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()  # Utiliser fetchone pour récupérer la première ligne
            cursor.close()  # Fermer le curseur après l'exécution

            return result  # Retourner la première ligne récupérée
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            return None
        except Exception as e:
            print(f"Erreur générale : {e}")
            return None