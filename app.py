from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, jwt

from routes.auth import auth
from routes.accounts import accounts
from routes.transactions import transactions
from routes.savings import savings
from routes.users import users


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)




    app.register_blueprint(users, url_prefix="/api/users")
    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(accounts, url_prefix="/api/accounts")
    app.register_blueprint(transactions, url_prefix="/api/transactions")
    app.register_blueprint(savings, url_prefix="/api/savings")



    with app.app_context():
        db.create_all()


    return app



if __name__=="__main__":

    create_app().run(debug=True)