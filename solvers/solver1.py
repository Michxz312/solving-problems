from flask import Blueprint, render_template, request
import pulp

bp = Blueprint('solver1', __name__, url_prefix='/optimization/solver1')

@bp.route("/", methods=["GET", "POST"])
def solver_page():
    result = None
    if request.method == "POST":
        # Parse input, create PuLP problem, solve
        x = pulp.LpVariable("x", lowBound=0)
        prob = pulp.LpProblem("Example", pulp.LpMaximize)
        prob += x
        prob.solve()
        result = pulp.value(prob.objective)
    return render_template("../templates/optimization/linearProgramming.html", result=result)
