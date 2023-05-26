"""
create-covid-table_
"""

from yoyo import step

__depends__ = {'20230526_01_Qd1SN-create-covid-schema'}

steps = [
    step(
        """
        CREATE TABLE covid.covid
        (
            id VARCHAR(50),
            country_region VARCHAR(255),
            last_update TIMESTAMP,
            confirmed BIGINT,
            deaths BIGINT,
            incident_rate DOUBLE PRECISION,
            case_fatality_ratio DOUBLE PRECISION
            
        )
        """,
        "DROP TABLE covid.covid",
    )
]
