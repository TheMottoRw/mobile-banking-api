from flask import Blueprint,request,jsonify

from extensions import db

from models.user import User
from models.account import Account

from flask_jwt_extended import create_access_token

import bcrypt

from helpers import utils

auth=Blueprint(
    "auth",
    __name__
)



@auth.post("/register")
def register():


    data=request.json


    if not data.get("email") or not data.get("password"):

        return {
            "message":"Invalid input"
        },400



    exists=User.query.filter_by(
        email=data["email"]
    ).first()


    if exists:

        return {
        "message":"Email exists"
        },400



    password=bcrypt.hashpw(
        data["password"].encode(),
        bcrypt.gensalt()
    )

    user=User(
        name=data["name"],
        email=data["email"],
        password=password.decode()
    )

    db.session.add(user)

    db.session.commit()

    account=Account(
        user_id=user.id,
        account_no= utils.generate_random_account(10),
        balance=0
    )

    db.session.add(account)

    db.session.commit()



    return {
        "message":"created"
    },201





@auth.post("/login")
def login():


    data=request.json


    user=User.query.filter_by(
        email=data["email"]
    ).first()


    if not user:

        return {"message":"Invalid"},401



    if bcrypt.checkpw(
        data["password"].encode(),
        user.password.encode()
    ):


        token=create_access_token(
            identity=user.id
        )


        return {
            "token":token
        }



    return {
        "message":"Invalid"
    },401