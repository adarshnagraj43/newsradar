FROM python:3.9

WORKDIR /

COPY / .

RUN pip3 install -e .

WORKDIR  /app
RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 8080

CMD [ "python", "main.py" ]
