import csv
import datetime
from decimal import Decimal
from datetime import datetime

import psycopg2

from covid.covid_data_etl import run
from covid.utils.db import WarehouseConnection
from covid.utils.db_config import get_warehouse_creds


class TestCovidProject:
    def teardown_method(self, test_covid_data_etl_run):
        with WarehouseConnection(
            get_warehouse_creds()
        ).managed_cursor() as curr:
            curr.execute("TRUNCATE TABLE covid.covid_stats;")

    def get_covid_data(self):
        with WarehouseConnection(get_warehouse_creds()).managed_cursor(
            cursor_factory=psycopg2.extras.DictCursor
        ) as curr:
            curr.execute(
                '''SELECT
                        country_region,
                        Last_Update,
                        confirmed,
                        deaths,
                        incident_rate,
                        case_fatality_ratio
                        FROM covid.covid_stats;'''
            )
            table_data = [dict(r) for r in curr.fetchall()]
        return table_data

    def test_covid_data_etl_run(self, mocker):
        mocker.patch(
            'covid.covid_data_etl.get_covid_data',
            return_value=[
                r
                for r in csv.DictReader(
                    open('tests/fixtures/sample_raw_covid_data.csv')
                )
            ],
        )
        run()
        expected_result = [
            {
                
                'country_region': 'Afghanistan',
                'last_update': datetime.strptime('2023-03-10 04:21:03', '%Y-%m-%d %H:%M:%S'),
                'confirmed': 209451,
                'deaths': 7896,
                'incident_rate': 538.0424508714615,
                'case_fatality_ratio': 3.76985547932452,
            },
            {
                
                'country_region': 'Albania',
                'last_update': datetime.strptime('2023-03-10 04:21:03', '%Y-%m-%d %H:%M:%S'),
                'confirmed': 334457,
                'deaths': 3598,
                'incident_rate': 11621.96817012996,
                'case_fatality_ratio': 1.075773567304616,
            },
            {
                
                'country_region': 'Argentina',
                'last_update': datetime.strptime('2023-03-10 04:21:03', '%Y-%m-%d %H:%M:%S'),
                'confirmed': 10044957,
                'deaths': 130472,
                'incident_rate': 22225.43269916568,
                'case_fatality_ratio': 1.2988806223859395,
            },
        ]
        result = self.get_covid_data()
        assert expected_result == result