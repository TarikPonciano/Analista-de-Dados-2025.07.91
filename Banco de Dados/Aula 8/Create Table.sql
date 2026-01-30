CREATE TABLE "Departamento"(
dept_cod integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
dept_nome varchar(255) NOT NULL,
dept_faturamento NUMERIC(10,2) NOT NULL DEFAULT 0
);

CREATE TABLE "Funcionario"(
func_cod integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
func_nome varchar(255) NOT NULL,
func_cpf char(11) NOT NULL,
func_cargo varchar(255) NOT NULL DEFAULT 'Sem Cargo',
cod_dept integer NOT NULL,
CONSTRAINT fk_dept_func FOREIGN KEY (cod_dept) REFERENCES "Departamento"(dept_cod)
);