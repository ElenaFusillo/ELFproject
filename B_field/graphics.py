import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def main_graphics(x, y, z_grid, xp, yp, cables_array):
    '''
    TODO docstring
    '''
    fig, ax = plt.subplots(constrained_layout=True)
    levels = np.geomspace(z_grid.min(), z_grid.max(), num=20)
    filled_contours = ax.contourf(x, y, z_grid, levels, norm=colors.LogNorm(vmin=z_grid.min(), vmax=z_grid.max()), cmap='inferno', origin='lower')
    line_values = (3, 10, 100)
    line_contours = ax.contour(filled_contours, levels=line_values, colors='g', origin='lower')
    plt.clabel(line_contours, inline=True, fmt='%1.0f', fontsize=8)

    ax.set_title('B field isolines')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')

    color_bar = fig.colorbar(filled_contours, shrink=0.8, ticks=(z_grid.min(), 0, 1, 3, 10, 100, z_grid.max()), format='%.2f')
    color_bar.ax.set_ylabel('B field (microTesla) - logscale')
    color_bar.add_lines(line_contours)

    poi, = plt.plot(xp, yp, 'bo')
    plt.legend([poi], ['Point of interest'])

    cables = []
    for i in range(2):
        for j in range(3):
            if min(x) < cables_array[i, j, 1] < max(x) and min(y) < cables_array[i, j, 2] < max(y):
                cables, = plt.plot(cables_array[i, j, 1], cables_array[i, j, 2], 'ko')
                plt.legend([poi, cables], ['Point of interest', 'Triad cables'])

    plt.show()
