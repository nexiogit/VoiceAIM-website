from flask import Flask, render_template


app = Flask(__name__,template_folder='templates')


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    host = "0.0.0.0"
    port = "8080"
    debug = False
    app.run(host, port, debug)
