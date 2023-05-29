# Covid data pipeline

This is an etl pipeline to pull covid data from a public api periodically with cron, then gets stored in warehouse.

## - Tech stack:
- Python
- Pytest
- Terraform for creating GCP compute engine simulating production environment
- Docker
- ci/cd
- Postgres
- Metabase

## Architecture

![](./assets/images/architecture.png)

## Dashboard

![](./assets/images/board2.png)
