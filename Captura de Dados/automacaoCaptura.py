import psutil
import time
from socket import gethostname
import platform
import mysql.connector

#Conexão com o banco
mydb = mysql.connector.connect(
    user='root', 
    password='43589543Lu', 
    host='localhost',
    #user = '',
    #password='',
    #host='localhost',
    database='vaultwise',
    port='3306'
)

nomeMaquina = gethostname()
sistemaOperacional = platform.system()
intervalo = 2 #setando o intervalo da captura

cursor = mydb.cursor()

while True:
    #Variáveis de captura dos dados
    
    porcent_cpu = psutil.cpu_percent()
    memoria = psutil.virtual_memory()
    freq_cpu = psutil.cpu_freq().current

    if(sistemaOperacional == "Windows"):
        disco = psutil.disk_usage('C:\\')
    else:
        disco = psutil.disk_usage('/')
    

    print(""" 
    DADOS ARMAZENADOS
          
    (Intervalo de {:d} s)
          
    CPU:      
    Porcentagem de uso da CPU: {:.2f}%
    Freq CPU: {:f}
    
    Memória (total = {:.2f} GB):
    Porcentagem de uso memória RAM: {:.1f}
    Memoria Usada: {:f} GB
          
    Disco Rígido (total = {:.2f} GB): 
    Porcentagem de uso do disco: {:.1f}%
    Disco usado: {:f} 
          
    Pressione Ctrl+C para encerrar a captura
    """.format(intervalo, porcent_cpu, freq_cpu,  memoria.total/pow(10, 9), memoria.used, memoria.percent, disco.total/pow(10, 9), disco.percent, disco.used))

    #Tempo de captura de dados
    time.sleep(intervalo)

    #Select para verificação da inserção do equipamento
    instrucaoVerEquipamento = "SELECT * FROM equipamento WHERE nome_equipamento = %s" 
    cursor.execute(instrucaoVerEquipamento, ([nomeMaquina]))

    #Função para utilizar o resultado do cursor, se não da erro de unread result
    for row in cursor:  
        print(row)

    #Função para verificar (apartir do select de cima) se já existe um equipamento com esse nome para fazer inserção automática dele
    if cursor.rowcount < 1: 
        instrucaoEquipamento= "INSERT INTO equipamento VALUES (default, %s, %s, '%s GB', '%s GB', null);"
        valuesEquipamento = (nomeMaquina, sistemaOperacional,round(disco.total/pow(10, 9), 0), round(memoria.total/pow(10, 9),0))
        cursor.execute(instrucaoEquipamento, valuesEquipamento) 
        mydb.commit()

    instrucaoID = "SELECT id_equipamento FROM equipamento WHERE nome_equipamento LIKE %s"
    valuesID = ([nomeMaquina])
    cursor.execute(instrucaoID, valuesID)
    idEquipamento_tupla = cursor.fetchone()

    #Seleção do id selecionado
    idEquipamento = idEquipamento_tupla[0]

    #Função para enviar os dados capturados com a informação de que estão em alerta
    if porcent_cpu > 80 or memoria.percent > 80:  
        instrucao = "INSERT INTO dado VALUES (default, %s, %s, %s, %s, %s, %s, 'Alerta', default, %s, 1);"
        values = (freq_cpu, porcent_cpu,memoria.used, memoria.percent, disco.used, disco.percent, idEquipamento)
        cursor.execute(instrucao, values)
    else:
        instrucao = "INSERT INTO dado VALUES (default, %s, %s, %s, %s, %s, %s, 'Seguro', default, %s, 1);"
        values = (freq_cpu, porcent_cpu,memoria.used, memoria.percent, disco.used, disco.percent, idEquipamento)
        cursor.execute(instrucao, values)

    mydb.commit()

cursor.close()
mydb.close()
