FROM python:3.5

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
run pip show python_people_names

COPY . /usr/src/app

CMD [ "python", "./tests/temp_tests.py" ]
