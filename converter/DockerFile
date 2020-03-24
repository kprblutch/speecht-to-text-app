FROM python:3.7.7-buster
RUN apt update
WORKDIR /converter
ADD requirements.txt /converter/requirements.txt
RUN pip install -r /converter/requirements.txt
ADD . /converter
ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]