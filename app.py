from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("Nav/index.html")

@app.route('/methods')
def methods_route():
    return render_template("Nav/methods.html")

@app.route('/aboutUs')
def about_us_route():
    return render_template("Nav/about_us.html")

@app.route('/help')
def help_route():
    return render_template("Nav/help.html")

if __name__ == "__main__":
    app.run(debug=True)