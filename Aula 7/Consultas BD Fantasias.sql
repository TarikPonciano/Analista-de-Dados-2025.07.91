/* =========================================================
   INSERÇÃO DE DADOS NA TABELA CLIENTE
   ========================================================= */

/* 
Insere um novo cliente na tabela "Cliente".
- default: o banco gera automaticamente o cod_cliente (SERIAL)
- 'Gesonel': nome do cliente
- '11111111111': CPF
- 0.3: altura
- '2022-06-06': data de nascimento
*/
INSERT INTO "Cliente"
VALUES (default, 'Gesonel', '11111111111', 0.3, '2022-06-06');

/* 
Consulta todos os registros da tabela Cliente
para verificar se o dado foi inserido corretamente
*/
SELECT * FROM "Cliente";


/* =========================================================
   CONSULTA E INSERÇÃO NA TABELA TRAJE
   ========================================================= */

/* 
Consulta todos os trajes cadastrados
*/
SELECT * FROM "Traje";

/* 
Insere um novo traje na tabela "Traje".
- default: gera automaticamente o cod_traje
- 'Disfarce': nome do traje
- 'Disfarce': tipo do traje
- 'Todos': tamanho
- 600: valor do aluguel
- 'Pato': gênero associado ao traje
*/
INSERT INTO "Traje"
VALUES (default, 'Disfarce', 'Disfarce', 'Todos', 600, 'Pato');


/* =========================================================
   CONSULTA E INSERÇÃO NA TABELA ALUGUEL
   ========================================================= */

/* 
Consulta todos os registros de aluguel
*/
SELECT * FROM "Aluguel";

/* 
Insere um novo aluguel.
- default: gera o cod_aluguel automaticamente
- 24: código do cliente que realizou o aluguel
- 11: código do traje alugado
- CURRENT_DATE: data atual do sistema (data do aluguel)
- '2026-01-28': data prevista para devolução
- 'Em aberto': situação do aluguel
*/
INSERT INTO "Aluguel"
VALUES (default, 24, 11, CURRENT_DATE, '2026-01-28', 'Em aberto');


/* =========================================================
   ATUALIZAÇÃO DE DADOS (UPDATE)
   ========================================================= */

/* 
Atualiza o nome do cliente.
- Altera o campo cli_nome
- Apenas para o cliente cujo cod_cliente = 24
*/
UPDATE "Cliente"
SET
    cli_nome = 'Mestre dos Disfarces'
WHERE
    cod_cliente = 24;


/* =========================================================
   EXCLUSÃO DE DADOS (DELETE)
   ========================================================= */

/* 
Remove o cliente cujo código é 15.
ATENÇÃO: essa operação exclui definitivamente o registro
*/
DELETE FROM "Cliente"
WHERE cod_cliente = 15;


/* =========================================================
   CONSULTAS COM JOIN (RELACIONAMENTO ENTRE TABELAS)
   ========================================================= */

/* 
Consulta os aluguéis realizando junção (INNER JOIN) entre:
- Aluguel
- Cliente
- Traje

Ordena pelo campo data_aluguel (do mais antigo para o mais recente)
Retorna apenas o primeiro registro (aluguel mais antigo)
*/
SELECT * FROM "Aluguel"
INNER JOIN "Cliente"
    ON "Aluguel".cod_cliente = "Cliente".cod_cliente
INNER JOIN "Traje"
    ON "Aluguel".cod_traje = "Traje".cod_traje
ORDER BY data_aluguel ASC
LIMIT 1;


/* 
Consulta os aluguéis filtrando apenas:
- Trajes do tipo 'Formal'
- Trajes de tamanho 'M'
*/
SELECT * FROM "Aluguel"
INNER JOIN "Cliente"
    ON "Aluguel".cod_cliente = "Cliente".cod_cliente
INNER JOIN "Traje"
    ON "Aluguel".cod_traje = "Traje".cod_traje
WHERE tipo = 'Formal'
  AND tamanho = 'M';


/* =========================================================
   CONSULTAS COM FILTROS (WHERE)
   ========================================================= */

/* 
Busca clientes cujo nome contenha a palavra 'José'
O operador LIKE com % permite correspondência parcial
*/
SELECT * FROM "Cliente"
WHERE cli_nome LIKE '%José%';


/* 
Busca clientes cujo nome esteja exatamente
dentro da lista informada
*/
SELECT * FROM "Cliente"
WHERE cli_nome IN ('José Clayton', 'Gabriela Rocha');


/* 
Busca clientes cujo código esteja
entre 5 e 20 (inclusive)
*/
SELECT * FROM "Cliente"
WHERE cod_cliente BETWEEN 5 AND 20;
