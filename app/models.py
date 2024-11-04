from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))


class BlogSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Blog

    id = ma.auto_field()
    title = ma.auto_field()
    content = ma.auto_field()
    author = ma.auto_field()
    image_url = ma.auto_field()
