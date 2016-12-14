import mock

from datetime import datetime, timedelta
from meteogrampy import Meteogram, SubPlot, Variable, Bar, Fill
from meteogrampy.styles import Temperature, Dewpoint, WindDirection, WindSpeed, Precipitation
from unittest import TestCase


class MeteogramTest(TestCase):
    def setUp(self):
        self.temperature_data = [45, 32, 18, 17, 18, 18, 19]
        self.wind_speed_data = [10, 25, 26, 30, 25, 26, 28]
        self.wind_direction_data = [180, 345, 355, 1, 355, 354, 356]

        self.dates = []
        start = datetime(2016, 12, 25, 12, 0)
        self.dates.append(start)
        for x in xrange(6):
            date = start + timedelta(seconds=1440)
            self.dates.append(date)

    def test_variable_factory(self):
        temp = Meteogram.variable(Temperature)
        self.assertIsInstance(temp, Variable)

        dewp = Meteogram.variable(Dewpoint)
        self.assertIsInstance(dewp, Variable)

        precip = Meteogram.variable(Precipitation)
        self.assertIsInstance(precip, Bar)

        wind_speed = Meteogram.variable(WindSpeed)
        self.assertIsInstance(wind_speed, Fill)

        wind_direction = Meteogram.variable(WindDirection)
        self.assertIsInstance(wind_direction, Variable)

    @mock.patch('meteogrampy.plt.subplot2grid')
    @mock.patch('meteogrampy.plt')
    def test_show(self, mock_plt, mock_subplotgrid):
        mock_subplotgrid.return_value = mock.MagicMock()

        temp = Meteogram.variable(Temperature)
        precip = Meteogram.variable(Precipitation)
        sub = SubPlot(temp, precip)

        meteogram = Meteogram(sub)

        meteogram.show()

        mock_subplotgrid.assert_called_with((1, 3), (0, 0), colspan=3)