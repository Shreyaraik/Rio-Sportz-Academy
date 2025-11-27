from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Founder Page
@app.route("/founder")
def founder():
    return render_template("founder.html")

@app.route("/programs")
def programs():
    return render_template("programs.html")


@app.route("/tracker")
def kids_performance():
    return render_template("tracker.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == "__main__":
    app.run(debug=True)


