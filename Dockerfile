FROM python:3.6

RUN apt-get update
RUN apt-get -y install tesseract-ocr
RUN apt-get install libmagickwand-dev

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY . /usr/src/app

CMD [ "python", "./tests/temp_tests.py" ]
