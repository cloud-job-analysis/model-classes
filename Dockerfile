FROM python:3.6
MAINTAINER TeamBAYES

WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY . /app
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
RUN cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
RUN apt-get install -y openssh-server

RUN wget http://apache.mirrors.ionfish.org/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
RUN tar -xzvf hadoop-3.1.2.tar.gz
RUN mv hadoop-3.1.2 /usr/local/hadoop
RUN echo "export HDFS_NAMENODE_USER="root"" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh
RUN echo "export HDFS_DATANODE_USER="root"" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh
RUN echo "export HDFS_SECONDARYNAMENODE_USER="root"" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh

RUN apt-get install -y default-jdk

RUN echo "export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh
RUN pip install Flask
RUN pip install requests
RUN pip install -U scikit-learn
RUN python -m pip install --user numpy scipy
RUN pip freeze

CMD ["./entrypoint.sh"]
