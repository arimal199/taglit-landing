from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download/")
def download():
    return "thanks for downloading!"


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return redirect(url_for('user'))
        else:
            return redirect(url_for('admin'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()
