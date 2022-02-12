from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def greet():
    return ("hello Rehan! How are you!")

app.run(debug=True)