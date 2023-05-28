FROM python:3.9-slim-buster

WORKDIR /api

COPY requirements.txt /api/requirements.txt

RUN pip install -r /api/requirements.txt

COPY app /api/app

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5555"]