"""
Client ECHO TCP
"""
import socket

ip_server = '127.0.0.1'
porta_server = 4000

#creazione del socket TCP IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#connessione al server
client.connect((ip_server,porta_server))

while(True):
    #richiesta del messaggio
    messaggio = input("messaggio: ")

    #invio dei dati al server
    client.sendall(messaggio.encode())
    
    #controllo del comando di chiusura
    if(messaggio == "close()"):
        break

    #leggo il risultato
    risultato = client.recv(4096) 

    #comunicazione risultato all'utente
    print("risultato: " + risultato.decode())

#chiusura del socket
client.close()