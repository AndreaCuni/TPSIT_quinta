from flask import Flask, request, render_template, redirect, url_for #tutte le cose da importare per fare questo server web
import sqlite3 #libreria per i db

app = Flask(__name__)
def validate(username, password):   #funzione per controllare username e psw

    conn = sqlite3.connect('db.db')
    print("db opened")
    try:
        cursor = conn.execute('SELECT * FROM Dati_utenti WHERE username = "' + username + '" AND password = "' + password + '"')
    except:
        return False
    if (len(cursor.fetchall) != 0):
        return True
    else:
        return False   
    

@app.route("/", methods=['GET', 'POST']) #http://127.0.0.1:5000/
def login(): #classe adibita allo sviluppo di richieste e risposte
    error = None
    if request.method == 'POST':    #metodo usato
        username = request.form['username'] #salva username 
        password = request.form['password'] #salva psw
        completion = validate(username, password)
        if completion == False: #controllo psw e user
            error = 'le credenziali inserite non sono valide. Tenta di nuovo sarai più fortunato'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error = error)

@app.route("/secret")  #http://127.0.0.1:5000/secret/
def index2():   #pagina di login.
    return "shhh, questa è una pagina segreta!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug="on")
