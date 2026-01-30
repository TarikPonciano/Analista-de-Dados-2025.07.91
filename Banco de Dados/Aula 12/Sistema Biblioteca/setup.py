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
    cursor.execute('''
INSERT INTO "Livro" (livro_titulo, livro_ano, id_autor) VALUES
('Dom Casmurro', 1899, 1),
('Memórias Póstumas de Brás Cubas', 1881, 1),
('Quincas Borba', 1891, 1),

('A Hora da Estrela', 1977, 2),
('Perto do Coração Selvagem', 1943, 2),

('O Guarani', 1857, 3),
('Iracema', 1865, 3),

('Reinações de Narizinho', 1931, 4),
('Sítio do Picapau Amarelo', 1920, 4),

('Alguma Poesia', 1930, 5),
('A Rosa do Povo', 1945, 5),

('Capitães da Areia', 1937, 6),
('Dona Flor e Seus Dois Maridos', 1966, 6),

('Vidas Secas', 1938, 7),
('São Bernardo', 1934, 7),

('Romanceiro da Inconfidência', 1953, 8),
('Ou Isto ou Aquilo', 1964, 8),

('O Alquimista', 1988, 9),
('Brida', 1990, 9),

('A Grande Arte', 1983, 10),
('Agosto', 1990, 10);

''')
    cursor.execute('''
INSERT INTO "Membro" (membro_nome, membro_email) VALUES
('Ana Beatriz Silva', 'ana.silva@email.com'),
('Carlos Henrique Souza', 'carlos.souza@email.com'),
('Mariana Oliveira', 'mariana.oliveira@email.com'),
('João Pedro Santos', 'joao.santos@email.com'),
('Fernanda Lima', 'fernanda.lima@email.com'),
('Lucas Gabriel Almeida', 'lucas.almeida@email.com'),
('Patrícia Ferreira', 'patricia.ferreira@email.com'),
('Rafael Costa', 'rafael.costa@email.com'),
('Juliana Martins', 'juliana.martins@email.com'),
('Bruno Rodrigues', 'bruno.rodrigues@email.com');

''')
    cursor.execute('''
INSERT INTO "Emprestimo" (id_livro, id_membro, emp_data, emp_devolucao) VALUES
(1,  1, '2025-01-05', '2025-01-15'),
(2,  2, '2025-01-08', '2025-01-20'),
(3,  3, '2025-01-10', '2025-01-25'),
(4,  4, '2025-01-12', NULL),
(5,  5, '2025-01-15', '2025-01-30'),
(6,  6, '2025-01-18', '2025-02-02'),
(7,  7, '2025-01-20', NULL),
(8,  8, '2025-01-22', '2025-02-05'),
(9,  9, '2025-01-25', '2025-02-10'),
(10, 10, '2025-01-28', NULL),

(11, 1,  '2025-02-01', '2025-02-12'),
(12, 2,  '2025-02-03', NULL),
(13, 3,  '2025-02-05', '2025-02-18'),
(14, 4,  '2025-02-07', '2025-02-20'),
(15, 5,  '2025-02-10', NULL),
(16, 6,  '2025-02-12', '2025-02-25'),
(17, 7,  '2025-02-15', NULL),
(18, 8,  '2025-02-18', '2025-03-02'),
(19, 9,  '2025-02-20', NULL),
(20, 10, '2025-02-22', '2025-03-05');

''')
    con.commit()

    # Bloco de Manipulações

    cursor.execute('''
    UPDATE "Membro"
    SET
        membro_nome = 'Mario Joaquim'
    WHERE
        membro_id = 8;
''')
    
    cursor.execute('''
    DELETE FROM "Emprestimo"
    WHERE id_livro = 4;
''')
    cursor.execute('''
    DELETE FROM "Livro"
    WHERE livro_id = 4;
''')
    
    cursor.execute('''
    DELETE FROM "Emprestimo"
    WHERE emp_id = (
    SELECT emp_id FROM "Emprestimo"
    WHERE emp_devolucao IS NULL
    LIMIT 1
    );
''')
    cursor.execute('''
    UPDATE "Emprestimo"
    SET
        emp_devolucao = CURRENT_DATE
    WHERE 
        emp_id = 15;
''')
    con.commit()
    print("Manipulações de Tabela Executadas com Sucesso")

    cursor.execute('''
    SELECT * FROM "Membro"
    ORDER BY membro_id ASC;
''')
    membros = cursor.fetchall()
    print("---------- Tabela de Membros ----------")
    print("ID | NOME | EMAIL")
    for membro in membros:
        print(f"{membro[0]} | {membro[1]} | {membro[2]}")

    cursor.execute('''
    SELECT livro_id, livro_titulo, livro_ano, autor_nome FROM "Livro"
    INNER JOIN "Autor" ON autor_id = id_autor
    ORDER BY livro_id ASC;
''')
    livros = cursor.fetchall()
    print("---------- Tabela de Livros ----------")
    print("ID | TITULO | ANO | AUTOR")
    for livro in livros:
        print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]}")
    
except Exception as error:
    print(f"HOUVER UM ERRO AO OPERAR O BANCO DE DADOS! ERRO: {error} ")
finally:
    #IMPORTANTE FECHAR AS CONEXÕES AO FINALIZAR A CONSULTA
    cursor.close()
    con.close()






