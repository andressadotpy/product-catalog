# Product catalog

Built with *Python 3.6.10* and *Flask 1.1.2*.



## Project definition and organization

Product catalog is a Flask application to manage *products*, *sellers* and *categories*. Each product can have many sellers, and each seller can sell many products. A product can be part of only one category, but a category groups many similar products. Only *admins* users can *create, read, update and delete* products, sellers and categories. 

```
product-catalog  
└─── app  
    |___ __init__.py
    |___ models.py
    └─── admin  
         │___ __init__.py  
         │___ forms.py  
         |___ views.py  
    |___ auth  
         |___ __init__.py
         |___ forms.py
         |___ views.py
    └─── home
    	 |___ __init__.py
    	 |___ views.py
|___ migrations  
└─── tests  
    |___ __init__.py
    |___ test_basics.py
    |___ test_models.py
|___ config.py
|___ product_catalog.py
|___ README.md
|___ requirements.txt
```

## Running the application

Activate your *virtual environment*, open the terminal in the  package root and type:

```bash
$ pip3 install -r requirements.txt
```

`product_catalog`is the application script and with

```bash
$ python3 product_catalog.py
```

command, run all unit tests for the application.

To start running the application, use some flask commands or access the `flask shell`:

```bash
$ export FLASK_APP=product_catalog:app
```

To initialize the database and handle migrations:

```bash
$ flask db init
$ flask db migrate
```

To access the `flask shell`:

```bash
$ flask shell
```

Inside the shell, we can create manually an admin User, for example:

```shell
>>> from app.models import User
>>> from app import db
>>> admin = User(username='admin', password='admin_password', is_admin=True)
>>> db.create_all()
>>> db.session.add(admin)
>>> db.session.commit()
```

I chose that only admins can handle CRUD operations. Because it's a simple application and there's just normal user and admins (not other roles for users), I made `is_admin`as an attribute with the boolean value set by default to `False`.