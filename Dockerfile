FROM python:3-buster

EXPOSE 8080
WORKDIR /app/live
COPY . /app/live
ENTRYPOINT [ "/app/live/starter.sh" ]