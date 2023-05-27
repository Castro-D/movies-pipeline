"""
create-covid-schema_
"""

from yoyo import step

__depends__ = {}

steps = [step("CREATE SCHEMA covid", "DROP SCHEMA covid")]
