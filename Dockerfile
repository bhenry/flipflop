# syntax=docker/dockerfile:1

FROM python:slim-trixie

WORKDIR /opt/app
RUN apt-get update
RUN pip install advent-of-code-data
RUN pip install shapely

COPY . .

CMD ["python"]
