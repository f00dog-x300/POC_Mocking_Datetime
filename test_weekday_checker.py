import weekday_checker
import pytest
import datetime


@pytest.fixture
def mock_datetime_weekday(monkeypatch):
    """Fixture to provide a weekday for test data"""
    mock_time = datetime.datetime(2020, 10, 23, 1, 21, 00)

    class MockToday:
        @classmethod
        def now(cls):
            return mock_time

    monkeypatch.setattr(datetime, 'datetime', MockToday)


@pytest.fixture
def mock_datetime_weekend(monkeypatch):
    """Fixture to provide a weekend for test data"""
    mock_time = datetime.datetime(2020, 11, 14, 1, 21, 00)

    class MockToday:
        @classmethod
        def now(cls):
            return mock_time

    monkeypatch.setattr(datetime, 'datetime', MockToday)


def test_check_for_weekday(mock_datetime_weekday):
    """validating if working as expected for weekday"""
    assert weekday_checker.is_weekend() == (True, 4)


def test_check_for_weekend(mock_datetime_weekend):
    """validating if working as expected for weekend"""
    assert weekday_checker.is_weekend() == False
