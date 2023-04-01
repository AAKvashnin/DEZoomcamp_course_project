#!/bin/bash

# Create airflow DB
sleep 10
airflow upgradedb
sleep 10

# Run airflow scheduler
airflow scheduler & airflow webserver
