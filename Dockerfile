# SELAMUN ALEYKUM
FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./fire_Ball.py" ]
