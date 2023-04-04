# based on
FROM python:3.7

# Airflow gloval vars
ARG AIRFLOW_VERSION=1.10.14
ARG AIRFLOW_USER_HOME=/usr/local/airflow
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}
ARG SPARK_VERSION="3.1.2"
ARG HADOOP_VERSION="3.2"

# Build airflow
RUN pip install apache-airflow[postgres]==${AIRFLOW_VERSION}
RUN pip install SQLAlchemy==1.3.23
RUN pip install markupsafe==2.0.1
RUN pip install wtforms==2.3.3
RUN pip install kaggle
RUN pip install boto3
RUN pip install pathlib

# Make directory for dags
RUN mkdir /project

# Copy scripts and config
COPY script/ /project/scripts/
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Set script access
RUN chmod +x /project/scripts/init.sh


#Java installation
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get install -y gnupg2 && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB9B1D8886F44E2A && \
    add-apt-repository "deb http://security.debian.org/debian-security stretch/updates main" && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    pip freeze && \
    java -version $$ \
    javac -version
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64
RUN export JAVA_HOME

ENV SPARK_HOME /usr/local/spark

# Spark submit binaries and jars (Spark binaries must be the same version of spark cluster)
RUN cd "/tmp" && \
        wget --no-verbose "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
        tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
        mkdir -p "${SPARK_HOME}/bin" && \
        mkdir -p "${SPARK_HOME}/assembly/target/scala-2.12/jars" && \
        cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin/." "${SPARK_HOME}/bin/" && \
        cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/." "${SPARK_HOME}/assembly/target/scala-2.12/jars/" && \
        rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

# Create SPARK_HOME env var
RUN export SPARK_HOME
ENV PATH $PATH:/usr/local/spark/bin


# Run script
ENTRYPOINT ["/project/scripts/init.sh"]
