from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download/")
def download():
    return "thanks for downloading!"


if __name__ == "__main__":
    app.run()
