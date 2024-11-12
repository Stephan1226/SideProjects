from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def parking_lot():
    return render_template('index.html', title="Home")
