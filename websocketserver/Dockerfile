FROM python:3.9

# leverage Docker cache
COPY ./requirements.txt /websocketserver/requirements.txt

WORKDIR /websocketserver

RUN pip install -r requirements.txt

COPY . /websocketserver

ENTRYPOINT [ "./websocketserver.py" ]