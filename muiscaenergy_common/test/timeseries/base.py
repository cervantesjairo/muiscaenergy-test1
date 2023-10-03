import unittest
from datetime import datetime, timedelta
import pandas as pd
from muiscaenergy_common.src.timeseries.base import (get_timeseries,
                                                     parse_custom_freq)


class TestMyModule(unittest.TestCase):

    def test_get_timeseries_no_timezone(self):
        ts_from = datetime(2023, 9, 30, 12, 0, 0)
        ts_to = datetime(2023, 10, 1, 11, 0, 0)
        freq = 'H'

        df = get_timeseries(ts_from=ts_from, ts_to=ts_to, freq=freq).df

        self.assertFalse(df.empty)
        self.assertTrue('datetime' in df.columns)

    # def test_get_timeseries_with_timezone(self):
    #     ts_from = datetime(2023, 9, 30, 12, 0, 0)
    #     ts_to = datetime(2023, 10, 1, 11, 0, 0)
    #     freq = 'H'
    #     lat = 40.7128  # New York
    #     lon = -74.0060
    #     tz = "America/New_York"
    #
    #     df = get_timeseries(ts_from=ts_from, ts_to=ts_to, freq=freq, lat=lat, lon=lon, tz=tz)
    #
    #     self.assertFalse(df.empty)
    #     self.assertTrue('datetime_utc' in df.columns)
    #     self.assertTrue('datetime_local_from' in df.columns)
    #     self.assertTrue('datetime_local_to' in df.columns)
    #
    # def test_get_timeseries_with_tz_only(self):
    #     ts_from = datetime(2023, 9, 30, 12, 0, 0)
    #     ts_to = datetime(2023, 10, 1, 12, 0, 0)
    #     freq = 'H'
    #     tz = "America/New_York"
    #
    #     df = get_timeseries(ts_from=ts_from, ts_to=ts_to, freq=freq, tz=tz)
    #
    #     self.assertFalse(df.empty)
    #     self.assertTrue('datetime_utc' in df.columns)
    #     self.assertTrue('datetime_local_from' in df.columns)
    #     self.assertTrue('datetime_local_to' in df.columns)
    #


    def test_parse_custom_freq(self):
        freq = '15T'
        td = parse_custom_freq(freq)

        self.assertEqual(td, pd.Timedelta(minutes=15))


if __name__ == '__main__':
    unittest.main()

# import unittest
# from datetime import datetime
# from muiscaenergy_common.src.timeseries.base import get_timeseries
#
# class TimeSeriesTest(unittest.TestCase):
#
#     def test_get_timeseries(self):
#         # df = get_timeseries(ts_from=datetime(2022, 4, 10),
#         #         ts_to=datetime(2022, 4, 11),
#         #         freq='H')
#
#         df = get_timeseries(ts_from=datetime(2022, 4, 10),
#         ts_to = datetime(2022, 4, 11),
#         freq = 'H',
#         tz = "America/Los_Angeles")
#
#         self.assertFalse(df.empty)
#         self.assertTrue('datetime_local_from' in df.columns)
#         # self.assertTrue('datetime_local_to' in df.columns)
#
#     def test_get_ts_tz(self):
#         # tz = "America/New_York"; tz = "America/Los_Angeles"; tz = "America/Chicago";
#         ts = TS(ts_from=datetime(2022, 4, 10),
#                 ts_to=datetime(2022, 4, 11),
#                 freq='H',
#                 tz="America/Los_Angeles")
#
#         df = ts.get_ts_tz()
#
#         self.assertFalse(df.empty)
#         self.assertTrue('datetime_utc' in df.columns)
#         self.assertTrue('datetime_local_from' in df.columns)
#         self.assertTrue('datetime_local_to' in df.columns)
#
#     def test_get_by_latlon(self):
#         lat = 40.7128  # Nueva York
#         lon = -74.0060
#         ts = TS(ts_from=datetime(2022, 4, 10),
#                 ts_to=datetime(2022, 4, 11),
#                 freq='2D',
#                 lat=lat,
#                 lon=lon)
#         df = ts.get_ts_latlon()
#
#         self.assertFalse(df.empty)
#         self.assertTrue('datetime_utc' in df.columns)
#         self.assertTrue('datetime_local_from' in df.columns)
#         self.assertTrue('datetime_local_to' in df.columns)
#
# if __name__ == '__main__':
#     unittest.main()
