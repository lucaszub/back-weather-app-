import mysql.connector

# Remplacez les valeurs suivantes par les informations de votre base de données
host = "mydb.cv042okomolf.eu-west-3.rds.amazonaws.com"
user = "Lucas"
password = "Medard44"
database = "mydb"
port = 3306  # Remplacez par le port utilisé par votre instance de base de données si différent de 3306

try:
    # Se connecter à la base de données
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    if connection.is_connected():
        print("Connected to MySQL database")
        
        # Exécuter une requête SQL
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ma_table")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print("Error connecting to MySQL database", e)

finally:
    # Fermer la connexion à la base de données
    if 'connection' in locals():
        connection.close()
        print("MySQL connection is closed")
