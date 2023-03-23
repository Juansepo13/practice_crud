import pandas as pd
import pymysql

# Conexión a la base de datos de MySQL
connection = pymysql.connect(host='localhost',
                             user='juansepo13',
                             password='winter13',
                             db='pokemon_db',
                             cursorclass=pymysql.cursors.DictCursor)

# Carga el archivo de Excel
df = pd.read_excel('//wsl.localhost/Ubuntu/home/juansepo13/practice_crud/database/pokemon_database.csv', sheet_name='pokemon_database')

# Inserta los datos en la tabla de MySQL
with connection.cursor() as cursor:
    for index, row in df.iterrows():
        sql = "INSERT INTO pokemon (columna_1, columna_2, columna_3) VALUES (%s, %s, %s)"
        cursor.execute(sql, (str(row['columna_1']), str(row['columna_2']), str(row['columna_3'])))
    connection.commit()
