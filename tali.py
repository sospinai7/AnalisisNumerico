from flask import Blueprint, render_template, request ,  abort

history =[]

tali = Blueprint('tali', __name__,
                        template_folder='templates',
                        static_folder='static')

@tali.route('/form')
def show():
    return render_template("index.html")

@tali.route('tali/form' , methods=["POST", "GET"])
def form():
    fx = request.form.get('fx')
    a=request.form.get("a")
    b=request.form.get("b")
    history.append(f"{fx}")
    title= "graph"
    return render_template("graph/form.html", title=title, history= history, fx=fx, a=a, b=b)

@tali.route('/form' , methods=["POST", "GET"])
def form2():
    fx = request.form.get('fx')
    a=request.form.get("a")
    b=request.form.get("b")
    history.append(f"{fx}")
    title= "graph"
    return render_template("graph/form.html", title=title, history= history, fx=fx, a=a, b=b)

@tali.route('/graph' , methods=["POST", "GET"])
def graph():
    data = {'title':'Function Plotter'}
    return render_template('graph/graph.html', data = data)

@tali.route('tali/help')
def help_route2():
    return render_template("nav/help.html")