import os
from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)

if __name__ == '__main__':
    test()
