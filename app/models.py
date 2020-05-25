from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('Not possible to access password.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User: {self.username}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


association_table = db.Table('association', db.metadata,
    db.Column('products_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('sellers_id', db.Integer, db.ForeignKey('sellers.id'))
)


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(60), index=True)
    sellers_id = db.relationship('Seller', secondary=association_table)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    categories = db.relationship('Category', back_populates='products')

    def __repr__(self):
        return f'{self.product_name}'


class Seller(db.Model):

    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True)
    seller_name = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    site = db.Column(db.String(60))

    def __repr__(self):
        return f'{self.seller_name}'


class Category(db.Model):

    __table__name = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(60), index=True)
    products = db.relationship('Product', back_populates='category')

    def __repr__(self):
        return f'{self.category_name}'
