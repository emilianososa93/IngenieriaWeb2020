FROM python:3.8.5

RUN mkdir /app_grupo7
WORKDIR /app_grupo7

COPY requirements.txt /app_grupo7/

RUN pip install -r requirements.txt

COPY . /app_grupo7/

ENV EN_DOCKER = True

RUN mkdir /app_grupo7/data

CMD ["python", "Comunidad_Educativa/manage.py", "runserver", "0.0.0.0:8000"]