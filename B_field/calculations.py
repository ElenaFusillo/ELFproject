import math
import cmath
import numpy as np


#Recall all the constants needed in the program
PI = math.pi
MU_ZERO = 1.25663706212 * 10**(-6)


def calc_B_phasors(I, xp, yp, cable_array):

    """It calculates the phasors of the x and y components of the
    magnetic induction field B in a given point for a given cable.

    Given the input, the function rectifies the current phase
    extracting respectively the real and imaginary part of it.
    Then, both real and imaginary part of x and y components are
    multiplied by a transfer function (dependent on the spatial
    disposition of the cable in respect to the point of interest)
    resulting in the magnetic inductin B phasor components of a
    single cable.

    Parameters
    -------------------
    I : int
        Current (A) circulating inside the considered power line
        (composed of a triad of cables)
    xp, yp : float
        Abscissa and ordinate of the point of interest where the
        magnetic induction field B will be calculated at last
    cable_array : numpy array
        First column - Current phase belonging to the n-th cable under consideration
        Second and third columns - Abscissa and ordinate of the n-th cable under consideration

    Returns
    -------------------
    B_phasors_n : numpy array 2x2
        Respectively the real and imaginary part (columns) of the
        x and y components (rows) of the magnetic induction field B
        produced by a single cable in a given point

    Notes
    -------------------
    The current function implements the calculations present both in
    [1]_"Norma Italiana CEI 106-11" formulas (5) and [2]_"Norma Italiana
    CEI 211-4" formulas (16).

    References
    -------------------
    ..[1] Norma Italiana CEI 106-11, "Guide for the determination of
    the respect widths for power lines and substations according to
    DPCM 8 July 2003 (Clause 6) - Part 1: Overhead lines and cables",
    first edition, 2006-02.
    ..[2] Norma Italiana CEI 211-4, "Guide to calculation methods of
    electric and magnetic fields generated by power-lines and electrical
    substations", second edition, 2008-09.
    """

    ph_n_rad = math.radians(cable_array[0])
    I_complex = cmath.rect(I, ph_n_rad)
    I_components = np.array([I_complex.real, I_complex.imag])
    coef = (MU_ZERO / (2*PI)) / ((xp - cable_array[1])**2 + (yp - cable_array[2])**2)
    transfer_fn_n = np.array([(cable_array[2] - yp) * coef, (xp - cable_array[1]) * coef]).reshape(2, 1)
    B_phasors_n = I_components * transfer_fn_n
    return B_phasors_n


def calc_B_effective(*B_phasors):

    """It calculates the effective value of the magnetic induction field B
    (microTesla) in a given point, considering the magnetic induction of
    all the cables provided.

    Firstly, the function computes the resulting real and imaginary parts
    of the x and y magnetic induction field components considering all the
    contributing cables given as input (typically three or six cables).
    The 'B_components' 2x2 numpy matrix indicates this intermediate step.

    Secondly, the module of the effective magnetic induction field B is
    calculated as the squared root of the sum of the squares of the
    components mentioned above.

    Lastly, the result is transformed from Tesla units to micro Tesla units.

    Parameters
    -------------------
    *B_phasors : numpy array 2x2
        Respectively the real and imaginary part (columns) of the
        x and y components (rows) of the magnetic induction field B
        produced by a single cable in a given point

    Returns
    -------------------
    B_effective_microT : float
        Effective magnetic induction field B (microTesla) calculated in the given point

    Notes
    -------------------
    The current function implements the calculations present both in
    [1]_"Norma Italiana CEI 106-11" formulas (3-4) and [2]_"Norma Italiana
    CEI 211-4" formulas (17).

    References
    -------------------
    ..[1] Norma Italiana CEI 106-11, "Guide for the determination of
    the respect widths for power lines and substations according to
    DPCM 8 July 2003 (Clause 6) - Part 1: Overhead lines and cables",
    first edition, 2006-02.
    ..[2] Norma Italiana CEI 211-4, "Guide to calculation methods of
    electric and magnetic fields generated by power-lines and electrical
    substations", second edition, 2008-09.
    """

    B_components = 0
    for B_phasor in B_phasors:
        B_components += B_phasor
    B_effective_T = math.sqrt(np.sum(B_components**2))
    B_effective_microT = B_effective_T*10**(6)
    return B_effective_microT


def main_single(I, xp, yp, cables_array):
    """Given a single triad of cables (one power line), the function
    computes its effective magnetic induction B in a given point.

    The respective phasors of the magnetic induction B of each cable
    are iteratively computed and then composed to obtain the result.

    Parameters
    -------------------
    I : int
        Current (A) circulating inside the considered power line
        (composed of a triad of cables)
    xp, yp : float
        Abscissa and ordinate of the point of interest where the
        magnetic induction field B will be calculated at last
    cable_array : numpy array
        First column - Current phase belonging to the n-th cable under consideration
        Second and third columns - Abscissa and ordinate of the n-th cable under consideration

    Returns
    -------------------
    B_eff : float
        Effective magnetic induction field B (microTesla) calculated in the given point
    """

    B_phasors_cables = np.zeros((3, 2, 2)) #3 sets, 2 row each, 2 columns each
    for i in range(3):
        B_phasors_cables[i,] = calc_B_phasors(I, xp, yp, cables_array[i,])
    B_eff = calc_B_effective(B_phasors_cables[0,], B_phasors_cables[1,], B_phasors_cables[2,])
    return B_eff


def main_double(II, xp, yp, cables_array):
    """Given two triads of cables (two power lines), the function computes
    their composed effective magnetic induction B in a given point.

    The respective phasors of the magnetic induction B of each cable
    are iteratively computed and then composed to obtain the result.

    Parameters
    -------------------
    II : numpy array
        Current (A) circulating inside the considered power lines
        (each one composed of a triad of cables)
    xp, yp : float
        Abscissa and ordinate of the point of interest where the
        magnetic induction field B will be calculated at last
    cable_array : numpy array
        First column - Current phase belonging to the n-th cable under consideration
        Second and third columns - Abscissa and ordinate of the n-th cable under consideration

    Returns
    -------------------
    B_eff : float
        Effective magnetic induction field B (microTesla) calculated in the given point
    """

    B_phasors_cables = np.zeros((2, 3, 2, 2))
    #2 super-sets (two triads), 3 sets (three cables each), 2 row each, 2 columns each
    for j in range(2):
        for i in range(3):
            B_phasors_cables[j, i,] = calc_B_phasors(II[j], xp, yp, cables_array[j, i,])
    B_eff = calc_B_effective(B_phasors_cables[0, 0, ], B_phasors_cables[0, 1, ], B_phasors_cables[0, 2, ],
                             B_phasors_cables[1, 0, ], B_phasors_cables[1, 1, ], B_phasors_cables[1, 2, ],)
    return B_eff


def main_grid(I_or_II, xp, yp, cables_array, subparser_type):
    '''
    TODO docstring
    '''
    nx, ny = ((9, 9))
    x = np.linspace(xp-2, xp+2, nx)
    y = np.linspace(yp-2, yp+2, ny)
    z_grid = np.zeros((nx, ny))
    xx, yy = np.meshgrid(x, y, sparse=True)
    if subparser_type == 'single':
        for i in range(nx):
            for j in range(ny):
                z_grid[i, j] = main_single(I_or_II, xx[0, i], yy[j, 0], cables_array)
    else:
        for i in range(nx):
            for j in range(ny):
                z_grid[i, j] = main_double(I_or_II, xx[0, i], yy[j, 0], cables_array)
    return x, y, z_grid
