from app import app
from flask import render_template, flash, redirect
from app.forms import searchForm 

@app.route("/", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
def index():
    form = searchForm() 
    if form.validate_on_submit():
        flash("Search initiated with term {}!".format(form.search_term.data))
        return redirect("/index")
    return render_template("index.html", form=form)