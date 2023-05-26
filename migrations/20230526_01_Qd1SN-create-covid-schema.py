"""
create-covid-schema_
"""

from typing import Any

from yoyo import step

__depends__: Any = {}

steps = [step("CREATE SCHEMA covid", "DROP SCHEMA covid")]