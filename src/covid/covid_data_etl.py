import datetime
import logging
import sys
from typing import Any, Dict, List, Optional

import psycopg2.extras as p
import requests

from covid.utils.db import WarehouseConnection
from covid.utils.db_config import get_warehouse_creds

def get_exchange_data() -> List[Dict[str, Any]]:
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
       case_fatality_ratio
    )
    VALUES (
        %(Country_Region)s,
        %(Last_Update)s,
        %(Confirmed)s,
        %(Deaths)s,
        %(Incident_Rate)s,
        %(Case_Fatality_Ratio)s
    );
    '''


def run() -> None:
    data = get_exchange_data()
    for record in data:
        if record['Incident_Rate'] == '':
            record['Incident_Rate'] = 0.0
        if record['Case_Fatality_Ratio'] == '':
            record['Case_Fatality_Ratio'] = 0.0
    
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        p.execute_batch(curr, _get_covid_insert_query(), data)


if __name__ == '__main__':
    run()