import matplotlib.pyplot as plt

from matplotlib.dates import date2num, num2date


class Variable(object):
    def __init__(self, style, data=None):
        try:
            self.label = style['label']
        except KeyError, e:
            self.label = None

        self._style = style
        self._ylim = None
        if data:
            self._dates = date2num(data[0])
            self._vals = data[1]
        else:
            self._dates = []
            self._vals = []

    def append(self, date, val):
        self._dates.append(date2num(date))
        self._vals.append(val)

    def plot(self, axis):
        axis.plot_date(self._dates, self._vals, **self._style)


class Fill(Variable):
    def __init__(self, style, data=None):
        super(Fill, self).__init__(style, data)

    def plot(self, axis):
        axis.fill_between(self._dates, self._vals, **self._style )


class Bar(Variable):
    def __init__(self, style, data=None):
        super(Bar, self).__init__(style, data)

    def plot(self, axis):
        axis.bar(self._dates, self._vals, **self._style)


# Registry of all Variable types currently implemented
PLOT_TYPES = {'line': Variable,
              'marker': Variable,
              'bar': Bar,
              'fill_to': Fill}


class SubPlot:
    def __init__(self, left_vars, right_var=None):
        self._left_axis = None
        self._left_label = None
        self._right_axis = None
        self._right_label = None

        self._left_ylim = None
        self._right_ylim = None
        try:
            self._left_vars = [var for var in left_vars]
        except Exception, e:
            self._left_vars = [left_vars]

        self._right_var = right_var

    @property
    def left_ylim(self):
        return self._left_ylim

    @left_ylim.setter
    def left_ylim(self, top_bottom):
        self._left_ylim = top_bottom

    @property
    def right_ylim(self):
        return self._right_ylim

    @right_ylim.setter
    def right_ylim(self, top_bottom):
        self._right_ylim = top_bottom

    def plot_vars(self, axis):
        self._left_axis = axis
        for var in self._left_vars:
            var.plot(axis)
        axis.legend(loc=2, frameon=False, numpoints=1)
        self._left_axis.set_xticklabels([num2date(d).strftime('%Y-%m-%dT%H:%M:%S') for d in
                                         self._left_axis.get_xticks()], rotation=30)
        if self.left_ylim:
            self._left_axis.set_ylim(self._left_ylim)

        # Make room for legends
        left_ylim = self._left_axis.get_ylim()
        ticks = self._left_axis.get_yticks()
        self._left_axis.set_ylim(top=left_ylim[1]*1.2)
        self._left_axis.set_yticks(ticks)

        if self._right_var:
            self._right_axis = axis.twinx()
            self._right_var.plot(self._right_axis)
            if self._right_ylim:
                self._right_axis.set_ylim(self._right_ylim)

            # Make room for legends
            right_ylim = self._right_axis.get_ylim()
            ticks = self._right_axis.get_yticks()
            self._right_axis.set_ylim(top=right_ylim[1]*1.2)
            self._right_axis.set_yticks(ticks)
            self._right_axis.legend(loc=1, frameon=False, numpoints=1)


class Meteogram(object):
    def __init__(self, subplots, title=None):
        """

        :param subplots: Order matters.  Plots will be plotted in order top to bottom with the last
                         subplot being the "anchor".
        :param title:
        """
        # Setup a figure for this meteogram, and alter the subplots so there is no whitespace between them.
        self.fig = plt.figure(facecolor='white', figsize=(15, 8))
        self._title = title
        plt.subplots_adjust(bottom=0.2, hspace=0.1)

        try:
            self._subplots = [plot for plot in subplots]
        except Exception, e:
            self._subplots = [subplots]
        self._plotted = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    @classmethod
    def variable(cls, style, data=None):
        try:
            return PLOT_TYPES[style['plot_type']](style['mpl_options'], data)
        except KeyError, e:
            raise Exception('plot_type of %s is unknown.' % style['plot_type'])

    def show(self):
        self._plot()
        plt.show(self.fig)

    def save(self, fname, **kwargs):
        """

        :param fname:
        :param kwargs: Any of the valid args at http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig
        :return:
        """
        self._plot()
        if 'bbox_inches' not in kwargs.keys():
            kwargs['bbox'] = 'tight'
        plt.savefig(fname, **kwargs)

    def _plot(self):
        num_subplots = len(self._subplots)
        for i, subplot in enumerate(self._subplots):
            var_axis = plt.subplot2grid((num_subplots, 3), (i, 0), colspan=3)
            self._plotted.append(var_axis)
            subplot.plot_vars(var_axis)

        # Go through each subplot except the last (bottom) and:
        # 1.) Align the x-axis with the bottom subplot
        # 2.) Remove x-ticks to clean up the plot
        for axis in self._plotted[:-1]:
            axis.set_xlim(*self._plotted[-1].get_xlim())
            axis.set_xticks([])

        self.fig.suptitle(self._title)

