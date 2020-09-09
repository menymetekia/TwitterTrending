import pytest
import ingestion
from datetime import datetime, timedelta

def test_last_x_hours():
    last_x_hours = 1
    assert ingestion.check_date(datetime.utcnow(),last_x_hours) == True
    assert ingestion.check_date(datetime.utcnow() - timedelta(hours=2), last_x_hours) == False

    last_x_hours = 72
    #Just within 72 hours
    assert ingestion.check_date(datetime.utcnow() - timedelta(hours=71, minutes=59), last_x_hours) == True
    #Just after 72 hours
    assert ingestion.check_date(datetime.utcnow() - timedelta(hours=72,minutes=1),last_x_hours) == False
    #Exactly 72 hours
    assert ingestion.check_date(datetime.utcnow() - timedelta(hours=72), last_x_hours) == False

def test_trends():
