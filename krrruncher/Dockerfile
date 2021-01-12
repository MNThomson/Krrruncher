FROM python:3.9

COPY ./requirements.txt /krrruncher/requirements.txt

WORKDIR /krrruncher

RUN pip3 install -r requirements.txt

COPY . /krrruncher

ENTRYPOINT [ "python3" ]

CMD [ "-u", "krrrunch.py" ]