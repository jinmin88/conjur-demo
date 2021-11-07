FROM python:3.8-slim-buster AS conjur-demo

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" , "src/app.py" ]
