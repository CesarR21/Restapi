SECRET_KEY = 'django-insecure-59=)k_0j4q59-1c3-kp72wv$f_(wpx)w8pw^axp-bs_e)xsq)p'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'myproject_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
