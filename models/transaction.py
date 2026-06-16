from extensions import db
from datetime import datetime



class Transaction(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )


    type=db.Column(
        db.String(20)
    )

    category=db.Column(
        db.String(50)
    )

    amount=db.Column(
        db.Float
    )

    description=db.Column(
        db.String(200)
    )

    created_at=db.Column(
        db.DateTime,
        default=datetime.utcnow
    )