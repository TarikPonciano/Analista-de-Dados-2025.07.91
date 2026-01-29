# Missões da Atividade

# 1. Criar as tabelas Autores, Livros, Membros e Empréstimo

# 2. Inserir pelo menos 10 Autores
# 3. Inserir pelo menos 20 Livros
# 4. Inserir pelo menos 5 membros
# 5. Inserir pelo menos 20 empréstimos válidos

# (Usar IA para gerar os dados)

# 6. Realizar a modificação do nome de um Membro
# 7. Remover um livro que comece com a letra "A"
# 8. Remover um empréstimo em que a data de devolução seja nula (se houver)
# 9. Modificar a data de devolução de um empréstimo para o dia de hoje

# 10. Exibir a lista de membros
# 11. Exibir a lista de livros
# 12. Exibir a lista de empréstimos, mostrando nome do livro e nome do membro
  


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

    #Remove as tabelas já existentes
    cursor.execute('''
    DROP TABLE IF EXISTS "Emprestimo";
''')
    cursor.execute('''
    DROP TABLE IF EXISTS "Membro";
''')
    cursor.execute('''
    DROP TABLE IF EXISTS "Livro";
''')
    cursor.execute('''
    DROP TABLE IF EXISTS "Autor";
''')
    print("TABELAS REMOVIDAS COM SUCESSO!")
    con.commit()

    #Criar a tabela de Membros (SQL)
    cursor.execute('''
    CREATE TABLE "Membro"(
    membro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    membro_nome varchar(255) NOT NULL,
    membro_email varchar(255) NOT NULL,
    CONSTRAINT chk_email_valido CHECK(membro_email LIKE '%@%')
);
    ''')
    print("Tabela Membro Criada Com Sucesso!")

    cursor.execute('''
    CREATE TABLE "Autor"(
    autor_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    autor_nome varchar(255) NOT NULL
);
''')
    print("Tabela Autor Criada Com Sucesso!")
    
    cursor.execute('''
    CREATE TABLE "Livro"(
    livro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    livro_titulo varchar(255) NOT NULL,
    livro_ano integer NOT NULL,
    id_autor integer NOT NULL,
    CONSTRAINT fk_livro_autor 
    FOREIGN KEY (id_autor) 
    REFERENCES "Autor"(autor_id)
);

''')
    
    print("Tabela Livro Criada Com Sucesso!")

    cursor.execute('''
CREATE TABLE "Emprestimo"(
    emp_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_livro integer NOT NULL,
    id_membro integer NOT NULL,
    emp_data date NOT NULL DEFAULT CURRENT_DATE,
    emp_devolucao date,
    CONSTRAINT fk_emp_livro FOREIGN KEY (id_livro) REFERENCES "Livro"(livro_id),
    CONSTRAINT fk_emp_membro FOREIGN KEY (id_membro) REFERENCES "Membro"(membro_id)
);
''')
    
    print("Tabela Empréstimo Criada Com Sucesso!")
    con.commit()

    print("Tabelas Criadas com Sucesso!")


    print("PREENCHENDO TABELAS DO BANCO...")

    cursor.execute('''
    INSERT INTO "Autor" (autor_nome) VALUES
('Machado de Assis'),
('Clarice Lispector'),
('José de Alencar'),
('Monteiro Lobato'),
('Carlos Drummond de Andrade'),
('Jorge Amado'),
('Graciliano Ramos'),
('Cecília Meireles'),
('Paulo Coelho'),
('Rubem Fonseca');
''')
    con.commit()

    
except Exception as error:
    print(f"HOUVER UM ERRO AO OPERAR O BANCO DE DADOS! ERRO: {error} ")
finally:
    #IMPORTANTE FECHAR AS CONEXÕES AO FINALIZAR A CONSULTA
    cursor.close()
    con.close()






