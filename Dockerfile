FROM python:3

RUN pip install flask

WORKDIR /code

COPY . .

RUN mkdir -p data/

CMD ["python", "./main.py"]