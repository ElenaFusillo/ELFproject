#This file contains all the fixtures needed for the tests.
#In such way, it is possible to use them among different files containing tests.

import pytest
import numpy as np

@pytest.fixture
def eg_input_OH():
    '''
    Overhead configuration A1 - single triad - INPUT
    '''
    current = 870
    xp = -20.5
    yp = 1
    cable_array = np.array([[330, -3.75, 6.3], [210, 3.2, 8.3], [90, -3.05, 10.3]])
    return current, xp, yp, cable_array

@pytest.fixture
def eg_output_B_phasors_OH():
    '''
    Overhead configuration A1 - single cable (4-330°) - OUTPUT B PHASORS
    '''
    expected_output = np.array([float(2.58753332e-6), float(-1.49391306e-6), float(-8.17758172e-6), float(4.72132901e-6)]).reshape(2, 2)
    return expected_output

@pytest.fixture
def eg_input_UG():
    '''
    Underground configuration A14 - single triad - INPUT
    '''
    current = 1110
    xp = 5.1
    yp = -1.5
    cable_array = np.array([[330, -0.2, -1.5], [210, 0, -1.5], [90, 0.2, -1.5]])
    return current, xp, yp, cable_array

@pytest.fixture
def eg_output_B_phasors_UG():
    '''
    Underground configuration A14 - single cable (4-330°) - OUTPUT B PHASORS
    '''
    expected_output = np.array([0, 0, float(3.62750264e-05), float(-2.09433962e-05)]).reshape(2, 2)
    return expected_output

@pytest.fixture
def eg_input_B_eff_single_OH():
    '''
    Overhead configuration A1 - single triad - INPUT
    '''
    expected_input_1 = np.array([float(2.58753332e-06), float(-1.49391306e-06), float(-8.17758172e-06), float(4.72132901e-06)]).reshape(2, 2)
    expected_input_2 = np.array([float(-1.78871747e-06), float(-1.03271651e-06), float(5.80720603e-06), float(3.35279196e-06)]).reshape(2, 2)
    expected_input_3 = np.array([float(2.53422182e-22), float(4.13869831e-06), float(-4.75507213e-22), float(-7.76562211e-06)]).reshape(2, 2)
    return expected_input_1, expected_input_2, expected_input_3

@pytest.fixture
def eg_output_B_eff_single_OH():
    '''
    Overhead configuration A1 - single triad - OUTPUT
    '''
    B_eff = 2.991776205053418
    return B_eff

@pytest.fixture
def eg_input_double_OH():
    '''
    Overhead configuration A9 - double triad - INPUT
    '''
    currents = np.array([870, 870])
    xp = -5
    yp = 1
    cables_array = np.array([[[330, -4.0, 6.3],
                              [210, -3.6, 11.6],
                              [90, -3.2, 16.3]],

                             [[330, 4.0, 6.3],
                              [210, 3.6, 11.6],
                              [90, 3.2, 16.3]]])
    return currents, xp, yp, cables_array

@pytest.fixture
def eg_input_B_eff_double_OH():
    '''
    Overhead configuration A9 - double triad - INPUT
    '''
    expected_input_1 = np.array([float(2.74544045e-05), float(-1.58508078e-05), float(-5.18007633e-06), float(2.99071846e-06)]).reshape(2, 2)
    expected_input_2 = np.array([float(-1.39721593e-05), float(-8.06682996e-06), float(1.84537954e-06), float(1.06543037e-06)]).reshape(2, 2)
    expected_input_3 = np.array([float(6.86861061e-22), float(1.12172924e-05), float(-8.08071836e-23), float(-1.31968146e-06)]).reshape(2, 2)
    expected_input_4 = np.array([float(7.32100676e-06), float(-4.22678523e-06), float(-1.24318983e-05), float(7.17755982e-06)]).reshape(2, 2)
    expected_input_5 = np.array([float(-8.57287063e-06), float(-4.94954917e-06), float(6.95534787e-06), float(4.01567196e-06)]).reshape(2, 2)
    expected_input_6 = np.array([float(5.40977452e-22), float(8.83483225e-06), float(-2.89935628e-22), float(-4.73500813e-06)]).reshape(2, 2)
    return expected_input_1, expected_input_2, expected_input_3, expected_input_4, expected_input_5, expected_input_6

@pytest.fixture
def eg_output_B_eff_double_OH():
    '''
    Overhead configuration A9 - double triad - OUTPUT
    '''
    B_eff = 21.95113745163136
    return B_eff

@pytest.fixture
def eg_input_B_eff_UG():
    '''
    Underground configuration A14 - INPUT
    '''
    expected_input_1 = np.array([0, 0, float(3.62750264e-05), float(-2.09433962e-05)]).reshape(2, 2)
    expected_input_2 = np.array([0, 0, float(-3.76975764e-05), float(-2.17647059e-05)]).reshape(2, 2)
    expected_input_3 = np.array([0, 0, float(2.77419989e-21), float(4.53061225e-05)]).reshape(2, 2)
    return expected_input_1, expected_input_2, expected_input_3

@pytest.fixture
def eg_output_B_eff_UG():
    '''
    Underground configuration A14 - OUTPUT
    '''
    B_eff = 2.961985541915273
    return B_eff
