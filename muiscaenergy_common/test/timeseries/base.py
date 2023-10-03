import unittest
from datetime import datetime, timedelta
import pandas as pd
from muiscaenergy_common.src.timeseries.base import get_timeseries
from muiscaenergy_common.src.message.message import TimeSeriesMessage as TSm


class TestGetTimeseries(unittest.TestCase):

    def test_get_timeseries_with_timezone(self):
        ts_from = datetime(2023, 9, 30, 12, 0, 0)
        ts_to = datetime(2023, 10, 1, 11, 0, 0)
        lat = 52.5200
        lon = 13.4050

        msg = get_timeseries(ts_from=ts_from, ts_to=ts_to, freq='H', lat=lat, lon=lon)

        self.assertIsInstance(msg, TSm)

    def test_get_timeseries_with_timezone_identifier(self):
        ts_from = datetime(2023, 9, 30, 12, 0, 0)
        ts_to = datetime(2023, 10, 1, 11, 0, 0)
        tz = 'America/Los_Angeles'

        msg = get_timeseries(ts_from=ts_from, ts_to=ts_to, freq='H', tz=tz)

        self.assertIsInstance(msg, TSm)


if __name__ == '__main__':
    unittest.main()
