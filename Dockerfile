FROM python:3.9

ENV REACT_APP_BASE_URL=https://pre-python-starter.herokuapp.com/
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=true

WORKDIR /var/www
COPY . .
COPY /react-app/build/* app/static/
RUN pip install -r requirements.txt && pip install psycopg2

CMD gunicorn app:app 