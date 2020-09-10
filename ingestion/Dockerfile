FROM python:3

WORKDIR /usr/src/app

COPY ./ingestion ./

COPY ./requirements.txt .

COPY ./config.yaml .

COPY ./storage_utils ./storage_utils

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-u","ingestion.py", "72"]