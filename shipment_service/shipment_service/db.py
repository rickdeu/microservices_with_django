import os


from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
HOST = '127.0.0.1'

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rating_score',
        'USER': 'postgres',
        'PASSWORD': '123tau123',
        'HOST': '127.0.0.1',
        'PORT': '5433'
    }
}"""

   
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shipmentservice',
        'USER': 'rickdeu',
        'PASSWORD': 'rickdeudeu', 
        'HOST': 'localhost',
        'PORT': '3303'
    }
}


SQLSERVER = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'rating_score',
        'HOST': '127.0.0.1',
        'PORT': 1433,
        'USER': 'sa',
        'PASSWORD': '123tau123',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


MONGODB = {
      'default': {
        'ENGINE': 'djongo',
        'NAME': 'WCI2',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
           'host': '127.0.0.1',
        }
    }
}