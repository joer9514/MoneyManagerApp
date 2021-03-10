# Create MySQL database connection
mysql = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moneydb',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}

# Create PostgreSQL database connection
postgresql = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moneydb',
        'USER': 'M&M',
        'PASSWORD': 'moneymanager',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
