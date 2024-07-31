from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='interfaces', static_folder='staticFolder')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('loginPage.html')

@app.route('/signup')
def register():
    return render_template('registerPage.html')


if __name__ == "__main__":
    app.run(debug=True)
