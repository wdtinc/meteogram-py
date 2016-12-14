from datetime import datetime, timedelta
from meteogrampy import Meteogram, SubPlot
from meteogrampy.styles import Temperature, WindSpeed, WindDirection, Freezing

# Lets create some data, and simulate a cold front passage
temperature_data = [50, 49, 18, 17, 18, 18, 19]
wind_speed_data = [10, 25, 26, 30, 25, 26, 28]
wind_direction_data = [180, 345, 355, 1, 355, 354, 356]

dates = []
date = datetime(2016, 12, 25, 12, 0)
dates.append(date)
for x in xrange(len(temperature_data) - 1):
    date = date + timedelta(seconds=3600)
    dates.append(date)

# We can create a freezing line as well
freezing_data = [32 for x in dates]

temp = Meteogram.variable(Temperature, [dates, temperature_data])
freezing = Meteogram.variable(Freezing, [dates, freezing_data])
wind_speed = Meteogram.variable(WindSpeed, [dates, wind_speed_data])
wind_direction = Meteogram.variable(WindDirection, [dates, wind_direction_data])

# Plot both freezing and temp on the same axis and subplot
temp_plot = SubPlot(left_vars=(temp, freezing))

# Plot wind speed on left axis, wind direction on right, but still on same subplot
wind_plot = SubPlot(left_vars=wind_speed, right_var=wind_direction)
wind_plot.right_ylim = (0, 360)

meteogram = Meteogram((wind_plot, temp_plot))
meteogram.title = "Sweet data bro!"
meteogram.show()