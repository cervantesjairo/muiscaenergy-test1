import unittest
from muiscaenergy_common.src.message.message import TimeSeriesMessage as TSm
import pandas as pd
from datetime import datetime
from muiscaenergy_common.src.timeseries.base import (get_timeseries,
                                                     parse_custom_freq)

class TestTimeSeriesMessage(unittest.TestCase):
    def setUp(self):
        self.ts_from = pd.date_range(start=datetime(2023, 9, 30, 12, 0, 0),
                                     end=datetime(2023, 10, 1, 11, 0, 0),
                                     freq='H',)
        self.ts_to = self.ts_from + pd.Timedelta(hours=1)

    def test_append_datetime(self):
        timeseries = pd.to_datetime(['2023-01-01', '2023-01-02'])

        msg = TSm().append_datetime(timeseries)
        self.assertTrue(TSm.DT in msg.df.columns)
        self.assertEqual(msg.df[TSm.DT].tolist(), timeseries.tolist())

    def test_append_datetime_utc(self):
        timeseries = pd.to_datetime(['2023-01-01', '2023-01-02'])

        msg = TSm().append_datetime_utc(timeseries)
        self.assertTrue(TSm.DT_UTC in msg.df.columns)
        self.assertEqual(msg.df[TSm.DT_UTC].tolist(), timeseries.tolist())

    def test_append_datetime_from(self):
        ts_from = pd.date_range(start=datetime(2023, 9, 30, 12, 0, 0),
                                end=datetime(2023, 10, 1, 11, 0, 0),
                                freq='H',)
        ts_to = ts_from + pd.Timedelta(hours=1)

        msg = (TSm()
               .append_datetime_from(ts_from)
               .append_datetime_to(ts_to))
        self.assertTrue(TSm.DT_FROM in msg.df.columns)
        self.assertTrue(TSm.DT_TO in msg.df.columns)

    def test_append(self):
        variable = ['var1', 'var2']
        value = [[10] * 24, [20] * 24]
        ts_from = datetime(2023, 9, 30, 12, 0, 0)
        ts_to = datetime(2023, 10, 1, 11, 0, 0)
        freq = 'H'
        tz = "America/New_York"

        timeseries = get_timeseries(ts_from=ts_from, ts_to=ts_to, freq=freq, tz=tz)

        timeseries = timeseries.append(variable, value)

        def test_parse_custom_freq(self):
            freq = '15T'
            td = parse_custom_freq(freq)

            self.assertEqual(td, pd.Timedelta(minutes=15))

    if __name__ == '__main__':
        unittest.main()

