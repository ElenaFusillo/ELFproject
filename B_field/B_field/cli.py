from argparse import ArgumentParser
from .calculations import main_single, main_double

def main():
    parser = ArgumentParser(prog='B_field',
                            usage='%(prog)s [options] path',
                            description='Evaluation of effective magnetic induction B in a given point (xp, yp), due to single or double triad of cables.',
                            fromfile_prefix_chars='@')
    subparsers = parser.add_subparsers(help='Possible cable configurations', dest='subparser')

    #Single triad
    single_parser = subparsers.add_parser('single', help='Calculate the magnetic induction B for a single triad of cables')
    
    single_parser.add_argument('xp', type = float, help='Abscissa of the point of interest')
    single_parser.add_argument('yp', type = float, help='Ordinate of the point of interest')
    single_parser.add_argument('I', type = int, help='Current (A) - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line')

    single_parser.add_argument('ph_1_deg', type = float, help='Initial phase (deg) - cable 1')
    single_parser.add_argument('x1', type = float, help='Abscissa of the first cable (1)')
    single_parser.add_argument('y1', type = float, help='Ordinate of the first cable (1)')

    single_parser.add_argument('ph_2_deg', type = float, help='Initial phase (deg) - cable 2')
    single_parser.add_argument('x2', type = float, help='Abscissa of the second cable (2)')
    single_parser.add_argument('y2', type = float, help='Ordinate of the second cable (2)')

    single_parser.add_argument('ph_3_deg', type = float, help='Initial phase (deg) - cable 3')
    single_parser.add_argument('x3', type = float, help='Abscissa of the third cable (3)')
    single_parser.add_argument('y3', type = float, help='Ordinate of the third cable (3)')

    #Double triad
    double_parser = subparsers.add_parser('double', help='Calculate the magnetic induction B for a double triad of cables')
    
    double_parser.add_argument('xp', type = float, help='Abscissa of the point of interest')
    double_parser.add_argument('yp', type = float, help='Ordinate of the point of interest')
    
    double_parser.add_argument('A_I', type = int, help='Current (A) of triad A - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line A')

    double_parser.add_argument('A_ph_1_deg', type = float, help='Initial phase (deg) - cable 1A')
    double_parser.add_argument('A_x1', type = float, help='Abscissa of the first cable (1A)')
    double_parser.add_argument('A_y1', type = float, help='Ordinate of the first cable (1A)')

    double_parser.add_argument('A_ph_2_deg', type = float, help='Initial phase (deg) - cable 2A')
    double_parser.add_argument('A_x2', type = float, help='Abscissa of the second cable (2A)')
    double_parser.add_argument('A_y2', type = float, help='Ordinate of the second cable (2A)')

    double_parser.add_argument('A_ph_3_deg', type = float, help='Initial phase (deg) - cable 3A')
    double_parser.add_argument('A_x3', type = float, help='Abscissa of the third cable (3A)')
    double_parser.add_argument('A_y3', type = float, help='Ordinate of the third cable (3A)')

    double_parser.add_argument('B_I', type = int, help='Current (A) of triad B - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line B')

    double_parser.add_argument('B_ph_1_deg', type = float, help='Initial phase (deg) - cable 1B')
    double_parser.add_argument('B_x1', type = float, help='Abscissa of the first cable (1B)')
    double_parser.add_argument('B_y1', type = float, help='Ordinate of the first cable (1B)')

    double_parser.add_argument('B_ph_2_deg', type = float, help='Initial phase (deg) - cable 2B')
    double_parser.add_argument('B_x2', type = float, help='Abscissa of the second cable (2B)')
    double_parser.add_argument('B_y2', type = float, help='Ordinate of the second cable (2B)')

    double_parser.add_argument('B_ph_3_deg', type = float, help='Initial phase (deg) - cable 3B')
    double_parser.add_argument('B_x3', type = float, help='Abscissa of the third cable (3B)')
    double_parser.add_argument('B_y3', type = float, help='Ordinate of the third cable (3B)')

    args = parser.parse_args()

    if args.subparser == 'single':
        main_single(args)
    if args.subparser == 'double':
        main_double(args)

if __name__ == '__main__':
    main()
