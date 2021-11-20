from argparse import ArgumentParser

import numpy as np

from .calculations import main_double, main_grid, main_single
from .graphics import main_graphics

def init_parser():
    '''
    Initialization of the argument parser.
    '''
    parser = ArgumentParser(prog='B_field',
                            usage='%(prog)s [options] path',
                            description='''Evaluation of effective magnetic induction B in a
                            given point (xp, yp), due to single or double triad of cables.''',
                            fromfile_prefix_chars='@')
    parser.add_argument("-v", "--version", action="version",
                        version=f"{parser.prog} version 0.1.0.dev1")
    return parser


def init_subparser_single(subparsers):
    '''
    Initialization of the subparser "single".
    '''

    #Single triad
    single_parser = subparsers.add_parser('single', help='''Calculate the magnetic induction B
                                            for a single triad of cables''')

    # OPTIONAL ARGUMENTS
    single_parser.add_argument('-point', '-p', action='store_true', help='Point estimate of the magnetic induction B in (xp, yp)')
    single_parser.add_argument('-bidim', '-b', action='store_true', help='2D estimate of the magnetic induction B around (xp, yp)')
    single_parser.add_argument('-graph', '-g', action='store_true', help='Graph of the trellis and the point of interest (xp, yp)')
    single_parser.add_argument('-dpa', '-d', action='store_true', help='Estimate of the DPA (distanza di prima approssimazione) for the given configuration')

    # POSITIONAL ARGUMENTS
    single_parser.add_argument('xp', type=float, help='Abscissa (m) of the point of interest')
    single_parser.add_argument('yp', type=float, help='Ordinate (m) of the point of interest')
    single_parser.add_argument('diam_cables', type=float, help='Diameter (mm) of the cables used')
    single_parser.add_argument('I', type=int, help='''Current (A) - PCSN (Portata in corrente
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
    Initialization of the subparser "double".
    '''

    #Double triad
    double_parser = subparsers.add_parser('double', help='''Calculate the magnetic induction B
                                                        for a double triad of cables''')

    # OPTIONAL ARGUMENTS
    double_parser.add_argument('-point', '-p', action='store_true', help='Point estimate of the magnetic induction B in (xp, yp)')
    double_parser.add_argument('-bidim', '-b', action='store_true', help='2D estimate of the magnetic induction B around (xp, yp)')
    double_parser.add_argument('-graph', '-g', action='store_true', help='Graph of the trellis and the point of interest (xp, yp)')
    double_parser.add_argument('-dpa', '-d', action='store_true', help='Estimate of the DPA (distanza di prima approssimazione) for the given configuration')

    # POSITIONAL ARGUMENTS
    double_parser.add_argument('xp', type=float, help='Abscissa (m) of the point of interest')
    double_parser.add_argument('yp', type=float, help='Ordinate (m) of the point of interest')
    double_parser.add_argument('diam_cables', type=float, help='Diameter (mm) of the cables used')

    double_parser.add_argument('A_I', type=int, help='''Current (A) of triad A - PCSN (Portata
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

    double_parser.add_argument('B_I', type=int, help='''Current (A) of triad B - PCSN (Portata
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
    Packaging of the arguments for a single triad in the wanted fashion.
    '''
    xp, yp = args.xp, args.yp
    #diameter: from millimeters to meters
    diam_cables = args.diam_cables*0.001
    I = args.I
    cables_array = np.array([[args.ph_1_deg, args.x1, args.y1],
                             [args.ph_2_deg, args.x2, args.y2],
                             [args.ph_3_deg, args.x3, args.y3]])
    return xp, yp, diam_cables, I, cables_array


def double_args_packaging(args):
    '''
    Packaging of the arguments for a double triad in the wanted fashion.
    '''
    xp, yp = args.xp, args.yp
    #diameter: from millimeters to meters
    diam_cables = args.diam_cables*0.001
    II = np.array([args.A_I, args.B_I])
    cables_array = np.array([[[args.A_ph_1_deg, args.A_x1, args.A_y1],
                              [args.A_ph_2_deg, args.A_x2, args.A_y2],
                              [args.A_ph_3_deg, args.A_x3, args.A_y3]],

                             [[args.B_ph_1_deg, args.B_x1, args.B_y1],
                              [args.B_ph_2_deg, args.B_x2, args.B_y2],
                              [args.B_ph_3_deg, args.B_x3, args.B_y3]]])
    return xp, yp, diam_cables, II, cables_array


def main(argv=None):
    '''
    *COMMAND LINE INTERFACE*

    The function parses the arguments passed by the user through the command line
    providing two options: single or double power line, i.e. three or six cables.

    Depending on the option selected, data are packed in numpy arrays of different
    fashion and the corresponding calculation functions are called.

    The result is the effective magnetic induction field B (microTesla) generated
    by the power line/lines calculated in the given point.
    '''
    parser = init_parser()
    subparsers = parser.add_subparsers(help='Possible cable configurations', dest='subparser')
    init_subparser_single(subparsers)
    init_subparser_double(subparsers)

    args = parser.parse_args(argv)

    if args.subparser == 'single':
        xp, yp, diam_cables, I, cables_array = single_args_packaging(args)

        if args.point:
            single_point = main_single(I, xp, yp, diam_cables, cables_array)
            print('\nIn point of coordinates (', xp, ',', yp, '), the magnetic induction is ', round(single_point, 2), ' microTesla.\n')

        if args.bidim:
            single_grid = main_grid(I, xp, yp, diam_cables, cables_array, args.subparser)
            print('''\n------Grid of B field values (microTesla)------\n----Point of interest in the matrix center-----\n\n''', np.flipud(single_grid[2]))
            # with the flip up down you see the matrix as if it was a xy grid
        
        if args.graph:
            single_grid = main_grid(I, xp, yp, diam_cables, cables_array, args.subparser)
            main_graphics(single_grid[0], single_grid[1], single_grid[2], xp, yp, cables_array, args.subparser)

        if args.dpa:
            #TODO
            return True

    if args.subparser == 'double':
        xp, yp, diam_cables, II, cables_array = double_args_packaging(args)

        if args.point:
            double_point = main_double(II, xp, yp, diam_cables, cables_array)
            print('\nIn point of coordinates (', xp, ',', yp, '), the magnetic induction is ', round(double_point, 2), ' microTesla.\n')

        if args.bidim:
            double_grid = main_grid(II, xp, yp, diam_cables, cables_array, args.subparser)
            print('''\n------Grid of B field values (microTesla)------\n----Point of interest in the matrix center-----\n\n''', np.flipud(double_grid[2]))
            # with the flip up down you see the matrix as if it was a xy grid

        if args.graph:
            double_grid = main_grid(II, xp, yp, diam_cables, cables_array, args.subparser)
            main_graphics(double_grid[0], double_grid[1], double_grid[2], xp, yp, cables_array, args.subparser)

        if args.dpa:
            #TODO
            return True


#Command line entry point
if __name__ == '__main__':
    main()
