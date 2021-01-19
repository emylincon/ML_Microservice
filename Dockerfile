FROM python:3.7-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ['python', 'app.py']


