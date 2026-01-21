SELECT * FROM "Cliente";

INSERT INTO "Cliente" 
VALUES (default, 'José Clayton', '12345678910', 1.75,'2012-10-17');

INSERT INTO "Cliente" (cli_nome, cli_cpf)
VALUES ('Maria Rosário', '12345678944'), ('Jão Silva', '32165498778');

INSERT INTO "Cliente" (cli_nome, cli_cpf, cli_altura, cli_nasc) VALUES
('Ana Paula Souza',   '11122233344', 1.62, '1995-03-12'),
('Bruno Henrique',    '22233344455', 1.80, '1990-07-25'),
('Carla Mendes',      '33344455566', 1.68, '1998-11-02'),
('Daniel Ribeiro',    '44455566677', 1.75, '1987-01-19'),
('Eduarda Lima',      '55566677788', 1.60, '2000-05-30'),
('Felipe Martins',    '66677788899', 1.82, '1993-09-14'),
('Gabriela Rocha',    '77788899900', 1.65, '1996-12-08'),
('Henrique Alves',    '88899900011', 1.78, '1989-04-21'),
('Isabela Torres',    '99900011122', 1.70, '1997-06-10'),
('João Pedro Costa',  '10111213141', 1.73, '1992-02-03'),
('Karina Nogueira',   '12131415161', 1.66, '1999-08-17'),
('Lucas Ferreira',    '14151617181', 1.85, '1988-10-05'),
('Mariana Pacheco',   '16171819201', 1.64, '2001-01-27'),
('Nicolas Araujo',    '18192021222', 1.79, '1994-03-09'),
('Olivia Barros',     '20212223242', 1.58, '2002-07-18'),
('Paulo Victor',      '22232425262', 1.76, '1991-11-11'),
('Renata Guedes',     '24252627282', 1.69, '1995-04-06'),
('Sergio Fonseca',    '26272829302', 1.81, '1986-06-29'),
('Tatiane Lopes',     '28293031322', 1.63, '1998-09-01'),
('Victor Moreira',    '30313233342', 1.77, '1993-12-15');


INSERT INTO "Traje" (nome, tipo, tamanho, valor, genero) VALUES
('Smoking Clássico Preto',      'Formal',        'M', 250.00, 'Masculino'),
('Vestido Longo de Festa Azul', 'Festa',         'G', 320.00, 'Feminino'),
('Terno Slim Cinza',            'Formal',        'G', 280.00, 'Masculino'),
('Vestido de Madrinha Rosa',    'Cerimonial',    'M', 300.00, 'Feminino'),
('Fantasia Batman',             'Fantasia',      'M', 180.00, 'Masculino'),
('Fantasia Mulher-Maravilha',   'Fantasia',      'P', 190.00, 'Feminino'),
('Traje Social Preto',          'Social',        'GG',220.00, 'Masculino'),
('Vestido de Noiva Clássico',   'Casamento',     'M', 800.00, 'Feminino'),
('Terno Infantil Azul',         'Formal Infantil','P',150.00, 'Masculino'),
('Vestido Infantil Princesa',   'Festa Infantil','P',160.00, 'Feminino');

SELECT * FROM "Traje";

INSERT INTO "Aluguel" (cod_cliente, cod_traje, data_aluguel, data_devolucao, situacao) VALUES
(1,  1, '2025-01-05', '2025-01-10', 'Devolvido'),
(18,  3, '2025-01-08', '2025-01-12', 'Devolvido'),
(20,  2, '2025-01-15', NULL,         'Em aberto'),
(14,  5, '2025-01-18', '2025-01-20', 'Devolvido'),
(12,  8, '2025-01-19', NULL,         'Em aberto');

SELECT * FROM "Aluguel";
