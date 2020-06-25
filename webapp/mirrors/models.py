from webapp.db import db


class Mirror(db.Model):
    __tablename__ = 'mirrors_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_src = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    mirror = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    fasteners = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Mirror {} {}>'.format(self.name, self.description)
