import pytest
import ingestion
from datetime import datetime, timedelta

def test_t():
    last_x_hours = 1
    assert ingestion.check_date(datetime.now(),last_x_hours) == True
    assert ingestion.check_date(datetime.now() - timedelta(hours=2), last_x_hours) == False