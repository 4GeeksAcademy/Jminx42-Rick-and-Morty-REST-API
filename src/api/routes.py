"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Pet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/pets', methods=['GET'])
def get_all_pets():

    pets = Pet.query.all()

    pets_serialized = [pet.serialize() for pet in pets]
    print("@@@@@@@@@@@@@@@@@@@")
    print(pets)
    print(pets_serialized)
    print("@@@@@@@@@@@@@@@@@@@")

    return jsonify({"pets": pets_serialized}), 200

@api.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet_by_id(pet_id):

    pet = Pet.query.get(pet_id)
    if not pet:
        return jsonify({"error": "No pet found with this id"}), 400
    return jsonify({"pet": pet.serialize()}), 200
    # if pet:
    #     return jsonify({"pet": pet.serialize()}), 200
    # else:
    #     return jsonify({"error": "No pet found with this id"}), 400

@api.route('/pet_by_name/<string:pet_name>', methods=['GET'])
def get_pet_by_name(pet_name):

    pet = Pet.query.filter_by(name = pet_name).first()

    # pet = Pet.query.filter(Pet.name == pet_name).all()

    if not pet:
        return jsonify({"error": "No pet found with this name"}), 400
    return jsonify({"pet": pet.serialize()}), 200
    
@api.route('/pet', methods=['POST'])
def create_pet():

    body = request.json
    new_pet = Pet(name= body['name'], age= body["age"], user_id = body['user_id'])
    db.session.add(new_pet)
    db.session.commit()

    return jsonify({"pet": "created"}), 200

@api.route('/pet/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):

    body = request.json
    pet = Pet.query.get(pet_id)
    if not pet:
        return jsonify({"error": "No pet found with this id"}), 400
    pet.name = body['name']
    pet.age = body['age']

    db.session.commit()

    return jsonify({"pet": "updated"}), 200

@api.route('/pet/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return jsonify({"error": "No pet found with this id"}), 400
    db.session.delete(pet)
    db.session.commit()

    return jsonify({"pet": pet.name + " was deleted"}), 200