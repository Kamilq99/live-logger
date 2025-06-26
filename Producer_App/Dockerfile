FROM python:3.14.0b3-alpine3.21

WORKDIR /Producer_App

COPY . .

RUN pip install flask

RUN pip install kafka-python

EXPOSE 5000

CMD ["python", "app.py"]