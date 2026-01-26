#Abrir o terminal e executar o comando 'pip install psycopg2'
import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#Estabelece a conexão com o banco
con = psycopg2.connect(
    dbname = DB_NAME,
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    password = DB_PASSWORD
)
#Cria a ferramenta de interação com o banco
cursor = con.cursor()

#Código SQL
cursor.execute('''
SELECT VERSION();
''')
resultado = cursor.fetchall()
print(resultado[0][0])

#IMPORTANTE FECHAR AS CONEXÕES AO FINALIZAR A CONSULTA
cursor.close()
con.close()

