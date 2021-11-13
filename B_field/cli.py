from argparse import ArgumentParser

import numpy as np

from .calculations import main_double, main_grid, main_single


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
                         version = f"{parser.prog} version 0.1.0.dev1")
    return parser


def init_subparser_single(subparsers):
    '''
    Initialization of the subparser "single".
    '''

    #Single triad
    single_parser = subparsers.add_parser('single', help='''Calculate the magnetic induction B
                                            for a single triad of cables''')

    single_parser.add_argument('xp', type=float, help='Abscissa of the point of interest')
    single_parser.add_argument('yp', type=float, help='Ordinate of the point of interest')
    single_parser.add_argument('I', type=int, help='''Current (A) - PCSN (Portata in corrente
                            in servizio nominale - i.e. current flowing inside the power line''')

    single_parser.add_argument('ph_1_deg', type=float, help='Initial phase (deg) - cable 1')
    single_parser.add_argument('x1', type=float, help='Abscissa of the first cable (1)')
    single_parser.add_argument('y1', type=float, help='Ordinate of the first cable (1)')

    single_parser.add_argument('ph_2_deg', type=float, help='Initial phase (deg) - cable 2')
    single_parser.add_argument('x2', type=float, help='Abscissa of the second cable (2)')
    single_parser.add_argument('y2', type=float, help='Ordinate of the second cable (2)')

    single_parser.add_argument('ph_3_deg', type=float, help='Initial phase (deg) - cable 3')
    single_parser.add_argument('x3', type=float, help='Abscissa of the third cable (3)')
    single_parser.add_argument('y3', type=float, help='Ordinate of the third cable (3)')
    return single_parser


def init_subparser_double(subparsers):
    '''
    Initialization of the subparser "double".
    '''

    #Double triad
    double_parser = subparsers.add_parser('double', help='''Calculate the magnetic induction B
                                                        for a double triad of cables''')

    double_parser.add_argument('xp', type=float, help='Abscissa of the point of interest')
    double_parser.add_argument('yp', type=float, help='Ordinate of the point of interest')

    double_parser.add_argument('A_I', type=int, help='''Current (A) of triad A - PCSN (Portata
            in corrente in servizio nominale - i.e. current flowing inside the power line A''')

    double_parser.add_argument('A_ph_1_deg', type=float, help='Initial phase (deg) - cable 1A')
    double_parser.add_argument('A_x1', type=float, help='Abscissa of the first cable (1A)')
    double_parser.add_argument('A_y1', type=float, help='Ordinate of the first cable (1A)')

    double_parser.add_argument('A_ph_2_deg', type=float, help='Initial phase (deg) - cable 2A')
    double_parser.add_argument('A_x2', type=float, help='Abscissa of the second cable (2A)')
    double_parser.add_argument('A_y2', type=float, help='Ordinate of the second cable (2A)')

    double_parser.add_argument('A_ph_3_deg', type=float, help='Initial phase (deg) - cable 3A')
    double_parser.add_argument('A_x3', type=float, help='Abscissa of the third cable (3A)')
    double_parser.add_argument('A_y3', type=float, help='Ordinate of the third cable (3A)')

    double_parser.add_argument('B_I', type=int, help='''Current (A) of triad B - PCSN (Portata
            in corrente in servizio nominale - i.e. current flowing inside the power line B''')

    double_parser.add_argument('B_ph_1_deg', type=float, help='Initial phase (deg) - cable 1B')
    double_parser.add_argument('B_x1', type=float, help='Abscissa of the first cable (1B)')
    double_parser.add_argument('B_y1', type=float, help='Ordinate of the first cable (1B)')

    double_parser.add_argument('B_ph_2_deg', type=float, help='Initial phase (deg) - cable 2B')
    double_parser.add_argument('B_x2', type=float, help='Abscissa of the second cable (2B)')
    double_parser.add_argument('B_y2', type=float, help='Ordinate of the second cable (2B)')

    double_parser.add_argument('B_ph_3_deg', type=float, help='Initial phase (deg) - cable 3B')
    double_parser.add_argument('B_x3', type=float, help='Abscissa of the third cable (3B)')
    double_parser.add_argument('B_y3', type=float, help='Ordinate of the third cable (3B)')
    return double_parser


def single_args_packaging(args):
    '''
    Packaging of the arguments for a single triad in the wanted fashion.
    '''
    I = args.I
    cables_array = np.array([[args.ph_1_deg, args.x1, args.y1],
                             [args.ph_2_deg, args.x2, args.y2],
                             [args.ph_3_deg, args.x3, args.y3]])
    return I, cables_array


def double_args_packaging(args):
    '''
    Packaging of the arguments for a double triad in the wanted fashion.
    '''
    II = np.array([args.A_I, args.B_I])
    cables_array = np.array([[[args.A_ph_1_deg, args.A_x1, args.A_y1],
                              [args.A_ph_2_deg, args.A_x2, args.A_y2],
                              [args.A_ph_3_deg, args.A_x3, args.A_y3]],

                             [[args.B_ph_1_deg, args.B_x1, args.B_y1],
                              [args.B_ph_2_deg, args.B_x2, args.B_y2],
                              [args.B_ph_3_deg, args.B_x3, args.B_y3]]])
    return II, cables_array


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
        I, cables_array = single_args_packaging(args)
        #single point
        main_single(I, args.xp, args.yp, cables_array)
        #2D grid
        single_grid = main_grid(args.I, args.xp, args.yp, cables_array, args.subparser)
        print('-----Grid of B field values (microTesla)-------\n', single_grid[2].round(2))

    if args.subparser == 'double':
        II, cables_array = double_args_packaging(args)
        #single point
        main_double(II, args.xp, args.yp, cables_array)
        #2D grid
        double_grid = main_grid(II, args.xp, args.yp, cables_array, args.subparser)
        print('-----Grid of B field values (microTesla)-------\n', double_grid[2].round(2))


#Command line entry point
if __name__ == '__main__':
    main()
