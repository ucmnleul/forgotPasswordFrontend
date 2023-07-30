from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, validators
from wtforms.validators import InputRequired, URL, InputRequired


class RetrieveForm(FlaskForm):
    site = StringField("Site", validators=[InputRequired(message="This field must be field."), URL(message="Invalid URL")],
                       render_kw={"class": "my_input", "placeholder": "https://website_url"})
    name = StringField("Name",
                       render_kw={"class": "my_input", "placeholder": "A name or a find key (Optional)"})

    submit = SubmitField(f"Get pass")


class CachePasswordForm(FlaskForm):
    site = StringField("Site", validators=[InputRequired(message="This field must be field."), URL(message="Invalid URL")],
                       render_kw={"class": "my_input", "placeholder": "https://the_url_of_the_website"})
    name = StringField("Name",
                       render_kw={"class": "my_input", "placeholder": "A name or a find key    (optional)"})

    password = StringField("Password", validators=[InputRequired()],
                             render_kw={"class": "my_input", "placeholder": "Type password or generate"})

    submit = SubmitField("Save")
