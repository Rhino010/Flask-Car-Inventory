from flask import Blueprint, jsonify, render_template, request
from helpers import token_required
from models import db, Cars, car_schema


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'hello':'world'}

@api.route('/car_info', methods = ['POST'])
@token_required
def add_vehicle(current_user_token):
    id = request.json['id']
    make = request.json['make']
    car_model = request.json['car_model']
    year = request.json['year']
    stock_quantity = request.json['stock_quantity']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    cars = Cars(id, make, car_model, year, stock_quantity, user_token = user_token)

    db.session.add(cars)
    db.session.commit()

    response = car_schema.dump(cars)
    return jsonify(response)

@api.route('/car_info', methods = ['GET'])
@token_required
def get_car_info(current_user_token):
    a_user = current_user_token.token
    cars = Cars.query.filter_by(user_token = a_user).all()
    response = car_schema.dump(cars)
    return jsonify(response)

@api.route('/car_info/<id>', methods = ['GET'])
@token_required
def pull_single_vehicle(current_user_token, id):
    car = Cars.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)


@api.route('/car_info/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    car = Cars.query.get(id)
    car.make = request.json['make']
    car.car_model = request.json['car_model']
    car.year = request.json['year']
    car.stock_quantity = request.json['stock_quantity']

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('car_info/<id>',methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Cars.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)




