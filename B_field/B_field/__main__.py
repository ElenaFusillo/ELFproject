import argparse
import math
import cmath
import numpy as np

#Recall all the constants needed in the program
pi = math.pi
mu_zero = 1.25663706212 * 10**(-6)

#A function that will work on each cable
def calc_phasors(I, xp, yp, ph_n_deg, xn, yn):
    '''
    Returns the phasors of the components x and y of the magnetic induction B in a given point (xp, yp) for a given cable
    Return value: np.matrix 2x2
    '''
    ph_n_rad = math.radians(ph_n_deg)
    I_complex = cmath.rect(I, ph_n_rad)
    I_components = np.array([I_complex.real, I_complex.imag])
    coef = (mu_zero / (2*pi)) / ((xp - xn)**2 + (yp - yn)**2)
    trans_fn_n = np.array([(yn - yp) * coef, (xp - xn) * coef]).reshape(2,1)
    phasors_n = I_components * trans_fn_n
    return phasors_n

#A function that will work on a single triad
def calc_B_effective(*phasors):
    '''
    Returns the effective value of the magnetic induction B in microTesla in a given point (xp, yp), considering all the cables provided.
    '''
    B_comp = 0
    for phasor in phasors:
        B_comp += phasor
    sum_B_comp = np.sum(B_comp**2)
    B_effective = math.sqrt(sum_B_comp)*10**(6)
    return B_effective

def main_single(args):
    phasors_1 = calc_phasors(args.I, args.xp, args.yp, args.ph_1_deg, args.x1, args.y1)
    phasors_2 = calc_phasors(args.I, args.xp, args.yp, args.ph_2_deg, args.x2, args.y2)
    phasors_3 = calc_phasors(args.I, args.xp, args.yp, args.ph_3_deg, args.x3, args.y3)
    
    B_eff = calc_B_effective(phasors_1, phasors_2, phasors_3)
    
    print('In point of coordinates (', args.xp, ',', args.yp, '), the magnetic induction is ', round(B_eff,2), ' microTesla.')


def main_double(args):
    phasors_1_A = calc_phasors(args.A_I, args.xp, args.yp, args.A_ph_1_deg, args.A_x1, args.A_y1)
    phasors_2_A= calc_phasors(args.A_I, args.xp, args.yp, args.A_ph_2_deg, args.A_x2, args.A_y2)
    phasors_3_A = calc_phasors(args.A_I, args.xp, args.yp, args.A_ph_3_deg, args.A_x3, args.A_y3)

    phasors_1_B = calc_phasors(args.B_I, args.xp, args.yp, args.B_ph_1_deg, args.B_x1, args.B_y1)
    phasors_2_B = calc_phasors(args.B_I, args.xp, args.yp, args.B_ph_2_deg, args.B_x2, args.B_y2)
    phasors_3_B = calc_phasors(args.B_I, args.xp, args.yp, args.B_ph_3_deg, args.B_x3, args.B_y3)
    
    B_eff = calc_B_effective(phasors_1_A, phasors_2_A, phasors_3_A, phasors_1_B, phasors_2_B, phasors_3_B)
    
    print('In point of coordinates (', args.xp, ',', args.yp, '), the magnetic induction is ', round(B_eff,2), ' microTesla.')    

def main():
    parser = argparse.ArgumentParser(prog='B_field',
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
