import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def contours(ax, x, y, z_grid):
    '''
    Given a grid of x and y coordinates, with the corresponding B values associated,
    the function calculates the filled contours to plot and the 3, 10, 100 microTesla isolines.

    Parameters
    -------------------
    ax: matplotlib.axes._subplots.AxesSubplot
        Subplot axes.
    x, y, z_grid : numpy.ndarray
        Abscissas (m) and ordinates (m) to plot with corresponding B values (microTesla).

    Returns
    -------------------
    filled_contours, line_contours : matplotlib.contour.QuadContourSet
        Matplotlib objects that plot the filled contours and the 3, 10, 100 microTesla isolines

    '''
    levels = np.geomspace(z_grid.min(), z_grid.max(), num=20)
    filled_contours = ax.contourf(x, y, z_grid, levels, norm=colors.LogNorm(vmin=z_grid.min(), vmax=z_grid.max()), cmap='inferno', origin='lower')
    line_values = (3, 10, 100)
    line_contours = ax.contour(filled_contours, levels=line_values, colors='g', origin='lower')
    plt.clabel(line_contours, inline=True, fmt='%1.0f', fontsize=8)
    return filled_contours, line_contours


def color_bar(fig, z_grid, filled_contours, line_contours):
    '''
    It creates the figure's color bar with the corresponding label.
    
    Parameters
    -------------------
    fig : matplotlib.figure.Figure
        Subplot figure.
    z_grid : numpy.ndarray
        Plotted B values (microTesla).
    filled_contours, line_contours : matplotlib.contour.QuadContourSet
        Matplotlib objects that plot the filled contours and the 3, 10, 100 microTesla isolines
    '''

    color_bar = fig.colorbar(filled_contours, shrink=0.8, ticks=(z_grid.min(), 0, 1, 3, 10, 100, z_grid.max()), format='%.2f')
    color_bar.ax.set_ylabel('B field (microTesla) - logscale')
    color_bar.add_lines(line_contours)


def plot_poi_cables(x, y, xp, yp, cables_array):
    '''
    It plots the point of interest (xp, yp) and triad cables (if present in the visualization).

    Parameters
    -------------------
    x, y, cables_array : numpy.ndarray
        Abscissas (m) and ordinates (m) to plot.
        Array containing the phases (deg), abscissas (m) and ordinates (m) of the cables.
    xp, yp : float
        Abscissa (m) and ordinate (m) of the point of interest.
    '''

    poi, = plt.plot(xp, yp, 'bo')
    plt.legend([poi], ['Point of interest'])
    cables = []
    for i in range(2):
        for j in range(3):
            if min(x) < cables_array[i, j, 1] < max(x) and min(y) < cables_array[i, j, 2] < max(y):
                cables, = plt.plot(cables_array[i, j, 1], cables_array[i, j, 2], 'ko')
                plt.legend([poi, cables], ['Point of interest', 'Triad cables'])


def main_graphics(x, y, z_grid, xp, yp, cables_array):
    '''
    It creates the plot of the B field values given. Filled contours fill the image, 3-10-100 isolines are present (if inside the visualization area).
    Blue point indicates the point of interest, black points indicate the cables' position (if inside the visualization area).

    Parameters
    -------------------
    x, y, z_grid, cables_array : numpy.ndarray
        Abscissas (m) and ordinates (m) to plot with corresponding B values (microTesla).
        Array containing the phases (deg), abscissas (m) and ordinates (m) of the cables.
    xp, yp : float
        Abscissa (m) and ordinate (m) of the point of interest.
    '''
    fig, ax = plt.subplots(constrained_layout=True)
    filled_contours, line_contours = contours(ax, x, y, z_grid)

    ax.set_title('B field isolines')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')

    color_bar(fig, z_grid, filled_contours, line_contours)
    plot_poi_cables(x, y, xp, yp, cables_array)

    plt.show()
