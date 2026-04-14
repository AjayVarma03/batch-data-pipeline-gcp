# Batch Data Pipeline — GCP

A production-grade batch data pipeline built on Google Cloud Platform. It reads CSV data, validates it, transforms it, and loads it into BigQuery using incremental MERGE logic, with full audit logging and Apache Airflow orchestration.

---

## What this pipeline does

Every time the pipeline runs, it:

1. **Extracts** data from a CSV file in Google Cloud Storage
2. **Validates** the data — checks for nulls, bad types, out-of-range values
3. **Transforms** the data — cleans, renames, and enriches fields
4. **Loads** it into BigQuery using a MERGE statement (no duplicates, ever)
5. **Logs** every run with row counts, timestamps, and pass/fail status

---

## Architecture

```
CSV File (GCS)
      │
      ▼
  extract.py          ← reads the CSV into a pandas DataFrame
      │
      ▼
  validate.py         ← checks data quality, rejects bad rows
      │
      ▼
  transform.py        ← cleans and enriches the data
      │
      ▼
  load.py             ← uploads to BigQuery staging table
      │
      ▼
  MERGE SQL           ← upserts into the final BigQuery table
      │
      ▼
  audit log           ← writes run metadata to BigQuery audit table
```

Airflow orchestrates all of the above steps on a daily schedule.

---

## Project structure

```
batch-data-pipeline-gcp/
│
├── run_etl.py                  ← entry point: runs the full pipeline manually
│
├── etl/
│   ├── extract.py              ← reads CSV from GCS into a DataFrame
│   ├── transform.py            ← cleans and transforms the data
│   ├── validate.py             ← data quality checks
│   └── load.py                 ← loads to BigQuery (staging + MERGE)
│
├── airflow/
│   └── dags/
│       └── batch_pipeline_dag.py   ← Airflow DAG (daily schedule)
│
├── sql/
│   └── merge.sql               ← MERGE statement for idempotent loads
│
├── scripts/
│   └── setup_gcp.sh            ← GCP setup script (APIs, buckets, BQ datasets)
│
├── data/
│   └── sample_data.csv         ← sample input file for testing
│
└── logs/
    └── pipeline.log            ← local run logs
```

---

## Tech stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | ETL logic (extract, transform, validate, load) |
| Apache Airflow | Pipeline orchestration and scheduling |
| Google BigQuery | Data warehouse (target) |
| Google Cloud Storage | Source file storage |
| Pandas | In-memory data transformation |
| BigQuery Python SDK | Loading data to BQ |
| Terraform | Infrastructure as Code (optional) |

---

## Prerequisites

Before running this project, you need:

- A Google Cloud account with billing enabled
- A GCP project created
- The following APIs enabled: BigQuery API, Cloud Storage API
- Python 3.10 or higher installed on your machine
- `gcloud` CLI installed and authenticated

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/AjayVarma03/batch-data-pipeline-gcp.git
cd batch-data-pipeline-gcp
```

### 2. Install Python dependencies

```bash
pip install pandas google-cloud-bigquery google-cloud-storage apache-airflow
```

### 3. Configure GCP credentials

```bash
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project-id
```

### 4. Run the GCP setup script

```bash
bash scripts/setup_gcp.sh
```

This creates the GCS bucket, BigQuery dataset, and required tables.

---

## Running the pipeline

### Manual run (no Airflow)

```bash
python run_etl.py
```

This runs extract → validate → transform → load in sequence and writes logs to `logs/pipeline.log`.

### With Airflow

```bash
# Copy the DAG to your Airflow dags folder
cp airflow/dags/batch_pipeline_dag.py ~/airflow/dags/

# Start Airflow
airflow standalone

# Open the Airflow UI at http://localhost:8080
# Trigger the batch_pipeline_dag manually or wait for the daily schedule
```

---

## Key design decisions

**Incremental loading with MERGE**
The pipeline never does a full reload. Every run uses a MERGE statement in BigQuery — if a row already exists (matched by ID), it updates it; if it's new, it inserts it. This means the pipeline is safe to re-run without creating duplicates.

**Idempotency**
Running the pipeline twice produces the same result as running it once. This is critical for backfill scenarios and recovery from failures.

**Data quality before load**
The `validate.py` step runs before any data touches BigQuery. Rows that fail validation are rejected and logged — they never make it into the warehouse.

**Audit logging**
Every pipeline run writes a record to a `pipeline_audit` table in BigQuery containing the run timestamp, row counts, validation pass/fail counts, and status. You can query this table to see the full history of pipeline runs.

---

## Backfill

To reprocess data for a historical date:

```bash
python run_etl.py --date 2024-01-15
```

The pipeline reads the file for that date from GCS and reloads it using the MERGE logic. Existing rows are updated, not duplicated.

---

## Logs

Local logs are written to `logs/pipeline.log`. Each run appends to this file with timestamps:

```
2024-01-15 08:00:01 - INFO - ===== PIPELINE STARTED =====
2024-01-15 08:00:02 - INFO - Extracted 5000 rows from GCS
2024-01-15 08:00:03 - INFO - Validation passed: 4987 rows. Rejected: 13 rows
2024-01-15 08:00:05 - INFO - Loaded 4987 rows to BigQuery staging
2024-01-15 08:00:06 - INFO - MERGE complete. Inserted: 3200, Updated: 1787
2024-01-15 08:00:06 - INFO - ===== PIPELINE COMPLETE =====
```

---

## Author

**Ajay Varma** — [github.com/AjayVarma03](https://github.com/AjayVarma03)
