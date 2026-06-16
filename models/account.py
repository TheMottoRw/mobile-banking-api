from extensions import db


class Account(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )


    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    account_no=db.Column(
        db.Text,
    )


    balance=db.Column(
        db.Float,
        default=0
    )