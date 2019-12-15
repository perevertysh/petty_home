release: python manage.py migrate
release: python manage.py collectstatic
web: gunicorn -b 127.0.0.1:$PORT pettyhome.wsgi