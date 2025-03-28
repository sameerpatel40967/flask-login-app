from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy credentials (Database ka use kar sakte ho future me)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return "Login Successful! Welcome, " + username
    else:
        return render_template('login.html', error="Invalid Username or Password!")

if __name__ == "__main__":
    app.run(debug=True)
