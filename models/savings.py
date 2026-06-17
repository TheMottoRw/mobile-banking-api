from datetime import datetime

from extensions import db



class Savings(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    title=db.Column(
        db.String(100)
    )

    target_amount=db.Column(
        db.Float
    )

    saved_amount=db.Column(
        db.Float,
        default=0
    )

    deadline=db.Column(
        db.String(20)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.now()
    )