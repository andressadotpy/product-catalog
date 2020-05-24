from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(db.Model):
    pass
