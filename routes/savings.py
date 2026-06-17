from flask import Blueprint,request
from extensions import db
from models.savings import Savings

from flask_jwt_extended import (
jwt_required,
get_jwt_identity
)

savings=Blueprint(
"savings",
__name__
)

@savings.post("")
@jwt_required()
def create_goal():
    user=get_jwt_identity()
    data=request.json

    goal=Savings(
        user_id=user,
        title=data["title"],
        target_amount=data["target"],
        deadline=data["deadline"],
    )
    db.session.add(goal)
    db.session.commit()

    return {
    "message":"goal created"
    }

@savings.get("")
@jwt_required()
def get_goals():
    user=get_jwt_identity()
    goals=Savings.query.filter_by(
        user_id=user
    ).all()

    return [
    {
    "id":g.id,
    "title":g.title,
    "target":g.target_amount,
    "saved":g.saved_amount,
    "deadline":g.deadline
    }

    for g in goals
    ]

@savings.put("/<int:id>")
@jwt_required()
def add_saving(id):
    user=get_jwt_identity()
    data=request.json
    goal=Savings.query.filter_by(
        id=id,
        user_id=user
    ).first()

    if not goal:
        return {
        "error":"Not found"
        },404

    goal.saved_amount += float(
        data["amount"]
    )

    db.session.commit()

    return {
    "message":"updated"
    }

@savings.delete("/<int:id>")
@jwt_required()
def delete_goal(id):
    user=get_jwt_identity()
    goal=Savings.query.filter_by(
        id=id,
        user_id=user
    ).first()

    db.session.delete(goal)
    db.session.commit()

    return {
    "message":"removed"
    }