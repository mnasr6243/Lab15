from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# Creates the Flask app and set up Bootstrap.
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2: Shows classmates' acronyms on the home page.
@app.route("/")
def home():
    return """
    <p>Task 2: Favorite Acronyms</p>
    <p>Ka'lyn R.: ASAP (As Soon As Possible)</p>
    <p>Rigoberto R.: WYA? (Where You At?)</p>
    <p>Ivan M.: LMK (Let Me Know)</p>
    """

# Tasks 3 and 4: Shows my acronym and an image.
@app.route("/Mohamed")
def templates():
    return render_template(
        "template.html",
        acronym="AFK",
        meaning="Away From Keyboard"
    )