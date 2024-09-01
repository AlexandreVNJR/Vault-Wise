import psutil
import time
from socket import gethostname
import platform

nomeMaquina = gethostname()
sistemaOperacional = platform.system()
intervalo = int(input("Digite o intervalo do monitoramento: \n")) #setando o intervalo da captura


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
          
    (Dados sendo capturados a cada {:f}s)
          
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
    """.format(intervalo, porcent_cpu, round(freq_cpu),  memoria.total/pow(10, 9), memoria.percent, round(memoria.used/pow(10,9)), disco.total/pow(10, 9), disco.percent, round(disco.used/pow(10,9))))

    #Tempo de captura de dados
    time.sleep(intervalo)