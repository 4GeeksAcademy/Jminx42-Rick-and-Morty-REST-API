"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Location, Character, Episode, Favorite
from api.utils import generate_sitemap, APIException

api = Blueprint("api", __name__)


@api.route("/hello", methods=["POST", "GET"])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route("/character", methods=["GET"])
def get_all_characters():
    characters = Character.query.all()

    char_serialized = [character.serialize() for character in characters]

    return jsonify({"characters": char_serialized}), 200


@api.route("/character/<int:character_id>", methods=["GET"])
def get_character_by_id(character_id):
    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error": "No character found with this id"}), 400
    return jsonify({"character": character.serialize()}), 200


@api.route("/location", methods=["GET"])
def get_all_locations():
    locations = Location.query.all()

    location_serialized = [location.serialize() for location in locations]

    return jsonify({"locations": location_serialized}), 200


@api.route("/location/<int:location_id>", methods=["GET"])
def get_location_by_id(location_id):
    location = Location.query.get(location_id)
    if not location:
        return jsonify({"error": "No location found with this id"}), 400
    return jsonify({"location": location.serialize()}), 200


@api.route("/episode", methods=["GET"])
def get_all_episodes():
    episodes = Episode.query.all()

    episode_serialized = [episode.serialize() for episode in episodes]
    print("@@@@@@@@@@@@@@@@@@@")
    print(episodes)
    print(episode_serialized)
    print("@@@@@@@@@@@@@@@@@@@")

    return jsonify({"episodes": episode_serialized}), 200


@api.route("/episode/<int:episode_id>", methods=["GET"])
def get_episode_by_id(episode_id):
    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({"error": "No episode found with this id"}), 400
    return jsonify({"episode": episode.serialize()}), 200


@api.route("/users", methods=["GET"])
def get_all_users():
    users = User.query.all()

    user_serialized = [user.serialize() for user in users]
    print("@@@@@@@@@@@@@@@@@@@")
    print(users)
    print(user_serialized)
    print("@@@@@@@@@@@@@@@@@@@")

    return jsonify({"users": user_serialized}), 200


@api.route("/users/favorites/<int:user_id>", methods=["GET"])
def get_all_user_favorites(user_id):
    user = User.query.get(user_id)

    user_serialized = [user.serialize() for user in users]
    print("@@@@@@@@@@@@@@@@@@@")
    print(users)
    print(user_serialized)
    print("@@@@@@@@@@@@@@@@@@@")

    return jsonify({"users": user_serialized}), 200
