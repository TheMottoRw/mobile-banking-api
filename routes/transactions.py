from flask import Blueprint,request

from extensions import db

from models.transaction import Transaction

from flask_jwt_extended import (
jwt_required,
get_jwt_identity
)



transactions=Blueprint(
"transactions",
__name__
)



@transactions.post("")
@jwt_required()
def create():
    user=get_jwt_identity()
    data=request.json

    if data["type"] not in [
        "income",
        "expense"
    ]:

        return {
        "error":"wrong type"
        },400
    transaction=Transaction(

        user_id=user,

        type=data["type"],

        category=data["category"],

        amount=data["amount"],

        description=data.get(
        "description"
        )
    )

    db.session.add(transaction)
    db.session.commit()

    return {
        "message":"saved"
    }



@transactions.get("")
@jwt_required()
def list_transactions():
    user=get_jwt_identity()
    result=Transaction.query.filter_by(
        user_id=user
    ).all()

    return [

    {
    "id":x.id,
    "category":x.category,
    "amount":x.amount,
    "type":x.type
    }

    for x in result

    ]
