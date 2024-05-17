FROM python:3.9

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app/backend.py /app/backend.py
COPY app/static /app/static

ENV FLASK_APP=backend.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_RUN_PORT=8080

CMD ["flask", "run"]