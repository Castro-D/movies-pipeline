"""
create-covid-stats-table_
"""

from yoyo import step

__depends__ = {'20230527_01_ou5t5-create-covid-schema'}

steps = [
    step(
        """
        CREATE TABLE covid.covid_stats
        (
            id INT,
            country_region VARCHAR(255),
            last_update TIMESTAMP,
            confirmed BIGINT,
            deaths BIGINT,
            incident_rate DOUBLE PRECISION,
            case_fatality_ratio DOUBLE PRECISION,
            PRIMARY KEY (id)
            
        )
        """,
        "DROP TABLE covid.covid_stats",
    )
]