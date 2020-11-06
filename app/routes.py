from app import app
from flask import render_template, flash, redirect, url_for, session
from app.forms import searchForm, categoryForm
from app.news import News

@app.route("/", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
def index():
    form1 = searchForm()
    form2 = categoryForm() 
    for choice in form2.category_form.choices:
        print(choice)
    if form1.validate_on_submit() and form2.validate_on_submit():
        session["q"] = form1.search_term.data
        session["category"] = form2.category_form.data
        return redirect(url_for("results"))
    else:
        print(form2.errors)
    return render_template("index.html", form1=form1, form2=form2)

@app.route("/results")  
def results():
    q = session.get("q", None)
    category = session.get("category", None)
    print(category)
    searcher = News()
    results = searcher.search(q, category)
    return render_template("results.html", q=q, results=results)
