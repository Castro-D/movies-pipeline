import logging
import sys
from typing import Any, Dict, List

import psycopg2.extras as p
import requests

from covid.utils.db import WarehouseConnection
from covid.utils.db_config import get_warehouse_creds


def get_covid_data() -> List[Dict[str, Any]]:
    url = 'https://coronavirus.m.pipedream.net/'
    try:
        r = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        sys.exit(1)
    return r.json().get('rawData', [])


def _get_covid_insert_query() -> str:
    return '''
    INSERT INTO covid.covid_stats (
       country_region,
       Last_Update,
       confirmed,
       deaths,
       incident_rate,
       case_fatality_ratio,
       combined_key
    )
    VALUES (
        %(Country_Region)s,
        %(Last_Update)s,
        %(Confirmed)s,
        %(Deaths)s,
        %(Incident_Rate)s,
        %(Case_Fatality_Ratio)s,
        %(Combined_Key)s
    );
    '''


def validate_data(rec) -> None:
    if rec['Incident_Rate'] == '':
        rec['Incident_Rate'] = 0.0
    if rec['Case_Fatality_Ratio'] == '':
        rec['Case_Fatality_Ratio'] = 0.0


def run() -> None:
    data = get_covid_data()
    for record in data:
        validate_data(record)

    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        p.execute_batch(curr, _get_covid_insert_query(), data)


if __name__ == '__main__':
    run()
