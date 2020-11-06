from app import app
from flask import render_template, flash, redirect, url_for, session, request
from app.forms import masterForm
from app.news import News

@app.route("/", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
def index():
    form = masterForm()
    if request.method == "POST" and form.validate():
        session["q"] = form.search_term.data
        session["category"] = form.category_form.data
        return redirect(url_for("results"))
    else:
        print(form.errors)
    return render_template("index.html", form=form)

@app.route("/results")  
def results():
    q = session.get("q", None)
    category = session.get("category", None).lower()
    print(category)
    searcher = News()
    results = searcher.search(q, category)
    return render_template("results.html", q=q, results=results)


