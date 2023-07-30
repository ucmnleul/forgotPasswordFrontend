from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import CSRFProtect
from forms import RetrieveForm, CachePasswordForm
from my_utils import write_on_to_file, find_password, fake_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AHGAJL;HENSNuhans1234567890l'
csrf = CSRFProtect(app)


@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home(copy_text=None):
    return render_template("home.html")


@app.route("/retrieve", methods=["GET", "POST"])
def retrieve():
    form = RetrieveForm()
    password = None
    if form.validate_on_submit():
        site = form.site.data
        password = find_password(site)
        hashed = fake_hash(password)
        flash(f"Here's your password: {hashed}", category="primary")
    else:
        if form.site.errors:
            flash(f"{form.site.errors[0]}", "danger")
    return render_template("retrieve.html", form=form, copy_text=password)


@app.route("/cache", methods=["GET", "POST"])
def cache():
    form = CachePasswordForm()
    copy_text = None
    if form.validate_on_submit():
        password = form.password.data
        site = form.site.data
        name = form.name.data
        copy_text = password
        write_on_to_file(site, password, name)
        flash(f"Saved Successfully!", category="primary")
        return render_template("home.html", copy_text=copy_text)
    else:
        if form.site.errors:
            flash(f"{form.site.errors[0]}", "danger")
        print("errors")
    return render_template("cache.html", form=form, copy_text=copy_text)



if __name__ == "__main__":
    app.run(debug=True)
