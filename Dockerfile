FROM python:3.6.5-stretch

VOLUME [ "/puppenc" ]

WORKDIR /puppenc


COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR "/puppenc"
