"""
    VERIFICA DI TPSIT
    author = Cuniberti Andrea
    ----> server <----
"""

import socket
import sqlite3
import threading
import logging

#imposto indirizzo e porta del server
server_ip = 'localhost'
server_port = 2011


#setto il livello di logging a debug, il più basso. In questo modo riuscirò a stampare tutti i log più in alto
logging.basicConfig(level = logging.DEBUG, filename="logging_server.log", filemode="a")
logger = logging.getLogger()


#classe per la gesione del client
class ClientThread(threading.Thread):
    def __init__(self,server,connessione, battesimo):
        threading.Thread.__init__(self)
        self.server = server
        self.connessione = connessione
        self.battesimo = battesimo

    #metodo per il sevizio ai vari therad
    def run(self):
        while(True):
            richiesta = self.battesimo
            #elaboro una lista dei vari calcoli che dovrò spedire al client
            calcolo = elabora_calcolo(richiesta)

            #spedisco il calcolo ai client
            for i in calcolo:
                invia_dati_client(self.server, self.connessione, calcolo[i])
                logger.info(f"ok, you should calculate this: {calcolo[i]}")



def connetti_client(server):
    try:
        #accettazione delle eventuali connessioni
        connessione, _ = server.accept() 
    except: 
        connessione = None
        logger.error("errore nella creazione della connessione")

    return connessione 

def invia_dati_client(server, connessione, data):
    try:
        data= data.encode()
        #restituisco il risultato al client
        connessione.sendall(data)
    except:
        logger.error(" connessione persa")


def elabora_calcolo(calcolo):

    #la lista da_fare conterrà la lista dei calcoli da spedire al client con id "calcolo"
    da_fare = []

    #connetto il server al database
    try:
        db = sqlite3.connect('operations.db')
        cursor = db.cursor()
    except:
        logger.error("database inesistente")
        return [0]
        
    #eseguo la query ed immagazino il risultato nella lista da_fare
    try:
        print(f'SELECT operation FROM operations WHERE client = {calcolo}')
        da_fare = cursor.execute(f'SELECT operation FROM operations WHERE client = {calcolo}')

    except:
        logger.error("errore nell'eseguizione della query")

    #inserisco alla fine della lista, anche se vuota, la stringa "exit", in questo modo potrò scollegare il client
    da_fare.append("exit")

    #chiudo il database e spedisco alla run la lista con le operazioni
    db.close()
    return da_fare

def main():

    #creazione di una lista di client
    client=[]

    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((server_ip, server_port))   

    #comunicazione dei dati del server all'utente
    logger.info(f"\nThe Server is online and ready to work \t {server_ip}:{server_port}")

    #attesa di una connessione
    server.listen()

    #battezzo i client dando loro un tag
    battesimo = 1

    while(1):
        #connetto il client
        connessione = connetti_client(server)

        #creo un istanza della classe ClientThread, andando di conseguenza a creare un thread
        c = ClientThread(server,connessione, battesimo)

        #aggiungo il thread alla lista client
        client.append(c)

        #avvio il thread
        c.start()

        #incremento il valore del battesimo per dare il nome incrementato al prossimo thread
        battesimo += 1

if __name__ == "__main__":
    main()
