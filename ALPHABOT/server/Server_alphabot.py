"""
Server per Comandare l'Alphabot
"""

import socket
import sqlite3
import threading
import logging

my_ip = '127.0.0.1'
porta = 2512

#setto il livello di logging a debug, il più basso. In questo modo riuscirò a stampare tutti i log più in alto
logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger()


class ClientThread(threading.Thread):
    def __init__(self,server,connessione):
        threading.Thread.__init__(self)
        self.server=server
        self.connessione=connessione

    def run(self):
        while(True):
            #lettura dei dati inviati dall'utente
            data = self.connessione.recv(4096)  
            richiesta = data.decode()
            #comunicazione dei dati del calcolo all'utente
            logger.info(f"We received those data: {data}") 
            percorso = elabora_Richiesta(richiesta)
            invia_dati_alphabot(self.server, self.connessione, percorso)
            logger.info(f"ok, you should follow this route: {percorso}")


def crea_server():
    global my_ip
    global porta

    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((my_ip, porta))   

    #comunicazione dei dati del server all'utente
    logger.info(f"\nThe Server is online and ready to work \t {my_ip}:{porta}")

    #attesa di una connessione
    server.listen()

    return server


def connetti_alphabot(server):
    try:
        #accettazione delle eventuali connessioni
        connessione, _ = server.accept() 
    except: 
        connessione = None
        logger.error("4.1, errore nella creazione della connessione")

    return connessione 

def invia_dati_alphabot(server, connessione, data):
    try:
        data= data.encode()
        #restituisco il risultato al client
        connessione.sendall(data)
    except:
        logger.error("3.1, connessione persa")

def chiusura_server(server):
    #chiusura del socket
    server.close()
    logger.info(f"The server is closed, you can join it an other time!")

def elabora_Richiesta(richiesta):
    try:
        db = sqlite3.connect('percorsi.db')
        cursor = db.cursor()
    except:
        logger.error("4.1, database inesistente")
        return [0]
    
    try:
        inizio,fine = richiesta.split(',')
    except:
        inizio = " "
        fine = " "
        logger.error("2.1, formato messaggi errato")
    
    try:
        print(f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE "{inizio}" = s.nome AND "{fine}" = f.nome')
        cursor.execute(f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE "{inizio}" = s.nome AND "{fine}" = f.nome')
        percorso = cursor.fetchone()#altrimenti fetchall
    except:
        logger.error("4.1, errore nell'eseguizione della query")

    try:
        percorso = f"{percorso[0]}"#trasformo in stringa il percorso
    except:
        logger.error("1.1 - 1.2, percorso non trovato - start e end errati")
        percorso = 0
    
    print(f"This the route: {percorso}")
    db.close()
    return percorso

def main():
    clienti=[]
    server = crea_server()
    while(1):
        connessione = connetti_alphabot(server)
        c = ClientThread(server,connessione)
        clienti.append(c)
        c.start()

    chiusura_server(server)

if __name__ == "__main__":
    main()
