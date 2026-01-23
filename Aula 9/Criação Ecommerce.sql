CREATE TABLE "Cliente"(
cli_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cli_nome varchar(255) NOT NULL
);

CREATE TABLE "Categoria"(
cat_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cat_nome varchar(255) NOT NULL
);

CREATE TABLE "Produto"(
prod_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
prod_nome varchar(255) NOT NULL,
prod_preco NUMERIC(6,2) NOT NULL DEFAULT 0,
prod_estoque int NOT NULL DEFAULT 0,
id_cat int NOT NULL,
CONSTRAINT fk_prod_cat FOREIGN KEY (id_cat) REFERENCES "Categoria"(cat_id)
);

CREATE TABLE "Pedido"(
ped_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
id_cli int,
ped_data DATE NOT NULL DEFAULT CURRENT_DATE,
CONSTRAINT fk_ped_cli FOREIGN KEY (id_cli) REFERENCES "Cliente"(cli_id)
);

CREATE TABLE "Item Pedido"(
item_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
id_ped int NOT NULL,
id_prod int NOT NULL,
item_qtd int NOT NULL DEFAULT 0,
item_preco NUMERIC(6,2) NOT NULL DEFAULT 0,
CONSTRAINT fk_item_ped FOREIGN KEY (id_ped) REFERENCES "Pedido"(ped_id),
CONSTRAINT fk_item_prod FOREIGN KEY (id_prod) REFERENCES "Produto"(prod_id)
);