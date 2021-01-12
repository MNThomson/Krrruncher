FROM python:3.9

# leverage Docker cache
COPY ./requirements.txt /flaskserver/requirements.txt

WORKDIR /flaskserver

RUN pip install -r requirements.txt

COPY . /flaskserver

ENTRYPOINT [ "python" ]

CMD [ "-u", "app.py" ]