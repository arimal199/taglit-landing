FROM python

WORKDIR /flask

COPY requirements.txt /flask

RUN pip install -r requirements.txt

COPY . /flask/