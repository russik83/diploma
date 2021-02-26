from flask import render_template
from webapp.db import db
from webapp.errors import blueprint


@blueprint.app_errorhandler(404)
def not_found_error(error):
    title = "Страница не найдена"
    return render_template('404.html', page_title=title), 404


@blueprint.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
