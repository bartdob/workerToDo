# syntax=docker/do
FROM python:3     
ENV PYTHONDONTWRIT
ENV PYTHONUNBUFFER
WORKDIR /code     
COPY requirements.
RUN pip install --
RUN pip install ba
RUN pip install -r
COPY . /code/     



