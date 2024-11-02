from base import db
from datetime import datetime


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class Uploads(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    about = db.Column(db.String(50), nullable=False)
    date_uploaded = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Uploads('{self.id}', '{self.name}', 'author={self.author.username}')"
