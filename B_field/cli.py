from argparse import ArgumentParser

import numpy as np

from .calculations import main_print_point_bidim_dpa
from .graphics import main_graph
from .save_output import save_output_jpg, save_output_txt

def init_parser():
    '''
    Initialization of the argument parser. Version as optional argument.

    Returns
    -------------------
    parser : argparse.ArgumentParser
        An instance of a command line arguments parser.
    '''
    parser = ArgumentParser(prog='B_field',
                            usage='%(prog)s [options] path',
                            description='''Evaluation both of the effective magnetic induction B in a
                            given point (xp, yp) and the DPA (distanza di prima approssimazione),
                            due to single or double triad of cables.''',
                            fromfile_prefix_chars='@',
                            epilog='SINGLE/DOUBLE TRIAD NEEDED. SINGLE/DOUBLE \"OPTIONAL\" ARGUMENT IN ORDER TO EVALUATE SOMETHING.\n')
    parser.add_argument("-v", "--version", action="version",
                        version=f"{parser.prog} version 0.1.0.dev3")
    return parser


def init_subparser_single(subparsers):
    '''
    Initialization of the subparser "single". Optional and positional arguments are listed in order of entry on the command line.

    Parameters
    -------------------
    subparsers : argparse._SubParsersAction
        A subparser action, it will be populated with a subparser instance.

    Returns
    -------------------
    single_parser : argparse.ArgumentParser
        An instance of a command line arguments parser (subparser in this specific case).
    '''
    # Single triad
    single_parser = subparsers.add_parser('single', help='Calculate the magnetic induction B or the DPA for a single triad of cables',
                                          description='''Positional arguments can be given either manually one by one or using a configuration file (prefix character: @).
                                          Choose an optional argument in order to evaluate something.''')

    # OPTIONAL ARGUMENTS
    single_parser.add_argument('-point', '-p', action='store_true', help='Point estimate of the magnetic induction B in (xp, yp)')
    single_parser.add_argument('-bidim', '-b', action='store_true', help='2D estimate of the magnetic induction B around (xp, yp)')
    single_parser.add_argument('-graph', '-g', action='store_true', help='Graph of the 2D estimate of the magnetic induction B around (xp, yp)')
    single_parser.add_argument('-dpa', '-d', type=float, nargs=1, metavar='lim_val', help='''Estimate of the DPA (distanza di prima approssimazione)
                                                                          for the given configuration at \'lim_val\' microTesla. Suggested lim_values: 3, 10''')
    single_parser.add_argument('-save', '-s', type=str, nargs=2, metavar=('dest', 'filename'), help='Save the output in \'dest\' repository, with \'filename\' denomination')

    # POSITIONAL ARGUMENTS
    single_parser.add_argument('xp', type=float, help='Abscissa (m) of the point of interest')
    single_parser.add_argument('yp', type=float, help='Ordinate (m) of the point of interest')
    single_parser.add_argument('diam_cables', type=float, help='Diameter (mm) of the cables used')
    single_parser.add_argument('current', type=int, help='''Current (A) - PCSN (Portata in corrente
                            in servizio nominale - i.e. current flowing inside the power line''')

    single_parser.add_argument('ph_1_deg', type=float, help='Initial phase (deg) - cable 1')
    single_parser.add_argument('x1', type=float, help='Abscissa (m) of the first cable (1)')
    single_parser.add_argument('y1', type=float, help='Ordinate (m) of the first cable (1)')

    single_parser.add_argument('ph_2_deg', type=float, help='Initial phase (deg) - cable 2')
    single_parser.add_argument('x2', type=float, help='Abscissa (m) of the second cable (2)')
    single_parser.add_argument('y2', type=float, help='Ordinate (m) of the second cable (2)')

    single_parser.add_argument('ph_3_deg', type=float, help='Initial phase (deg) - cable 3')
    single_parser.add_argument('x3', type=float, help='Abscissa (m) of the third cable (3)')
    single_parser.add_argument('y3', type=float, help='Ordinate (m) of the third cable (3)')
    return single_parser


def init_subparser_double(subparsers):
    '''
    Initialization of the subparser "double". Optional and positional arguments are listed in order of entry on the command line.

    Parameters
    -------------------
    subparsers : argparse._SubParsersAction
        A subparser action, it will be populated with a subparser instance.

    Returns
    -------------------
    double_parser : argparse.ArgumentParser
        An instance of a command line arguments parser (subparser in this specific case).
    '''

    # Double triad
    double_parser = subparsers.add_parser('double', help='Calculate the magnetic induction B or the DPA for a double triad of cables',
                                          description='''Positional arguments can be given either manually one by one or using a configuration file (prefix character: @).
                                          Choose an optional argument in order to evaluate something.''')

    # OPTIONAL ARGUMENTS
    double_parser.add_argument('-point', '-p', action='store_true', help='Point estimate of the magnetic induction B in (xp, yp)')
    double_parser.add_argument('-bidim', '-b', action='store_true', help='2D estimate of the magnetic induction B around (xp, yp)')
    double_parser.add_argument('-graph', '-g', action='store_true', help='Graph of the 2D estimate of the magnetic induction B around (xp, yp)')
    double_parser.add_argument('-dpa', '-d', type=float, nargs=1, metavar='lim_val', help='''Estimate of the DPA (distanza di prima approssimazione)
                                                                          for the given configuration at \'lim_val\' microTesla. Suggested lim_values: 3, 10''')
    double_parser.add_argument('-save', '-s', type=str, nargs=2, metavar=('dest', 'filename'), help='Save the output in \'dest\' repository, with \'filename\' denomination')

    # POSITIONAL ARGUMENTS
    double_parser.add_argument('xp', type=float, help='Abscissa (m) of the point of interest')
    double_parser.add_argument('yp', type=float, help='Ordinate (m) of the point of interest')
    double_parser.add_argument('diam_cables', type=float, help='Diameter (mm) of the cables used')

    double_parser.add_argument('A_current', type=int, help='''Current (A) of triad A - PCSN (Portata
            in corrente in servizio nominale - i.e. current flowing inside the power line A''')

    double_parser.add_argument('A_ph_1_deg', type=float, help='Initial phase (deg) - cable 1A')
    double_parser.add_argument('A_x1', type=float, help='Abscissa (m) of the first cable (1A)')
    double_parser.add_argument('A_y1', type=float, help='Ordinate (m) of the first cable (1A)')

    double_parser.add_argument('A_ph_2_deg', type=float, help='Initial phase (deg) - cable 2A')
    double_parser.add_argument('A_x2', type=float, help='Abscissa (m) of the second cable (2A)')
    double_parser.add_argument('A_y2', type=float, help='Ordinate (m) of the second cable (2A)')

    double_parser.add_argument('A_ph_3_deg', type=float, help='Initial phase (deg) - cable 3A')
    double_parser.add_argument('A_x3', type=float, help='Abscissa (m) of the third cable (3A)')
    double_parser.add_argument('A_y3', type=float, help='Ordinate (m) of the third cable (3A)')

    double_parser.add_argument('B_current', type=int, help='''Current (A) of triad B - PCSN (Portata
            in corrente in servizio nominale - i.e. current flowing inside the power line B''')

    double_parser.add_argument('B_ph_1_deg', type=float, help='Initial phase (deg) - cable 1B')
    double_parser.add_argument('B_x1', type=float, help='Abscissa (m) of the first cable (1B)')
    double_parser.add_argument('B_y1', type=float, help='Ordinate (m) of the first cable (1B)')

    double_parser.add_argument('B_ph_2_deg', type=float, help='Initial phase (deg) - cable 2B')
    double_parser.add_argument('B_x2', type=float, help='Abscissa (m) of the second cable (2B)')
    double_parser.add_argument('B_y2', type=float, help='Ordinate (m) of the second cable (2B)')

    double_parser.add_argument('B_ph_3_deg', type=float, help='Initial phase (deg) - cable 3B')
    double_parser.add_argument('B_x3', type=float, help='Abscissa (m) of the third cable (3B)')
    double_parser.add_argument('B_y3', type=float, help='Ordinate (m) of the third cable (3B)')
    return double_parser


def single_args_packaging(args):
    '''
    Packaging of the arguments for a single triad in the wanted fashion. The cables' diameter is transformed from millimeters to meters.

    Parameters
    -------------------
    args : argparse.Namespace
        Namespace object built up from attributes parsed out of the command line.

    Returns
    -------------------
    xp, yp, diam_cables : float
        Abscissa (m) and ordinate (m) of the point of interest.
        Cables' diameter (mm).
    current, cables_array : numpy.ndarray
        Current (A) flowing inside the power line.
        Array containing the phases (deg), abscissas (m) and ordinates (m) of the cables.

    Notes
    -------------------
    NaN values are used in order to mantain the overall numpy array structure similar to the double triad's one, thus exploiting the same "for" loops.
    NaNs are preferable to zeros since in the visualization algorithm NaN values are not plotted automatically.
    '''
    xp, yp = args.xp, args.yp
    diam_cables = args.diam_cables*0.001
    current = np.array([args.current, np.nan])
    cables_array = np.array([[[args.ph_1_deg, args.x1, args.y1],
                              [args.ph_2_deg, args.x2, args.y2],
                              [args.ph_3_deg, args.x3, args.y3]],

                             [[np.nan, np.nan, np.nan],
                              [np.nan, np.nan, np.nan],
                              [np.nan, np.nan, np.nan]]])
    return xp, yp, diam_cables, current, cables_array


def double_args_packaging(args):
    '''
    Packaging of the arguments for a double triad in the wanted fashion. The cables' diameter is transformed from millimeters to meters.

    Parameters
    -------------------
    args : argparse.Namespace
        Namespace object built up from attributes parsed out of the command line.

    Returns
    -------------------
    xp, yp, diam_cables : float
        Abscissa (m) and ordinate (m) of the point of interest.
        Cables' diameter (mm).
    currents, cables_array : numpy.ndarray
        Currents (A) flowing inside the power lines.
        Array containing the phases (deg), abscissas (m) and ordinates (m) of the cables.
    '''
    xp, yp = args.xp, args.yp
    diam_cables = args.diam_cables*0.001
    currents = np.array([args.A_current, args.B_current])
    cables_array = np.array([[[args.A_ph_1_deg, args.A_x1, args.A_y1],
                              [args.A_ph_2_deg, args.A_x2, args.A_y2],
                              [args.A_ph_3_deg, args.A_x3, args.A_y3]],

                             [[args.B_ph_1_deg, args.B_x1, args.B_y1],
                              [args.B_ph_2_deg, args.B_x2, args.B_y2],
                              [args.B_ph_3_deg, args.B_x3, args.B_y3]]])
    return xp, yp, diam_cables, currents, cables_array


def main(argv=None):
    '''
    *COMMAND LINE INTERFACE*

    The function parses the arguments passed by the user through the command line
    providing two options: single or double power line, i.e. three or six cables.

    Depending on the option selected, data are packed in numpy arrays of different
    fashion and the corresponding calculation functions are called.

    The result are:

    - point : the point estimate of the magnetic induction B in (xp, yp);
    - bidim : the 2D estimate of the magnetic induction B around (xp, yp);
    - graph : graphical representation of the 2D estimate of the magnetic induction B around (xp, yp);
    - dpa : estimate of the DPA (distanza di prima approssimazione) for the given configuration at \'lim_val\' microTesla. Suggested lim_values: 3, 10.

    With the 'save' optional argument is possible to save the output in a file (respectively: point, bidim, dpa in .txt and graph in .jpg)
    '''
    parser = init_parser()
    subparsers = parser.add_subparsers(help='Possible cable configurations', dest='subparser')
    init_subparser_single(subparsers)
    init_subparser_double(subparsers)

    args = parser.parse_args(argv) #args is a namespace

    if args.subparser == 'single':
        xp, yp, diam_cables, current_s, cables_array = single_args_packaging(args)
    elif args.subparser == 'double':
        xp, yp, diam_cables, current_s, cables_array = double_args_packaging(args)

    main_print_point_bidim_dpa(current_s, xp, yp, diam_cables, cables_array, args)
    if args.save:
        save_output_txt(args.save[0], args.save[1], current_s, xp, yp, diam_cables, cables_array, args)

    if args.graph:
        output_figure = main_graph(current_s, xp, yp, diam_cables, cables_array, args.subparser)
        if args.save:
            save_output_jpg(args.save[0], args.save[1], output_figure)


#Command line entry point
if __name__ == '__main__':
    main()
