from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("Nav/index.html")

@app.route('/methods')
def methods_route():
    return render_template("nav/methods.html")

if __name__ == "__main__":
    app.run(debug=True)