"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

MADLIB_TEMPLATES = ["madlib.html", "madlib2.html"]

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS,4)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game', methods=['GET'])
def show_madlib_form():
	"""Play the madlibs game"""
	user_response = request.args.get("playgame")

	if user_response == "no":
		return render_template("goodbye.html")
	else:
		return render_template("game.html")


@app.route('/madlib', methods=['GET','POST'])
def show_madlib():
	"""Show the madlib result"""

	# print(request.form.getlist('favfood'))

	data = {
		"person": request.form.get("person"),
		"color": request.form.get("color"),
		"noun": request.form.get("noun"),
		"adjective": request.form.get("adjective"),
		"favfood" : request.form.getlist('favfood') #list of fav foods
	}

	madlib_template = choice(MADLIB_TEMPLATES)
	print(madlib_template)
	return render_template(madlib_template, data=data)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
