FROM python:3.8

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
