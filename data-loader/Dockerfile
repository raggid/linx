FROM python:3.8
RUN pip install pipenv
COPY . /tmp
WORKDIR /tmp
RUN pipenv install --system
CMD [ "python", "data-load.py" ]