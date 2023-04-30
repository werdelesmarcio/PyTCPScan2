#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PyTCPScan Version 2.1 (Alfa)

# Relação de todos os Imports necessários para a execução do software
import socket
import sys
from datetime import datetime
import os
import time

from utils.banner import banner

# Caminho das pastas onde estão arquivos importantes
pathfile = './utils/'
if pathfile not in sys.path:
	sys.path.append(pathfile)

# Aguarda um tempo, após isso limpa a tela e chama o banner do programa
time.sleep(8)
os.system('cls' if os.name == 'nt' else 'clear')
banner()

"""
A aplicação precisa que seja informado os parâmetros
alvo, porta inicial e porta final.
Quando não for informado nenhum parametro ela emite
a mensagem de erro abaixo.
"""
if len(sys.argv) != 4:
	print('')
	print(' [!] ERROR: Missing input arguments.')
	print(' [!] Usage: ./pyTCPScan.py [target] [initial_port] [final_port]\n')
	sys.exit(1)

# Variáveis
target = str(sys.argv[1])
host = socket.gethostbyname(target)
ip = int(sys.argv[2])
fp = int(sys.argv[3])

# Criando o socket de conexão para testar as portas
def connect(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
	
 # Testa a conexão 
    try:
        s.connect((target, port))
        return(1)
    except:
        return(2)

# Iniciando o scan
print (' [*] Connecting to Target: %s\n [*] Scanning ports between %s and %s ...' % (target, ip, fp))
print ('')
print (' [!] Please wait, scanning remote host', host)
print (' [*] This may take a while, be patient.')
print ('')

# Checando a hora que iniciou o Scan
t1 = datetime.now()

# Laço que testa as portas no range
try:
    for port in range(ip, fp+1):
        e = connect(target, port)
        if e == 1:
            print (' [+] POSITIVE TO Port {}:	Status: OPEN'.format(port))
	    
# Se control+c for pressionado encerra a aplicação
except KeyboardInterrupt:
    print('')
    print(' You pressed Ctrl+C')
    print(' The application has been stopped prematurely.')
    sys.exit()

# Se o Host não pôde ser resolvido	
except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

# Se foi impossível conectar com o alvo	
except socket.error:
	print ('Could not connect to target')
	sys.exit()
	
# Checa o termino do scan
t2 = datetime.now()

tempoTotal = t2 - t1

print ('-' * 50)
print
print (' [!] Scanning Completed in: ', tempoTotal)  # Banner indicando o tempo de scan
print
print ('-' * 50)
 
print('\n ---Finished---\n')