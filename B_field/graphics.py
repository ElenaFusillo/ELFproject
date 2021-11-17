import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

def main_graphics(x, y, z_grid, xp, yp, cables_array, subparser_type):
    '''
    TODO docstring
    '''
    fig, ax = plt.subplots(constrained_layout=True)
    levels = np.logspace(-1, 2, num=25)
    filled_contours = ax.contourf(x, y, z_grid, levels, norm=colors.LogNorm(vmin=z_grid.min(), vmax=z_grid.max()), cmap=plt.cm.hot, origin='lower')
    line_values = (3, 10, 100)
    line_contours = ax.contour(filled_contours, levels=line_values, colors='k', origin='lower')
    plt.clabel(line_contours, inline=True, fmt='%1.0f', fontsize=8)

    ax.set_title('B field isolines')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')

    color_bar = fig.colorbar(filled_contours, shrink=0.8, ticks=(0, 3, 10, 100, z_grid.max()), format='%.1f')
    color_bar.ax.set_ylabel('B field (microTesla)')
    color_bar.add_lines(line_contours)

    poi, = plt.plot(xp, yp, 'bo')
    
    if subparser_type == 'single':
        cable_1, = plt.plot(cables_array[0, 1], cables_array[0, 2], 'ko')
        cable_2, = plt.plot(cables_array[1, 1], cables_array[1, 2], 'go')
        cable_3, = plt.plot(cables_array[2, 1], cables_array[2, 2], 'yo')
        plt.legend([poi, cable_1, cable_2, cable_3], ['Point of interest', 'Cable 1', 'Cable 2', 'Cable 3'])

    elif subparser_type == 'double':
        cableA_1, = plt.plot(cables_array[0, 0, 1], cables_array[0, 0, 2], 'ko')
        cableA_2, = plt.plot(cables_array[0, 1, 1], cables_array[0, 1, 2], 'go')
        cableA_3, = plt.plot(cables_array[0, 2, 1], cables_array[0, 2, 2], 'yo')
        cableB_1, = plt.plot(cables_array[1, 0, 1], cables_array[1, 0, 2], 'ko')
        cableB_2, = plt.plot(cables_array[1, 1, 1], cables_array[1, 1, 2], 'go')
        cableB_3, = plt.plot(cables_array[1, 2, 1], cables_array[1, 2, 2], 'yo')

        plt.legend([poi, cableA_1, cableA_2, cableA_3, cableB_1, cableB_2, cableB_3],
                   ['Point of interest', 'Cable 1A', 'Cable 2A', 'Cable 3A',
                   'Cable 1B', 'Cable 2B', 'Cable 3B'], fontsize=6)

    plt.show()
