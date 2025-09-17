from flask import Flask, render_template
from solvers import solver1  # Import your modules

app = Flask(__name__)

# Static pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    # You can pass a list of projects to the template
    project_list = [
        {"title": "Solver 1", "image": "project1.png", "link": "/optimization/solver1"},
    ]
    return render_template("projects.html", projects=project_list)

# Optimization pages
app.register_blueprint(solver1.bp)

if __name__ == "__main__":
    app.run(debug=True)
