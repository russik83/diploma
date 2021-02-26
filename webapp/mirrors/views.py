from flask import abort, Blueprint, render_template

from webapp.db import db
from webapp.mirrors.models import Mirror

blueprint = Blueprint('mirrors', __name__)


@blueprint.route("/mirrors")
def index():
    title = "ЗЕРКАЛА"
    mirrors = Mirror.query.order_by(Mirror.name.asc())
    return render_template('mirrors/index.html', page_title=title, mirrors=mirrors, title=title)


@blueprint.route('/mirrors_table/<int:mirrors_table_id>')
def single_mirrors_table(mirrors_table_id):
    my_mirrors_table = Mirror.query.filter(Mirror.id == mirrors_table_id).first()

    if not my_mirrors_table:
        abort(404)

    return render_template('single_mirrors_table.html', mirror=my_mirrors_table, page_title=my_mirrors_table.name)
