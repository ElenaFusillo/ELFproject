# This file contains all the fixtures needed for the tests.
# In such way, it is possible to use them among multiple files containing tests.

from numpy.lib.ufunclike import fix
from pytest import fixture
import numpy as np

@fixture
def eg_input_single_OH():
    '''
    Overhead configuration A1 - single triad - INPUT
    '''
    current = np.array([870, np.nan])
    xp = -20.5
    yp = 1
    diam_cables = 31.5*0.001
    cables_array = np.array([[[330, -3.75, 6.3], [210, 3.2, 8.3], [90, -3.05, 10.3]],
                            [[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]]])
    subparser_type = 'single'
    lim_val = 3
    return current, xp, yp, diam_cables, cables_array, subparser_type, lim_val

@fixture
def eg_input_single_conf_file():
    '''
    Overhead configuration A1 - single triad - INPUT (-point -bidim -dpa 3)
    '''
    file_content, args_list = [], ['single']
    with open('./examples/Argom_Bsingle.txt', encoding="utf-8") as conf_file:
        file_content = conf_file.readlines()
        for line in file_content:
            args_list += line.splitlines()
    optional_arguments = ['-point', '-bidim', '-dpa', '3']
    args_list.extend(optional_arguments)
    return args_list

@fixture
def eg_output_single_point_bidim_dpa():
    '''
    Overhead configuration A1 - single triad - OUTPUT (-point -bidim -dpa 3)
    '''
    file_content, output_string = [], ''
    with open('./examples/Single_output.txt', encoding="utf-8") as output_file:
        file_content = output_file.readlines()
        for line in file_content:
            output_string += line
    return output_string

@fixture
def eg_output_B_phasors_OH():
    '''
    Overhead configuration A1 - single cable (4-330°) - OUTPUT B PHASORS
    '''
    expected_output = np.array([float(2.58753332e-6), float(-1.49391306e-6), float(-8.17758172e-6), float(4.72132901e-6)]).reshape(2, 2)
    return expected_output

@fixture
def eg_input_UG():
    '''
    Underground configuration A14 - single triad - INPUT
    '''
    current = np.array([1110, np.nan])
    xp = 5.1
    yp = -1.5
    diam_cables = 108*0.001
    cables_array = np.array([[[330, -0.2, -1.5], [210, 0, -1.5], [90, 0.2, -1.5]],
                            [[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]]])
    subparser_type = 'single'
    lim_val = 3
    return current, xp, yp, diam_cables, cables_array, subparser_type, lim_val

@fixture
def eg_output_B_phasors_UG():
    '''
    Underground configuration A14 - single cable (4-330°) - OUTPUT B PHASORS
    '''
    expected_output = np.array([0, 0, float(3.62750264e-05), float(-2.09433962e-05)]).reshape(2, 2)
    return expected_output

@fixture
def eg_input_B_eff_single_OH():
    '''
    Overhead configuration A1 - single triad - INPUT
    '''
    expected_input_1 = np.array([float(2.58753332e-06), float(-1.49391306e-06), float(-8.17758172e-06), float(4.72132901e-06)]).reshape(2, 2)
    expected_input_2 = np.array([float(-1.78871747e-06), float(-1.03271651e-06), float(5.80720603e-06), float(3.35279196e-06)]).reshape(2, 2)
    expected_input_3 = np.array([float(2.53422182e-22), float(4.13869831e-06), float(-4.75507213e-22), float(-7.76562211e-06)]).reshape(2, 2)
    return expected_input_1, expected_input_2, expected_input_3

@fixture
def eg_output_single_OH():
    '''
    Overhead configuration A1 - single triad - OUTPUT
    '''
    B_eff = 2.991776205053418
    x = np.array([-23.5, -23, -22.5, -22, -21.5, -21, -20.5, -20, -19.5, -19, -18.5, -18, -17.5])
    y = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
    z_grid = np.array([[2.11, 2.19, 2.28, 2.37, 2.46, 2.56, 2.66, 2.78, 2.89, 3.02, 3.15, 3.29, 3.44],
                       [2.15, 2.23, 2.32, 2.41, 2.51, 2.61, 2.72, 2.84, 2.96, 3.09, 3.23, 3.38, 3.53],
                       [2.18, 2.27, 2.36, 2.45, 2.56, 2.66, 2.78, 2.90, 3.03, 3.16, 3.31, 3.46, 3.63],
                       [2.22, 2.30, 2.40, 2.50, 2.60, 2.71, 2.83, 2.96, 3.09, 3.24, 3.39, 3.55, 3.72],
                       [2.25, 2.34, 2.44, 2.54, 2.65, 2.76, 2.89, 3.02, 3.16, 3.31, 3.47, 3.64, 3.82],
                       [2.28, 2.37, 2.47, 2.58, 2.69, 2.81, 2.94, 3.08, 3.22, 3.38, 3.54, 3.72, 3.91],
                       [2.31, 2.41, 2.51, 2.62, 2.74, 2.86, 2.99, 3.13, 3.28, 3.45, 3.62, 3.81, 4.01],
                       [2.34, 2.44, 2.54, 2.66, 2.78, 2.90, 3.04, 3.19, 3.34, 3.51, 3.69, 3.89, 4.10],
                       [2.37, 2.47, 2.58, 2.69, 2.82, 2.95, 3.09, 3.24, 3.40, 3.58, 3.76, 3.96, 4.18],
                       [2.39, 2.50, 2.61, 2.73, 2.85, 2.99, 3.13, 3.29, 3.46, 3.64, 3.83, 4.04, 4.27],
                       [2.42, 2.53, 2.64, 2.76, 2.89, 3.03, 3.18, 3.34, 3.51, 3.69, 3.89, 4.11, 4.35],
                       [2.44, 2.55, 2.67, 2.79, 2.92, 3.06, 3.22, 3.38, 3.56, 3.75, 3.95, 4.18, 4.42],
                       [2.46, 2.57, 2.69, 2.82, 2.95, 3.10, 3.25, 3.42, 3.60, 3.80, 4.01, 4.24, 4.49]])
    xg, yg = -1.2, 8.3
    dpa_value = 21.999999999999996
    delta, nx = 35, 71
    x_lim = np.linspace(xg-delta, xg+delta, nx)
    z_array = [1.04, 1.1, 1.17, 1.24, 1.32, 1.41, 1.51, 1.62, 1.74, 1.87, 2.03, 2.2, 2.39, 2.62, 2.87, 3.17, 3.51, 3.91, 4.39, 4.96, 5.65, 6.5, 7.55, 8.9, 10.65, 12.98,
               16.18, 20.77, 27.64, 38.52, 56.73, 87.49, 129.76, 151.24, 131.27, 107.85, 100.09, 110.06, 154.76, 460.69, 267.76, 89.11, 49.33, 32.39, 23.25, 17.63,
               13.9, 11.27, 9.35, 7.88, 6.75, 5.84, 5.11, 4.51, 4.01, 3.59, 3.24, 2.93, 2.67, 2.44, 2.24, 2.06, 1.91, 1.77, 1.64, 1.53, 1.43, 1.34, 1.26, 1.18, 1.11]
    lim_val = 3
    return B_eff, x, y, z_grid, xg, yg, dpa_value, delta, nx, x_lim, z_array, lim_val

@fixture
def eg_input_double_OH():
    '''
    Overhead configuration A9 - double triad - INPUT
    '''
    currents = np.array([870, 870])
    xp, yp = -5, 1
    diam_cables = 31.5*0.001
    cables_array = np.array([[[330, -4.0, 6.3],
                              [210, -3.6, 11],
                              [90, -3.2, 15.7]],

                             [[330, 4.0, 6.3],
                              [210, 3.6, 11],
                              [90, 3.2, 15.7]]])
    subparser_type = 'double'
    lim_val = 3
    return currents, xp, yp, diam_cables, cables_array, subparser_type, lim_val

@fixture
def eg_input_double_conf_file():
    '''
    Overhead configuration A9 - double triad - INPUT (-point -bidim -dpa 3)
    '''
    file_content, args_list = [], ['double']
    with open('./examples/Argom_Bdouble.txt', encoding="utf-8") as conf_file:
        file_content = conf_file.readlines()
        for line in file_content:
            args_list += line.splitlines()
    optional_arguments = ['-point', '-bidim', '-dpa', '3']
    args_list.extend(optional_arguments)
    return args_list

@fixture
def eg_output_double_point_bidim_dpa():
    '''
    Overhead configuration A9 - double triad - OUTPUT (-point -bidim -dpa 3)
    '''
    file_content, output_string = [], ''
    with open('./examples/Double_output.txt', encoding="utf-8") as output_file:
        file_content = output_file.readlines()
        for line in file_content:
            output_string += line
    return output_string

@fixture
def eg_input_B_eff_double_OH():
    '''
    Overhead configuration A9 - double triad - INPUT
    '''
    expected_input_1 = np.array([float(2.74544045e-05), float(-1.58508078e-05), float(-5.18007633e-06), float(2.99071846e-06)]).reshape(2, 2)
    expected_input_2 = np.array([float(-1.47791703e-05), float(-8.53275795e-06), float(2.06908384e-06), float(1.19458611e-06)]).reshape(2, 2)
    expected_input_3 = np.array([float(7.14084162e-22), float(1.16618794e-05), float(-8.74388770e-23), float(-1.42798523e-06)]).reshape(2, 2)
    expected_input_4 = np.array([float(7.32100676e-06), float(-4.22678523e-06), float(-1.24318983e-05), float(7.17755982e-06)]).reshape(2, 2)
    expected_input_5 = np.array([float(-8.66224536e-06), float(-5.00114969e-06), float(7.44953101e-06), float(4.30098874e-06)]).reshape(2, 2)
    expected_input_6 = np.array([float(5.52783254e-22), float(9.02763562e-06), float(-3.08355284e-22), float(-5.03582395e-06)]).reshape(2, 2)
    return expected_input_1, expected_input_2, expected_input_3, expected_input_4, expected_input_5, expected_input_6

@fixture
def eg_output_double_OH():
    '''
    Overhead configuration A9 - double triad - OUTPUT
    '''
    B_eff = 21.108776674367164
    x = np.array([-8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2])
    y = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
    z_grid = np.array([[11.79, 12.08, 12.34, 12.58, 12.78, 12.95, 13.08, 13.17, 13.22, 13.25, 13.24, 13.22, 13.18],
                       [12.56, 12.89, 13.19, 13.46, 13.68, 13.86, 13.99, 14.08, 14.11, 14.11, 14.08, 14.02, 13.95],
                       [13.42, 13.80, 14.14, 14.45, 14.70, 14.89, 15.03, 15.10, 15.11, 15.07, 14.99, 14.88, 14.75],
                       [14.38, 14.82, 15.22, 15.57, 15.86, 16.07, 16.21, 16.26, 16.24, 16.14, 15.99, 15.80, 15.60],
                       [15.45, 15.97, 16.44, 16.86, 17.19, 17.44, 17.58, 17.61, 17.53, 17.35, 17.10, 16.81, 16.49],
                       [16.65, 17.28, 17.85, 18.35, 18.75, 19.04, 19.18, 19.18, 19.03, 18.75, 18.35, 17.90, 17.42],
                       [18.01, 18.77, 19.47, 20.09, 20.59, 20.94, 21.11, 21.07, 20.82, 20.38, 19.79, 19.10, 18.38],
                       [19.55, 20.48, 21.36, 22.15, 22.80, 23.26, 23.46, 23.38, 23.01, 22.35, 21.47, 20.45, 19.39],
                       [21.30, 22.46, 23.58, 24.62, 25.49, 26.12, 26.41, 26.31, 25.77, 24.82, 23.52, 22.02, 20.45],
                       [23.26, 24.73, 26.19, 27.58, 28.81, 29.73, 30.22, 30.13, 29.40, 28.03, 26.15, 23.94, 21.63],
                       [25.47, 27.34, 29.27, 31.19, 32.96, 34.40, 35.27, 35.31, 34.36, 32.43, 29.69, 26.46, 23.10],
                       [27.93, 30.31, 32.88, 35.56, 38.21, 40.56, 42.20, 42.64, 41.52, 38.77, 34.75, 30.03, 25.16],
                       [30.61, 33.64, 37.06, 40.84, 44.87, 48.82, 52.06, 53.60, 52.48, 48.49, 42.39, 35.38, 28.42]])
    xg, yg = 0.0, 11.0
    dpa_value = 32.0
    delta, nx = 35, 71
    x_lim = np.linspace(xg-delta, xg+delta, nx)
    z_array = [2.35, 2.49, 2.65, 2.82, 3.01, 3.22, 3.45, 3.7, 3.99, 4.31, 4.67, 5.08, 5.55, 6.08, 6.69, 7.4, 8.24, 9.22, 10.38, 11.78, 13.49, 15.58, 18.2, 21.51, 25.78,
               31.38, 38.89, 49.22, 64.13, 88.07, 139.91, 445.74, 289.2, 119.35, 88.08, 81.09, 88.08, 119.35, 289.2, 445.74, 139.91, 88.07, 64.13, 49.22, 38.89, 31.38,
               25.78, 21.51, 18.2, 15.58, 13.49, 11.78, 10.38, 9.22, 8.24, 7.4, 6.69, 6.08, 5.55, 5.08, 4.67, 4.31, 3.99, 3.7, 3.45, 3.22, 3.01, 2.82, 2.65, 2.49, 2.35]
    lim_val = 3
    return B_eff, x, y, z_grid, xg, yg, dpa_value, delta, nx, x_lim, z_array, lim_val

@fixture
def eg_input_B_eff_UG():
    '''
    Underground configuration A14 - INPUT
    '''
    expected_input_1 = np.array([0, 0, float(3.62750264e-05), float(-2.09433962e-05)]).reshape(2, 2)
    expected_input_2 = np.array([0, 0, float(-3.76975764e-05), float(-2.17647059e-05)]).reshape(2, 2)
    expected_input_3 = np.array([0, 0, float(2.77419989e-21), float(4.53061225e-05)]).reshape(2, 2)
    return expected_input_1, expected_input_2, expected_input_3

@fixture
def eg_output_UG():
    '''
    Underground configuration A14 - OUTPUT
    '''
    B_eff = 2.961985541915273
    x = np.array([2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1, 5.6, 6.1, 6.6, 7.1, 7.6, 8.1])
    y = np.array([-4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    z_grid = np.array([[5.73, 4.88, 4.13, 3.50, 2.98, 2.55, 2.20, 1.91, 1.67, 1.46, 1.30, 1.15, 1.03],
                       [7.21, 5.91, 4.85, 4.01, 3.34, 2.81, 2.39, 2.05, 1.77, 1.55, 1.36, 1.20, 1.07],
                       [9.15, 7.16, 5.66, 4.54, 3.70, 3.06, 2.57, 2.18, 1.87, 1.62, 1.41, 1.25, 1.11],
                       [11.58, 8.56, 6.50, 5.07, 4.04, 3.29, 2.73, 2.29, 1.95, 1.68, 1.46, 1.28, 1.13],
                       [14.30, 9.96, 7.27, 5.53, 4.33, 3.48, 2.85, 2.38, 2.01, 1.73, 1.50, 1.31, 1.16],
                       [16.65, 11.04, 7.83, 5.84, 4.52, 3.60, 2.93, 2.44, 2.06, 1.76, 1.52, 1.33, 1.17],
                       [17.62, 11.46, 8.04, 5.96, 4.59, 3.64, 2.96, 2.46, 2.07, 1.77, 1.53, 1.33, 1.17],
                       [16.65, 11.04, 7.83, 5.84, 4.52, 3.60, 2.93, 2.44, 2.06, 1.76, 1.52, 1.33, 1.17],
                       [14.30, 9.96, 7.27, 5.53, 4.33, 3.48, 2.85, 2.38, 2.01, 1.73, 1.50, 1.31, 1.16],
                       [11.58, 8.56, 6.50, 5.07, 4.04, 3.29, 2.73, 2.29, 1.95, 1.68, 1.46, 1.28, 1.13],
                       [9.15, 7.16, 5.66, 4.54, 3.70, 3.06, 2.57, 2.18, 1.87, 1.62, 1.41, 1.25, 1.11],
                       [7.21, 5.91, 4.85, 4.01, 3.34, 2.81, 2.39, 2.05, 1.77, 1.55, 1.36, 1.20, 1.07],
                       [5.73, 4.88, 4.13, 3.50, 2.98, 2.55, 2.20, 1.91, 1.67, 1.46, 1.30, 1.15, 1.03]])
    xg, yg = 0.0, -1.5
    dpa_value = 5.100000000000001
    delta, nx = 6, 121
    x_lim = np.linspace(xg-delta, xg+delta, nx)
    z_array = [2.14, 2.21, 2.29, 2.37, 2.46, 2.55, 2.64, 2.74, 2.85, 2.96, 3.08, 3.21, 3.34, 3.49, 3.64, 3.81, 3.98, 4.17, 4.37, 4.59, 4.82, 5.07, 5.34, 5.64, 5.96, 6.3,
               6.68, 7.09, 7.54, 8.04, 8.59, 9.2, 9.87, 10.62, 11.46, 12.4, 13.46, 14.67, 16.04, 17.62, 19.45, 21.58, 24.08, 27.05, 30.6, 34.9, 40.19, 46.79, 55.18, 66.09,
               80.64, 100.69, 129.5, 173.21, 244.73, 375.84, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 375.84, 244.73, 173.21, 129.5, 100.69, 80.64, 66.09,
               55.18, 46.79, 40.19, 34.9, 30.6, 27.05, 24.08, 21.58, 19.45, 17.62, 16.04, 14.67, 13.46, 12.4, 11.46, 10.62, 9.87, 9.2, 8.59, 8.04, 7.54, 7.09, 6.68, 6.3,
               5.96, 5.64, 5.34, 5.07, 4.82, 4.59, 4.37, 4.17, 3.98, 3.81, 3.64, 3.49, 3.34, 3.21, 3.08, 2.96, 2.85, 2.74, 2.64, 2.55, 2.46, 2.37, 2.29, 2.21, 2.14]
    lim_val = 3
    return B_eff, x, y, z_grid, xg, yg, dpa_value, delta, nx, x_lim, z_array, lim_val
