FROM python:3

WORKDIR /usr/src/app

COPY ./api ./

COPY ./requirements.txt .

COPY ./config.yaml .

COPY ./storage_utils ./storage_utils

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]