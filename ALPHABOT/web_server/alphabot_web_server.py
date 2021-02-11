from flask import Flask, render_template, url_for, request, redirect
import time, alphabot
import time
app = Flask(__name__)
bot = alphabot.AlphaBot()
bot.stop()
    
@app.route("/", methods=['POST']) #http://127.0.0.1:5000/
def index():
    if (request.method == 'POST'):
        value = 100
        if request.form['btn'] == 'avanti':
            bot.forward()
            time.sleep(value)
            bot.stop()
        elif request.form['btn'] == 'destra':
            bot.right()
            time.sleep(value)
            bot.stop()
        elif request.form['btn'] == 'indietro':
            bot.backward()
            time.sleep(value)
            bot.stop()
        elif request.form['btn'] == 'sinistra':
            bot.left()
            time.sleep(value)
            bot.stop()
    return render_template("webpage_alphabot.html")

def main():
    app.run(host="127.0.0.1", debug=True)

if __name__=="__main__":
    main()
