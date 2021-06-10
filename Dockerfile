FROM python:3.9

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# This's gonna create folder /app and cd app in docker container
WORKDIR /app

# This's gonna copy to WORKDIR
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# This's gonna copy to WORKDIR/app
COPY ./app ./app

# COPY ./app ./

# After all tree in docker container will be like this
# app = requirements.txt, app
# app/app = app (local)

# This run command in terminal
# RUN ["apt-get", "update"]
# RUN ["apt-get", "install", "-y", "vim"]

# This CMD for using app
CMD uvicorn --host=0.0.0.0 --reload app.main:app