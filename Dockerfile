FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install unzip

RUN pip install gdown

# Replace this with the model version google drive ids
# The file is in the folder model/{version}/saved_model.zip
RUN gdown 10gOqI0R1XEDkAx85ZAilzyqwyJAkHakf

RUN unzip saved_model.zip

RUN rm saved_model.zip

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

ENV HOST 0.0.0.0

EXPOSE 8001

CMD ["python", "main.py"]