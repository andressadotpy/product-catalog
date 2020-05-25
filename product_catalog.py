import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Product, Seller, Category


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Product=Product, Seller=Seller, Category=Category)

if __name__ == '__main__':
    test()
