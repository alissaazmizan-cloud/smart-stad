from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login')
def login():
    return "Login page coming soon"

@app.route('/signup')
def signup():
    return "Signup page coming soon"

if __name__ == '__main__':
    app.run(debug=True)