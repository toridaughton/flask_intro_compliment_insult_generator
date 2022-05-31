"""Greeting Flask app."""

from random import choice

from flask import Flask, render_template, request
from pkg_resources import parse_version

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'rancid', 'vacant' 'boneheaded', 'childish' 'arrogant',
  'clay-brained', 'decrepit', 'very gullible', 'wimpy', 'spineless'
  'ignorant', 'illiterate', 'meh', 'airheaded'
]


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><h1>Hi! This is the home page.<h1><div><p>Come on in!<br><button><a href='/hello'>Open Gates</button></a></p></div></html>"


@app.route('/hello', methods=["GET"])
def say_hello():
    """Say hello and prompt for user's name."""

    awesome = AWESOMENESS

    insult = INSULTS

    return render_template("hello.html", awesomeness=awesome, insult=insult, awesome_len = len(awesome), insult_len = len(insult))


@app.route('/greet', methods=["GET", "POST"])
def greet_person():
    """Get user by name."""

    player = request.form.get("person")

    compliment = request.form.get("compliment")


    return render_template("greeting.html", player=player, compliment=compliment)


@app.route("/diss", methods=["GET", "POST"])
def diss_person():
  """Get user by name
    Then diss them formally with their inputted name :)
  """

  player = request.form.get("person")

  insult = request.form.get("insult")

  return render_template("dissmissal.html", player=player, insult=insult)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
