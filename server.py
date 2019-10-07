from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "yo momma"
@app.route('/')
def index():
    if 'answer' in session:
        print(session['answer'])
        return render_template("index.html")
    else:
        session['answer'] = random.randint(1, 100)
        session['username'] = ""
        print(session['answer'])
        return render_template("index.html")
@app.route('/answer', methods = ["POST"])
def answer():
    guess = request.form['guess']
    session['userguess'] = int(guess)
    return redirect('/')
@app.route('/startover', methods = ["POST"])
def startover():
    session.clear()
    session['userguess'] = ""
    return redirect('/')
        




if __name__=="__main__":
    app.run(debug=True)
