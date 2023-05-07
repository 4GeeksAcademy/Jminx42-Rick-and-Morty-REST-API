from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # has_favorite = db.Column(db.Boolean, unique=False)
    favorite = db.relationship("Favorite", backref="user")

    def __repr__(self):
        return f"<User {self.username}>"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    dimension = db.Column(db.String(120), nullable=False)
    favorite = db.relationship("Favorite", backref="location")

    def __repr__(self):
        return f"<Location {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    status = db.Column(db.String(120), nullable=False)
    species = db.Column(db.String(120), nullable=False)
    favorite = db.relationship("Favorite", backref="character")

    def __repr__(self):
        return f"<Character {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
        }


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    air_date = db.Column(db.String(20), nullable=False)
    episode = db.Column(db.String(120), nullable=False)
    favorite = db.relationship("Favorite", backref="episode")

    def __repr__(self):
        return f"<Episode {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode,
        }


class Category(enum.Enum):
    character = "character"
    episode = "episode"
    location = "location"


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # category = db.Column(db.Enum(Category), server_default="character")
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=True)
    episode_id = db.Column(db.Integer, db.ForeignKey("episode.id"), nullable=True)
