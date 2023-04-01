CREATE DATABASE online_fraud;

\c online_fraud

CREATE SCHEMA IF NOT EXISTS dwh
 AUTHORIZATION root;


CREATE SCHEMA IF NOT EXISTS datamart
    AUTHORIZATION root;


CREATE TABLE dwh.online_transaction(step int not null,
                                         type varchar(10) not null,
                                         amount numeric(20,2),
                                         nameOrig varchar(100),
                                         oldbalanceOrig numeric(20,2),
                                         newbalanceOrig numeric(20,2),
                                         nameDest varchar(100),
                                         oldbalanceDest numeric(20,2),
                                         newbalanceDest numeric(20,2),
                                         isFraud int)
partition by range(step);

create table dwh.online_transaction_100 partition of dwh.online_transaction
FOR VALUES FROM (0) to (100);

create table dwh.online_transaction_200 partition of dwh.online_transaction
FOR VALUES FROM (100) to (200);

create table dwh.online_transaction_300 partition of dwh.online_transaction
FOR VALUES FROM (200) to (300);

create table dwh.online_transaction_400 partition of dwh.online_transaction
FOR VALUES FROM (300) to (400);

create table dwh.online_transaction_500 partition of dwh.online_transaction
FOR VALUES FROM (400) to (500);

create table dwh.online_transaction_600 partition of dwh.online_transaction
FOR VALUES FROM (500) to (600);

create table dwh.online_transaction_700 partition of dwh.online_transaction
FOR VALUES FROM (600) to (700);

create table datamart.agg_trans(step int not null,
                                type varchar(10) not null,
                                isfraud int,
                                amount numeric(20,2),
                                cnt int,
                                cntDistOrig int,
                                cntDistDest int
                                );





