import argparse
import math
import cmath
import numpy as np

parser = argparse.ArgumentParser(prog='B_field',
                            usage='%(prog)s [options] path',
                            description='Evaluation of effective magnetic induction B in a given point (xp, yp), due to single or double triad of cables.',
                            fromfile_prefix_chars='@')

parser.add_argument('xp', type = float,
                    help='Abscissa of the point of interest')
parser.add_argument('yp', type = float,
                    help='Ordinate of the point of interest')
parser.add_argument('I', type = int,
                    help='Current (A) - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line')

parser.add_argument('ph_1_deg', type = float,
                    help='Initial phase (deg) - cable 1')
parser.add_argument('x1', type = float,
                    help='Abscissa of the first cable (1)')
parser.add_argument('y1', type = float,
                    help='Ordinate of the first cable (1)')

parser.add_argument('ph_2_deg', type = float,
                    help='Initial phase (deg) - cable 2')
parser.add_argument('x2', type = float,
                    help='Abscissa of the second cable (2)')
parser.add_argument('y2', type = float,
                    help='Ordinate of the first cable (1)')

parser.add_argument('ph_3_deg', type = float,
                    help='Initial phase (deg) - cable 3')
parser.add_argument('x3', type = float,
                    help='Abscissa of the third cable (3)')
parser.add_argument('y3', type = float,
                    help='Ordinate of the first cable (1)')

#Execute parse_args()
args = parser.parse_args()

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

def calc_B_effective(phasors_1, phasors_2, phasors_3):
      '''
      Returns the effective value of the magnetic induction B in microTesla in a given point (xp, yp), considering a triad of cables
      '''
      B_comp = phasors_1 + phasors_2 + phasors_3
      sum_B_comp = np.sum(B_comp**2)
      B_effective = math.sqrt(sum_B_comp)*10**(6)
      return B_effective

phasors_1 = calc_phasors(args.I, args.xp, args.yp, args.ph_1_deg, args.x1, args.y1)
phasors_2 = calc_phasors(args.I, args.xp, args.yp, args.ph_2_deg, args.x2, args.y2)
phasors_3 = calc_phasors(args.I, args.xp, args.yp, args.ph_3_deg, args.x3, args.y3)

B_eff = calc_B_effective(phasors_1, phasors_2, phasors_3)

print('In point of coordinates (', args.xp, ',', args.yp, '), the magnetic induction is ', round(B_eff,2), ' microTesla.')