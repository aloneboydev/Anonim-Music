FROM nikolaik/python-nodejs:python3.9-nodejs16
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
COPY . /app/
WORKDIR /app/
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
RUN if [ $OKTETO_TOKEN ]; then curl https://get.okteto.com -sSfL | sh; fi
CMD python3 -m Music
