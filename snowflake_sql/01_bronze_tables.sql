USE WAREHOUSE WH_BROADBAND_DEV;
USE DATABASE BROADBAND_DEV;

CREATE SCHEMA IF NOT EXISTS BRONZE;
CREATE SCHEMA IF NOT EXISTS SILVER;
CREATE SCHEMA IF NOT EXISTS GOLD;
CREATE SCHEMA IF NOT EXISTS MONITORING;

CREATE OR REPLACE TABLE BRONZE.CUSTOMERS_RAW (
    customer_id STRING,
    gender STRING,
    age STRING,
    province STRING,
    segment STRING,
    register_date STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);

CREATE OR REPLACE TABLE BRONZE.SUBSCRIPTIONS_RAW (
    subscription_id STRING,
    customer_id STRING,
    package_name STRING,
    promotion_price STRING,
    start_date STRING,
    end_date STRING,
    status STRING,
    network_operation STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);

CREATE OR REPLACE TABLE BRONZE.PAYMENTS_RAW (
    payment_id STRING,
    subscription_id STRING,
    bill_month STRING,
    billed_amount STRING,
    paid_amount STRING,
    payment_status STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);

CREATE OR REPLACE TABLE BRONZE.NETWORK_USAGE_RAW (
    subscription_id STRING,
    usage_date STRING,
    month_id STRING,
    download_gb STRING,
    upload_gb STRING,
    avg_speed_mbps STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);

CREATE OR REPLACE TABLE BRONZE.TROUBLE_TICKETS_RAW (
    ticket_id STRING,
    subscription_id STRING,
    ticket_date STRING,
    issue_type STRING,
    resolution_days STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);

CREATE OR REPLACE TABLE BRONZE.PRODUCT_ONTOP_RAW (
    subscription_id STRING,
    product_name STRING,
    start_month STRING,
    monthly_fee STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);

CREATE OR REPLACE TABLE BRONZE.CALENDAR_MONTHS_RAW (
    month_date STRING,
    month_id STRING,
    input_file_name STRING,
    ingestion_timestamp TIMESTAMP,
    source_system STRING,
    batch_id STRING
);