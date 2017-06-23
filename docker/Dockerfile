FROM python:2.7

RUN apt-get update && apt-get install -y libsndfile1

RUN mkdir /app
COPY ./ /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

#Generate the training set
#RUN python generateTrainingSet.py

