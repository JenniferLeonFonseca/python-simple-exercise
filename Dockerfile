FROM python:3.5

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]CMD ["src/server.py"]