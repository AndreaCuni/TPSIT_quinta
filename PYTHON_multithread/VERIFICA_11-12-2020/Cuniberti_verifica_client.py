"""
    VERIFICA TPSIT
    author: Cuniberti Andrea
    ----> client <----
"""
import socket

ip_server = 'localhost'
porta_server = 2011

#creazione del socket TCP IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#connessione al server
client.connect((ip_server,porta_server))

while(True):
        
    #leggo il risultato
    
    casella_x = input("inserisci l'ascissa della casella da crocettare")
    casella_y = input("inserisci l'ordinata della casella da crocettare")

    risultato = casella_x + casella_y

    client.sendall(risultato.encode)
    
    risposta = client.recv(4096)

    risposta = risposta.decode()

    if(risposta == "errore"):
        print("si è verificato un errore nell'inserimento, per favore inserisci una nuova casella")
    else:
        



#chiusura del socket
client.close()