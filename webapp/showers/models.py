from webapp.db import db


class Shower(db.Model):
    __tablename__ = 'showers_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_src = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    colour = db.Column(db.String, nullable=False)
    material = db.Column(db.String, nullable=False)
    dimensions = db.Column(db.String, nullable=False)
    thickness = db.Column(db.String, nullable=False)
    hardware = db.Column(db.String, nullable=False)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Shower {} {}>'.format(self.name, self.description)
