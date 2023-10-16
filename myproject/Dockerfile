  FROM python:latest
  LABEL maintainer="Adya Nand Jha, adya.nand.jha1@ibm.com"
  RUN apt-get update
  RUN apt-get install -y vim
  RUN mkdir /app
  WORKDIR /app
  COPY . /app
  RUN pip install -r requirements.txt
  EXPOSE 5000
  ENTRYPOINT [ "python3" ]
  CMD [ "app.py" ]