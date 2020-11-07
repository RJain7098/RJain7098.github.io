from app import app
from flask import render_template, flash, redirect, url_for, session, request
from app.forms import masterForm
from app.news import News

# default images in case news site does not provide one
images = dict(technology="https://www.onlinetoolsexpert.com/wp-content/uploads/2020/08/Technology-news.jpg",
                entertainment="https://kstp.com/kstpImages/800EntertainmentNewsGfx.jpg",
                sports="https://ak.picdn.net/shutterstock/videos/29587630/thumb/3.jpg")

@app.route("/", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
def index():
    form = masterForm()
    if request.method == "POST" and form.validate():
        session["q"] = form.search_term.data
        session["category"] = form.category_form.data
        return redirect(url_for("results"))
    else:
        flash(form.errors)
    return render_template("index.html", form=form)

@app.route("/results")  
def results():
    q = session.get("q", None)
    category = session.get("category", None).lower()
    searcher = News()
    results = searcher.search(q, category)
    return render_template("results.html", q=q, category = category, results=results, default_images=images)


