FROM python:3.10

WORKDIR /code

RUN mkdir /code/app/

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app/ /code/app/

CMD ["fastapi", "run", "app/main.py", "--port", "$LISTEN_PORT"]