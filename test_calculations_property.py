import numpy as np
from itertools import permutations
from B_field import calculations


#TESTING CALC_B_PHASORS PROPERTIES


def test_zero_current(eg_input_single_OH):
    '''
    Tests:
    calc_B_phasors function output

    Given:
    single triad OVERHEAD (OH) - zero current

    Expected:
    Zero magnetic induction field B
    '''
    zero_phasors = np.zeros(4).reshape(2, 2)
    zero_current = 0
    calculated_B_phasors = calculations.calc_B_phasors(zero_current, eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    assert np.allclose(calculated_B_phasors, zero_phasors)

def test_current_is_doubled(eg_input_single_OH):
    '''
    Tests:
    calc_B_phasors function output

    Given:
    single triad OVERHEAD (OH) - a certain current value / doubled current value

    Expected:
    A certain magnetic induction field B values / B value doubled
    '''
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    doubled_current = 2*eg_input_single_OH[0][0]
    doubled_calculated_B_phasors = calculations.calc_B_phasors(doubled_current, eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    assert np.allclose(doubled_calculated_B_phasors, 2*calculated_B_phasors)

def test_one_cable_in_axis_origin(eg_input_single_OH):
    '''
    Tests:
    calc_B_phasors function output

    Given:
    single triad OVERHEAD (OH) - one of the three cables is in the axis origin (0, 0)

    Expected:
    No difference in the calculations and results
    '''
    origin_in_trellis_base_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    new_xp = eg_input_single_OH[1] - eg_input_single_OH[4][0][0][1]
    new_yp = eg_input_single_OH[2] - eg_input_single_OH[4][0][0][2]
    new_cable_array = [eg_input_single_OH[4][0][0][0], 0, 0]
    origin_in_first_cable_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], new_xp, new_yp, new_cable_array)
    assert np.allclose(origin_in_trellis_base_B_phasors, origin_in_first_cable_B_phasors)

def test_null_denominator(eg_input_single_OH):
    '''
    Tests:
    calc_B_phasors function output

    Given:
    single triad OVERHEAD (OH) - null denominator of the formula used

    Expected:
    NaN phasors are returned because it is a 0/0 division
    '''
    xp_coincident_xcable = eg_input_single_OH[4][0][0][1]
    yp_coincident_ycable = eg_input_single_OH[4][0][0][2]
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], xp_coincident_xcable, yp_coincident_ycable, eg_input_single_OH[4][0][0])
    assert np.all(np.isnan(calculated_B_phasors))


#TESTING CALC_B_EFFECTIVE PROPERTIES


def test_zero_B_eff_input():
    '''
    Tests:
    calc_B_effective function output

    Given:
    Zero B phasors as input

    Expected:
    Zero effective magnetic induction field B
    '''
    zero_B_phasors_first = np.zeros(4).reshape(2, 2)
    zero_B_phasors_second = np.zeros(4).reshape(2, 2)
    zero_B_phasors_third = np.zeros(4).reshape(2, 2)
    calculated_zero_B_effective = calculations.calc_B_effective(zero_B_phasors_first, zero_B_phasors_second, zero_B_phasors_third)
    assert np.isclose(calculated_zero_B_effective, 0)

def test_nan_B_eff_input():
    '''
    Tests:
    calc_B_effective function output

    Given:
    NaN B phasors as input

    Expected:
    NaN effective magnetic induction field B
    '''
    nan_phasors = np.empty((2, 2))
    nan_phasors[:] = np.nan
    calculated_nan_B_effective = calculations.calc_B_effective(nan_phasors)
    assert np.isnan(calculated_nan_B_effective)


#TESTING MAIN_POINT PROPERTIES


def test_dummy_values(eg_input_UG):
    '''
    Tests:
    main_point function output

    Given:
    single triad UNDERGROUND (UG) - point of interest coordinates (xp, yp) too close to the first cable

    Expected:
    Magnetic induction field dummy value '9999'
    '''
    dummy_value = 9999
    half_radius_cable = eg_input_UG[3]/4
    too_close_xp = eg_input_UG[4][0][0][1] + half_radius_cable
    too_close_yp = eg_input_UG[4][0][0][2] + half_radius_cable
    is_point_dummy = calculations.main_point(eg_input_UG[0], too_close_xp, too_close_yp, eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
    assert np.isclose(is_point_dummy, dummy_value)

def test_B_axial_symmetry_with_main_point(eg_input_UG):
    '''
    Tests:
    main_point function output

    Given:
    single triad UNDERGROUND (UG) - three cables (i.e. phases) arranged horizontally

    Expected:
    Axial symmetry with respect to the horizontal and vertical axis
    '''
    axial_symmetry_points = [(0, 0), (0, -3), (-1.7, -1.5), (1.7, -1.5)]
    B_values_to_check = np.empty((0))
    for i in range(4):
        B_value_to_append = calculations.main_point(eg_input_UG[0], axial_symmetry_points[i][0], axial_symmetry_points[i][1], eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
        B_values_to_check = np.append(B_values_to_check, B_value_to_append)
    #horizontal symmetry axis
    assert np.isclose(B_values_to_check[0], B_values_to_check[1])
    #vertical symmetry axis
    assert np.isclose(B_values_to_check[2], B_values_to_check[3])


#TESTING MAIN_GRID PROPERTIES


def test_all_phases_in_one_point(eg_input_UG):
    '''
    Tests:
    main_grid function output

    Given:
    single triad UNDERGROUND (UG) - three cables (i.e. phases) all in the same point

    Expected:
    Zero magnetic induction field B in all the grid
    
    Notes:
    In fact, twisted cables are typically used (in Low Voltage power lines) to drastically reduce magnetic induction field B.
    '''
    cables_array = np.array([[[330, 0, -1.5], [210, 0, -1.5], [90, 0, -1.5]],
                            [[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]]])
    grid_results = calculations.main_grid(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3], cables_array, eg_input_UG[5])
    assert np.allclose(grid_results[2], 0)

def test_matrix_radial_symmetry(eg_input_single_OH):
    '''
    Tests:
    main_grid function output

    Given:
    single triad OVERHEAD (OH) - only one cable (i.e. phase) with coordinates equal to the point of interest (x1 = xp, y1 = yp)

    Expected:
    Radial symmetry i.e. same grid through a 90 degrees rotation of it

    Notes:
    Second and third cables (i.e. phases) are very far away so not to influence the magnetic induction field B of a single cable
    '''
    xp, yp = 0, 0
    cables_array = np.array([[[330, 0, 0], [210, 1000000, 1000000], [90, 1000020, 1000020]],
                            [[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]]])
    grid_results = calculations.main_grid(eg_input_single_OH[0], xp, yp, eg_input_single_OH[3], cables_array, eg_input_single_OH[5])
    rotation_90_degree = np.rot90(grid_results[2])
    assert np.allclose(grid_results[2], rotation_90_degree)

def test_two_cables_central_symmetry_grid(eg_input_UG):
    '''
    Tests:
    main_grid function output

    Given:
    single triad UNDERGROUND (UG) - three cables arranged horizontally

    Expected:
    Axial symmetry with respect to the horizontal and vertical axis
    '''
    xp, yp = 0, -1.5
    grid_results = calculations.main_grid(eg_input_UG[0], xp, yp, eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
    horizontal_axis_reflection = np.flipud(grid_results[2])
    vertical_axis_reflection = np.fliplr(grid_results[2])
    assert np.allclose(grid_results[2], horizontal_axis_reflection)
    assert np.allclose(grid_results[2], vertical_axis_reflection)

def test_commutative_property_grid(eg_input_UG):
    '''
    Tests:
    main_grid function output

    Given:
    single triad UNDERGROUND (UG) - swap the cables phases through all the SIX possible permutations

    Expected:
    Magnetic induction field B is exactly the same in all the grid
    '''
    phases_permutations = permutations([90, 210, 330]) # SIX different permutations
    grids_to_compare = np.empty((13, 13)) # grids_to_compare[0:13] will be empty. Escamotage needed to concatenate 2D arrays.
    for phases_permutation in phases_permutations:
        cables_array = np.array([[[phases_permutation[0], -0.2, -1.5],
                                  [phases_permutation[1], 0, -1.5],
                                  [phases_permutation[2], 0.2, -1.5]],
                                [[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]]])
        grid_results = calculations.main_grid(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3], cables_array, eg_input_UG[5])
        grids_to_compare = np.concatenate((grids_to_compare, grid_results[2]))
    # FIVE different assertions to compare with each other SIX different grids
    for i in range(5):
        first_index = (i+1)*13
        second_index = (i+2)*13
        third_index = (i+3)*13
        assert np.allclose(grids_to_compare[first_index:second_index], grids_to_compare[second_index:third_index])

def test_six_cables_axial_symmetry_grid(eg_input_double_OH):
    '''
    Tests:
    main_grid function output

    Given:
    double triad OVERHEAD (OH) - six cables

    Expected:
    Axial symmetry with respect to the vertical axis
    '''
    xp, yp = 0, 11
    grid_results = calculations.main_grid(eg_input_double_OH[0], xp, yp, eg_input_double_OH[3], eg_input_double_OH[4], eg_input_double_OH[5])
    vertical_axis_reflection = np.fliplr(grid_results[2])
    assert np.allclose(grid_results[2], vertical_axis_reflection)


#TESTING CENTROID PROPERTIES


def test_given_centroid(eg_input_single_OH):
    '''
    Tests:
    centroid function output

    Given:
    single triad OVERHEAD (OH) - three cables arranged at the vertices of a triangle

    Expected:
    Centroid coordinates (xg, yg) as expected
    '''
    expected_xg, expected_yg = -1.2, 8.3
    xg, yg = calculations.centroid(eg_input_single_OH[4], eg_input_single_OH[5])
    assert expected_xg == xg, expected_yg == yg


#TESTING MAIN_DPA PROPERTIES


def test_dpa_y_independent(eg_input_double_OH):
    '''
    Tests:
    main_dpa function output

    Given:
    double triad OVERHEAD (OH) - same cable configuration / different y coordinates

    Expected:
    Same dpa values
    '''
    dpa_values_to_check = np.empty((0))
    for y_displacement in range(5):
        cables_array = np.array([[[330, -4.0, 6.3 + y_displacement],
                                [210, -3.6, 11 + y_displacement],
                                [90, -3.2, 15.7 + y_displacement]],

                                [[330, 4.0, 6.3 + y_displacement],
                                [210, 3.6, 11 + y_displacement],
                                [90, 3.2, 15.7 + y_displacement]]])
        dpa_value_to_append = calculations.main_dpa(eg_input_double_OH[0], eg_input_double_OH[3], cables_array, eg_input_double_OH[5], eg_input_double_OH[6])
        dpa_values_to_check = np.append(dpa_values_to_check, dpa_value_to_append)
    assert np.all(dpa_values_to_check == dpa_values_to_check[0])
