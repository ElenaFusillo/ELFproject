import argparse as ap
#import math

#import matplotlib.pylab as plt
#import numpy as np
#from numpy.core.fromnumeric import partition
#import pandas as pd

parser = ap.ArgumentParser(prog='B_field',
                            usage='%(prog)s [options] path',
                            description='Evaluation of magnetic induction B',
                            fromfile_prefix_chars='@')

parser.add_argument('I',
                    help='Current (A) - PCSN (Portata in corrente in servizio nominale - i.e. current flowing inside the power line')

parser.add_argument('ph_1_deg',
                    help='Initial phase (deg) - cable 1')
parser.add_argument('x1',
                    help='Abscissa of the first cable (1)')
parser.add_argument('y1',
                    help='Ordinate of the first cable (1)')

parser.add_argument('ph_2_deg',
                    help='Initial phase (deg) - cable 2')
parser.add_argument('x2',
                    help='Abscissa of the second cable (2)')
parser.add_argument('y2',
                    help='Ordinate of the first cable (1)')

parser.add_argument('ph_3_deg',
                    help='Initial phase (deg) - cable 3')
parser.add_argument('x3',
                    help='Abscissa of the third cable (3)')
parser.add_argument('y3',
                    help='Ordinate of the first cable (1)')

parser.add_argument('xp',
                    help='Abscissa of the point of interest')
parser.add_argument('yp',
                    help='Ordinate of the point of interest')


#Execute parse_args()
args = parser.parse_args()

print('If you read this line it means that you have provided '
      'all the parameters')

