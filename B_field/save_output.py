from .calculations import main_print_point_bidim_dpa


def save_output_txt(dest, filename, current_s, xp, yp, diam_cables, cables_array, args):
    '''
    It saves inside a .txt file the output of the 'point', 'bidim' and 'dpa' CL optional arguments.
    The file is opened in 'append' mode, i.e. open for writing, appending to the end of file if it already exists.

    Print's 'file' keyword argument is made explicit so that now it is replaced with the selected destination file.

    Parameters
    -------------------
    dest, filename : string
        Destination path and filename where the output will be saved
    current_s : numpy.ndarray
        Current (A) circulating inside the considered power line/lines
        (each one composed of a triad of cables)
    xp, yp : float
        Abscissa (m) and ordinate (m) of the point of interest where
        the magnetic induction field B will be calculated at last
    diam_cables : float
        Diameter (m) of the cables in use
    cable_array : numpy array
        First column - Current phase belonging to the n-th cable under consideration
        Second and third columns - Abscissa and ordinate of the n-th cable under consideration
    args : argparse.Namespace
        Namespace object build up from attributes parsed out of the command line

    Returns
    -------------------
    None
    '''
    full_destination_txt = dest + '/' + filename + '.txt'
    with open(full_destination_txt, "a", encoding="utf-8") as output_file:
        main_print_point_bidim_dpa(current_s, xp, yp, diam_cables, cables_array, args, output_file)


def save_output_jpg(dest, filename, output_figure):
    '''
    It saves inside a .jpg file the output of the 'graph' CL optional arguments.

    Parameters
    -------------------
    dest, filename : string
        Destination path and filename where the output will be saved
    output_figure : matplotlib.figure.Figure
        Plot of the B field values given

    Returns
    -------------------
    None
    '''
    full_destination_jpg = dest + '/' + filename + '.jpg'
    output_figure.savefig(full_destination_jpg)
