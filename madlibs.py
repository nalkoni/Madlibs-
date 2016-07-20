from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)



AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return render_template("home.html")


@app.route('/home')
def decision():
    """Ask user if they would like to playgame or recieve a compliment"""
    
    answer = request.args.get("playgame_compliment")

    if answer == "yes_to_game":

        return render_template("game.html")
    else: 
        return render_template("compliment.html")

@app.route('/hello')
def say_hello():
    """Save hello to user."""

    html =  render_template("hello.html")
    print html
    print type(html)
    return html


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Madlib input"""

    response = request.args.get("playgame")
    if response == "yes":
        return render_template("game.html")
    else: 
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Show madlib response"""
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html",
                            person=person, 
                            color=color,
                             noun=noun,
                             adjective=adjective) 
        

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
