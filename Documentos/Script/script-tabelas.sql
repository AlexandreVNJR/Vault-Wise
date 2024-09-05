DROP DATABASE IF EXISTS vaultwise;
CREATE DATABASE vaultwise;
USE vaultwise;

CREATE TABLE empresa(
cnpj CHAR(14) PRIMARY KEY ,
cep CHAR(8),
razao_social VARCHAR(45),
telefone CHAR(9) UNIQUE,
email VARCHAR(45) UNIQUE,
senha VARCHAR(45)
);
select * from empresa;

CREATE TABLE usuario(
cpf CHAR(11),
nome VARCHAR(45),
email VARCHAR(45) UNIQUE,
telefone CHAR(9) UNIQUE,
cargo VARCHAR(45),
senha VARCHAR(45),
fk_cnpj char(14),

    FOREIGN KEY (fk_cnpj) REFERENCES empresa (cnpj),
    PRIMARY KEY (cpf,fk_cnpj)	
);



CREATE TABLE equipamento(
id_equipamento INT AUTO_INCREMENT,
nome_equipamento VARCHAR(45),
sistema_operacional VARCHAR(45),
total_disco VARCHAR(45),
total_memoria VARCHAR(45),
fk_cnpj char(14),

    FOREIGN KEY (fk_cnpj) REFERENCES empresa (cnpj),
    PRIMARY KEY (id_equipamento)
);

CREATE TABLE dado(
id_dado INT AUTO_INCREMENT,
cpu_freq VARCHAR(45),
cpu_percent VARCHAR(45),
memoria_usada VARCHAR(45),
memoria_percent VARCHAR(45),
disco_usada VARCHAR(45),
disco_percent VARCHAR(45),
estado VARCHAR(45),
dt_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
fk_equipamento INT,
fk_cnpj char(14),

    FOREIGN KEY (fk_equipamento) REFERENCES equipamento (id_equipamento),
    FOREIGN KEY (fk_cnpj) REFERENCES empresa (cnpj),
    PRIMARY KEY (id_dado, fk_equipamento, fk_cnpj)
);

INSERT INTO empresa VALUES
(default, 12345678910111, 99999999, "Empresa XPTO", 999999999, "xpto@gmail.com", "999", null);

INSERT INTO equipamento VALUES
(default, 'Teste', "Windows", "1TB", "8GB",1);

SELECT * FROM dado;
SELECT * FROM equipamento;

SELECT d.cpu_percent, d.memoria_percent, d.disco_percent, d.dt_hora,e.nome_equipamento FROM dado AS d JOIN equipamento AS e ON fk_equipamento = id_equipamento;	