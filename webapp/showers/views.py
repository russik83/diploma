from flask import abort, Blueprint, render_template

from webapp.db import db
from webapp.showers.models import Shower

blueprint = Blueprint('showers', __name__)


@blueprint.route("/showers")
def index():
    title = "ДУШЕВЫЕ ОГРАЖДЕНИЯ ИЗ СТЕКЛА"
    showers = Shower.query.order_by(Shower.name.asc())
    return render_template('showers/index.html', page_title=title, title=title, showers=showers)


@blueprint.route('/showers_table/<int:showers_table_id>')
def single_showers_table(showers_table_id):
    my_showers_table = Shower.query.filter(Shower.id == showers_table_id).first()

    if not my_showers_table:
        abort(404)

    return render_template('single_showers_table.html', shower=my_showers_table, page_title=my_showers_table.name)
