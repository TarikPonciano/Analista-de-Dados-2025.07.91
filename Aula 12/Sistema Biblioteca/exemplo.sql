CREATE TABLE "Membro"(
    membro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    membro_nome varchar(255) NOT NULL,
    membro_email varchar(255) NOT NULL,
    CONSTRAINT chk_email_valido CHECK(membro_email LIKE '%@%')
);

CREATE TABLE "Autor"(
    autor_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    autor_nome varchar(255) NOT NULL
);

CREATE TABLE "Livro"(
    livro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    livro_titulo varchar(255) NOT NULL,
    livro_ano integer NOT NULL,
    id_autor integer NOT NULL,
    CONSTRAINT fk_livro_autor 
    FOREIGN KEY (id_autor) 
    REFERENCES "Autor"(autor_id)
);

CREATE TABLE "Emprestimo"(
    emp_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_livro integer NOT NULL,
    id_membro integer NOT NULL,
    emp_data date NOT NULL DEFAULT CURRENT_DATE,
    emp_devolucao date,
    CONSTRAINT fk_emp_livro FOREIGN KEY (id_livro) REFERENCES "Livro"(livro_id),
    CONSTRAINT fk_emp_membro FOREIGN KEY (id_membro) REFERENCES "Membro"(membro_id)
);