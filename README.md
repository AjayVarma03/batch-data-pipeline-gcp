# Batch Data Pipeline (GCP)

## Overview
This project builds a production-grade batch data pipeline using GCP.

## Features
- Batch ingestion from CSV
- Incremental processing
- Idempotent loads using MERGE
- Data quality validation
- Audit logging
- Backfill support
- Infrastructure as Code (Terraform)

## Project Structure
- terraform/ → Infrastructure setup
- airflow/ → DAGs
- etl/ → Python scripts
- sql/ → SQL queries
- data/ → Sample data
- docs/ → Architecture details