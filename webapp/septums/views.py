from flask import abort, Blueprint, render_template

from webapp.db import db
from webapp.septums.models import Septum

blueprint = Blueprint('septums', __name__)


@blueprint.route("/septums")
def index():
    title = "СТЕКЛЯННЫЕ КОНСТРУКЦИИ НА ЗАКАЗ"
    septums = Septum.query.order_by(Septum.name.asc())
    return render_template('septums/index.html', page_title=title, title=title, septums=septums)


@blueprint.route('/septums_table/<int:septums_table_id>')
def single_septums_table(septums_table_id):
    my_septums_table = Septum.query.filter(Septum.id == septums_table_id).first()

    if not my_septums_table:
        abort(404)

    return render_template('single_septums_table.html', septum=my_septums_table, page_title=my_septums_table.name)
