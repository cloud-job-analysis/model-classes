FROM python:3.6
MAINTAINER TeamBAYES

WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY . /app
ENV DEBIAN_FRONTEND noninteractive

RUN tar -xzvf hadoop-3.1.2.tar.gz
RUN mv hadoop-3.1.2 /usr/local/hadoop

RUN apt-get update 
RUN apt-get install -y default-jdk

RUN echo "export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh

RUN pip install Flask
RUN pip install requests
RUN pip install -U scikit-learn
RUN python -m pip install --user numpy scipy
RUN pip freeze

CMD ["python", "agent.py"]
