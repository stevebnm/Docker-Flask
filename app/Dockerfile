FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY . /app
RUN pip3 install -r /app/requirements.txt
ENV MYSQL_USER python
ENV MYSQL_PASS python
ENV MYSQL_HOST mysql
ENV MYSQL_DB sample

# CMD python3 /app/app.py

