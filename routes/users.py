from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db
from models.user import User


users = Blueprint(
    "users",
    __name__
)



@users.get("/me")
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })


@users.put("/me")
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data=request.json

    if "name" in data:
        user.name=data["name"]
    if "email" in data:
        user.email=data["email"]
    db.session.commit()

    return {
        "message":"updated"
    }