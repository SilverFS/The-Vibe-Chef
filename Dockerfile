FROM python:3.9.0-slim

WORKDIR /app

RUN apt-get update -y && pip install pipenv && apt-get install ffmpeg && apt-get install build-essential git -y --no-install-recommends

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv lock -r > requirements.txt && pip install -r requirements.txt && pip uninstall pipenv -y && apt-get purge build-essential build-essential git -y -o APT::AutoRemove::RecommendsImportant=false

COPY . .

CMD [ "python", "./main.py" ]