import math
import cmath
import numpy as np


#Recall all the constants needed in the program
pi = math.pi
mu_zero = 1.25663706212 * 10**(-6)


def calc_phasors(I, xp, yp, ph_n_deg, xn, yn):
    '''
    calc_phasors(I, xp, yp, ph_n_deg, xn, yn)

    It calculates the phasors of the x and y components of the magnetic induction field B in a given point for a given cable.

    -------------------
    Parameters
    -------------------
    I : int
        Current (A) circulating inside the considered power line (composed of a triad of cables)
    xp, yp : float
        Abscissa and ordinate of the point of interest where the magnetic induction field B will be calculated at last
    ph_n_deg : float
        Current phase belonging to the n-th cable under consideration
    xn, yn : float
        Abscissa and ordinate of the n-th cable under consideration
    -------------------
    Returns
    -------------------
    phasors_n : numpy matrix 2x2
        DESCRIZIONE
    '''
    ph_n_rad = math.radians(ph_n_deg)
    I_complex = cmath.rect(I, ph_n_rad)
    I_components = np.array([I_complex.real, I_complex.imag])
    coef = (mu_zero / (2*pi)) / ((xp - xn)**2 + (yp - yn)**2)
    transfer_fn_n = np.array([(yn - yp) * coef, (xp - xn) * coef]).reshape(2,1)
    phasors_n = I_components * transfer_fn_n
    return phasors_n

#A function that will work on a single triad
def calc_B_effective(*phasors):
    '''
    Returns the effective value of the magnetic induction B in microTesla in a given point (xp, yp), considering all the cables provided.

    esempio di doc:
    *args : tuple
        Additional arguments should be passed as keyword arguments
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

