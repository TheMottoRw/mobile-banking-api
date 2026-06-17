from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required,get_jwt_identity

from extensions import db
from models.account import Account
from models.transaction import Transaction
from routes.transactions import transactions

accounts=Blueprint(
"accounts",
__name__
)


@accounts.get("")
@jwt_required()
def get_account():
    user_id=get_jwt_identity()
    account=Account.query.filter_by(
        user_id=user_id
    ).first()

    return jsonify({
        "balance":account.balance
    })



@accounts.post("/deposit")
@jwt_required()
def deposit():
    user=get_jwt_identity()
    data=request.json
    amount=float(
        data["amount"]
    )
    account=Account.query.filter_by(
        user_id=user
    ).first()

    account.balance += amount

    transaction=Transaction(

        user_id=user,

        type="income",

        category="deposit",

        amount=amount,

        description="Account deposit"
    )


    db.session.add(transaction)

    db.session.commit()



    return {
        "message":"deposited",
        "balance":account.balance
    }


@accounts.post("/withdraw")
@jwt_required()
def withdraw():
    user=get_jwt_identity()
    data=request.json
    amount=float(
        data["amount"]
    )
    account=Account.query.filter_by(
        user_id=user
    ).first()

    if account.balance < amount:
        return {
            "message":"Insufficient balance"
        },400

    account.balance -= amount
    transaction=Transaction(
        user_id=user,
        type="expense",
        category="withdraw",
        amount=amount,
        description="Cash withdrawal"
    )
    db.session.add(transaction)
    db.session.commit()

    return {
        "message":"withdrawn",
        "balance":account.balance
    }

@accounts.post("/transfer")
@jwt_required()
def transfer():
    sender=get_jwt_identity()
    data=request.json
    receiver=data["receiver_id"]
    amount=float(
        data["amount"]
    )

    sender_account=Account.query.filter_by(
        user_id=sender
    ).first()

    receiver_account=Account.query.filter_by(
        user_id=receiver
    ).first()
    if not receiver_account:
        return {
            "message":"Invalid receiver"
        },400

    if sender_account.balance < amount:
        return {
        "message":"Not enough money"
        },400

    sender_account.balance -= amount
    receiver_account.balance += amount

    tx1=Transaction(
        user_id=sender,
        type="expense",
        category="transfer",
        amount=amount,
        description=f"Sent to {receiver}"
    )

    tx2=Transaction(
        user_id=receiver,
        type="income",
        category="transfer",
        amount=amount,
        description=f"Received from {sender}"
    )

    db.session.add_all(
        [tx1,tx2]
    )
    db.session.commit()
    return {
        "message":"transfer completed"
    }

@transactions.get("/<int:id>")
@jwt_required()
def get_transaction(id):
    user=get_jwt_identity()
    transaction=Transaction.query.filter_by(
        id=id,
        user_id=user
    ).first()

    if not transaction:
        return {
        "error":"Not found"
        },404

    return {
        "id":transaction.id,
        "type":transaction.type,
        "category":transaction.category,
        "amount":transaction.amount,
        "description":transaction.description
    }

@transactions.delete("/<int:id>")
@jwt_required()
def delete_transaction(id):
    user=get_jwt_identity()
    tx=Transaction.query.filter_by(
        id=id,
        user_id=user
    ).first()

    if not tx:
        return {
        "error":"Not found"
        },404

    db.session.delete(tx)
    db.session.commit()
    return {
        "message":"deleted"
    }