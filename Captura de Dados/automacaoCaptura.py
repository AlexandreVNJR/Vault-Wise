import psutil
import time
from socket import gethostname

nomeMaquina = gethostname()

intervalo = 2 #setando o intervalo da captura

import mysql.connector

mydb = mysql.connector.connect(
    #user='VaultWise', 
    #password='Senha123', 
    #host='10.18.32.222',
    user = '',
    password='',
    host='localhost',
    database='vaultwise',
    port='3306'
)

cursor = mydb.cursor()

while True:
    porcent_cpu = psutil.cpu_percent()
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage('/')

    print(""" 
    DADOS ARMAZENADOS
          
    (Intervalo de {:d} s)
          
    CPU:      
    Porcentagem de uso da CPU: {:.2f}%
    
    Memória (total = {:.2f} GB):
    Porcentagem de uso memória RAM: {:.1f}
          
    Disco Rígido (total = {:.2f} GB): 
    Porcentagem de uso do disco: {:.1f}%
    """.format(intervalo, porcent_cpu,  memoria.total/pow(10, 9), memoria.percent, disco.total/pow(10, 9), disco.percent))
    time.sleep(intervalo)

    instrucaoVerEquipamento = "SELECT * FROM equipamento WHERE nome_equipamento = %s" 
    cursor.execute(instrucaoVerEquipamento, ([nomeMaquina]))

    for row in cursor: #Função para utilizar o resultado do cursor, se não da erro de unread result 
        print(row)

    if(cursor.rowcount < 1): #Função para verificar (apartir do select de cima) se já existe um equipamento com esse nome para fazer inserção automática dele
        instrucaoEquipamento= "INSERT INTO equipamento VALUES (default, %s, 'Windows', '%sGB', '%sGB', 1);"
        valuesEquipamento = (nomeMaquina, round(disco.total/pow(10, 9), 0), round(memoria.total/pow(10, 9),0))
        cursor.execute(instrucaoEquipamento, valuesEquipamento) 
        mydb.commit()

    if(porcent_cpu > 80 or memoria.percent > 70 ): #Função para enviar os dados capturados direto para uma tabela de alerta 
        instrucao = "INSERT INTO alerta VALUES (default, %s, %s, %s, default, 1, 1);"
        values = (porcent_cpu, memoria.percent, disco.percent)
        cursor.execute(instrucao, values)

    instrucao = "INSERT INTO dado VALUES (default, %s, %s, %s, default, 1, 1);"
    values = (porcent_cpu, memoria.percent, disco.percent)

    cursor.execute(instrucao, values)

    mydb.commit()

cursor.close()
mydb.close()