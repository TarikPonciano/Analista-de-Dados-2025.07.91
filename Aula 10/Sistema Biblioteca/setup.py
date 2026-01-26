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


try:
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

    #Criar a tabela de Membros (SQL)
    cursor.execute('''
    CREATE TABLE "Membro"(
    membro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    membro_nome varchar(255) NOT NULL,
    membro_email varchar(255) NOT NULL,
    CONSTRAINT chk_email_valido CHECK(membro_email LIKE '%@%')
);
    ''')
    con.commit()
    print("Tabela Membro Criada com Sucesso!")
    
except Exception as error:
    print(f"HOUVER UM ERRO AO OPERAR O BANCO DE DADOS! ERRO: {error} ")
finally:
    #IMPORTANTE FECHAR AS CONEXÕES AO FINALIZAR A CONSULTA
    cursor.close()
    con.close()






