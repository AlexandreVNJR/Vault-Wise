package school.sptech.service.dao;

import org.springframework.jdbc.core.JdbcTemplate;
import school.sptech.Conexao;

public class DaoDado {
    public static void main(String[] args) {
        Conexao conexao = new Conexao();
        JdbcTemplate banco = conexao.getConexaoBanco();

        banco.execute("""
                CREATE TABLE IF NOT EXISTS dado(
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
                fk_empresa char(14),
                
                    FOREIGN KEY (fk_equipamento) REFERENCES equipamento (id_equipamento),
                    FOREIGN KEY (fk_empresa) REFERENCES empresa (id_empresa),
                    PRIMARY KEY (id_dado, fk_equipamento, fk_empresa)
                );
                )""");
    }
}
