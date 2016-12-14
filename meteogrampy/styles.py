Temperature = {'plot_type': 'line',
               'mpl_options': {'linestyle': '-',
                               'linewidth': 2,
                               'color': 'red',
                               'marker': None,
                               'label': 'Temp in C'}}

Dewpoint = {'plot_type': 'line',
            'mpl_options': {'linestyle': '-',
                            'linewidth': 2,
                            'color': 'green',
                            'marker': None,
                            'label': 'Dewpoint in C'}}

Precipitation = {'plot_type': 'bar',
                 'mpl_options': {'width': 0.01,
                                 'bottom': 0,
                                 'color': 'lightgreen',
                                 'edgecolor': 'green',
                                 'alpha': 0.5,
                                 'label': 'Precipitation in mm'}}

Freezing = {'plot_type': 'line',
            'mpl_options': {'linewidth': 1,
                            'linestyle': 'dashed',
                            'marker': None,
                            'color': 'blue',
                            'label': 'Freezing'}}

WindSpeed = {'plot_type': 'fill_to',
             'mpl_options': {'linestyle': '-',
                             'linewidth': 1,
                             'color': 'lightblue',
                             'edgecolor': 'blue',
                             'alpha': 0.5,
                             'label': 'Wind Speed in m/s'}}

WindDirection = {'plot_type': 'marker',
                 'mpl_options': {'marker': 'o',
                                 'markersize': 5,
                                 'color': 'blue',
                                 'label': 'Wind Direction in deg from North'}}
