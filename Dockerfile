FROM python:3.10.3

ENV PYTHONUNBUFFERED=1

COPY . .

WORKDIR /src

RUN pip install -r /requirements.txt


#CMD ["python", "manage.py runserver"]
