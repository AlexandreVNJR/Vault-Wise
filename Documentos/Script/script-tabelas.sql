-- DROP DATABASE IF EXISTS vaultwise;
CREATE DATABASE vaultwise;
USE vaultwise;


CREATE TABLE empresa(
id_empresa INT PRIMARY KEY AUTO_INCREMENT,
cnpj CHAR(14) UNIQUE,
cep CHAR(8),
razao_social VARCHAR(45),
telefone CHAR(9) UNIQUE,
email VARCHAR(45) UNIQUE,
numero VARCHAR(45),
complemento VARCHAR(45)
);

CREATE TABLE usuario(
id_usuario INT AUTO_INCREMENT,
cpf CHAR(11) UNIQUE,
nome VARCHAR(45),
email VARCHAR(45) UNIQUE,
telefone CHAR(9) UNIQUE,
cargo VARCHAR(45),
senha VARCHAR(45),
fk_empresa INT,

    FOREIGN KEY (fk_empresa) REFERENCES empresa (id_empresa),
    PRIMARY KEY (id_usuario,fk_empresa)
);

CREATE TABLE equipamento(
id_equipamento INT,
sistema_operacional VARCHAR(45),
fk_empresa INT,

    FOREIGN KEY (fk_empresa) REFERENCES empresa (id_empresa),
    PRIMARY KEY (id_equipamento,fk_empresa)
);

CREATE TABLE dado(
id_dado INT,
processamento VARCHAR(45),
memoria VARCHAR(45),
disco VARCHAR(45),
dt_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
fk_equipamento INT,
fk_empresa INT,

    FOREIGN KEY (fk_equipamento) REFERENCES equipamento (id_equipamento),
    FOREIGN KEY (fk_empresa) REFERENCES empresa (id_empresa),
    PRIMARY KEY (id_dado, id_equipamento, fk_empresa)
);