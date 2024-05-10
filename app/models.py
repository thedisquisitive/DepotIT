
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login

class User(UserMixin, db.Model):
    id: so.Mapped[int] = db.Column(db.Integer, primary_key=True)
    username: so.Mapped[str] = db.Column(db.String(64), index=True, unique=True)
    firstName: so.Mapped[str] = db.Column(db.String(64))
    lastName: so.Mapped[str] = db.Column(db.String(64))
    email: so.Mapped[str] = db.Column(db.String(120), index=True, unique=True)
    phone: so.Mapped[str] = db.Column(db.String(20))

    password_hash: so.Mapped[Optional[str]] = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Item(db.Model):
    id: so.Mapped[int] = db.Column(db.Integer, primary_key=True)
    sku: so.Mapped[str] = db.Column(db.String(64), index=True, unique=True)
    name: so.Mapped[str] = db.Column(db.String(255))
    description: so.Mapped[str] = db.Column(db.String(255))
    cost: so.Mapped[float] = db.Column(db.Float)
    price: so.Mapped[float] = db.Column(db.Float)
    quantityInStock: so.Mapped[int] = db.Column(db.Integer)
    quantityOnOrder: so.Mapped[int] = db.Column(db.Integer)
    quantityReserved: so.Mapped[int] = db.Column(db.Integer)
    quantityInTruck: so.Mapped[int] = db.Column(db.Integer)
    manufacturer: so.Mapped[str] = db.Column(db.String(255))
    category: so.Mapped[str] = db.Column(db.String(255))

    def __repr__(self):
        return '<Item {}>'.format(self.name)
    

