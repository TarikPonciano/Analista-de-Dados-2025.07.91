import psycopg2
# pip install psycopg2

DB_NAME = "Ecommerce"
DB_USER = "avnadmin"
DB_PASSWORD = "*************" 
DB_PORT = "28699" 
DB_HOST = "********ncloud.com"

con = psycopg2.connect(dbname=DB_NAME, user= DB_USER, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT)

cursor = con.cursor()

#Executar SQL
cursor.execute('SELECT * FROM "Produto";')
resultado = cursor.fetchall()
print(resultado)

print(resultado[0])
print(resultado[0][2])

cursor.close()
con.close()