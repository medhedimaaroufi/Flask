from flask import Flask, redirect, url_for,render_template,request, session
from datetime import timedelta

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key='hello'
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        name=request.form['name']
        password = request.form['password']
        session.permanent = True
        session['usr']=name
        return redirect(url_for('dashboard'))
    else:
        if 'usr' in session:
            return redirect(url_for('dashboard'))
        return render_template('login.html')
    
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html",user=session['usr'])
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

