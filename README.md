# GitHub Commit Velocity: End-to-End Data Pipeline

An automated, local ELT pipeline utilizing a Medallion architecture (Bronze, Silver, Gold) to extract, transform, and visualize GitHub repository commit data. 

## Architecture & Tech Stack
* **Extraction (Bronze):** Python and **dlt** pull the latest commit data from the public GitHub REST API and load the raw JSON directly into the data warehouse.
* **Storage:** **DuckDB** acts as the local analytical data warehouse.
* **Transformation (Silver & Gold):** **dbt** cleans the nested JSON (Silver layer) and aggregates the data into daily contributor metrics (Gold layer). Includes automated data quality tests for uniqueness and null constraints.
* **Visualization:** **Streamlit** queries the Gold layer to serve a local interactive web dashboard.
* **Automation:** Configured to run daily via Windows Task Scheduler.

## Repository Structure
* `extract_github.py`: The dlt pipeline script that handles API pagination and database loading.
* `transform_layer/`: The dbt project containing data quality tests and SQL models for Silver and Gold transformations.
* `dashboard.py`: The Streamlit application for data visualization.
* `run_pipeline.bat`: The executable script used for local task scheduling.

## How to Run Locally

1. Clone this repository and create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
Install the required dependencies:

Bash
pip install "dlt[duckdb]" dbt-duckdb requests streamlit pandas
Run the extraction pipeline:

Bash
python extract_github.py
Run the transformations and tests:

Bash
cd transform_layer
dbt run
dbt test
cd ..
Launch the dashboard:

Bash
streamlit run dashboard.py
Author: Ivan Manuel Advincula

