from flask import abort, Blueprint, render_template

from webapp.db import db
from webapp.doors.models import Category, Door

blueprint = Blueprint('doors', __name__)


@blueprint.route("/")
def index():
    title = "Мир дверей"
    heading = "Межкомнатные стеклянные двери"
    categories = Category.query.order_by(Category.name.asc())
    print(Category, Door)
    return render_template('doors/index.html', page_title=title, heading=heading, categories=categories)


@blueprint.route('/doors_table/<int:doors_table_id>')
def single_doors_table(doors_table_id):
    my_doors_table = Door.query.filter(Door.id == doors_table_id).first()

    if not my_doors_table:
        abort(404)

    return render_template('single_doors_table.html', door=my_doors_table, page_title=my_doors_table.name)
