import os


BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


class Config:


    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(
            BASE_DIR,
            "database",
            "mobile_banking.db"
        )
    )


    SQLALCHEMY_TRACK_MODIFICATIONS=False


    JWT_SECRET_KEY="a9f83jd72ksh29dk39slx92kdk39sld82jdksl30"