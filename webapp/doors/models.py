from webapp.db import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    img_src = db.Column(db.String, unique=True, nullable=True)
    door_list = db.relationship("Door", backref="door_id")

    def __repr__(self):
        return '<Category {} {}>'.format(self.name, self.description)


class Door(db.Model):
    __tablename__ = 'doors_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'))
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
        return '<Door {} {}>'.format(self.name, self.description)
