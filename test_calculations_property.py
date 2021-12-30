import numpy as np

from B_field import calculations


#TESTING CALC_B_PHASORS PROPERTIES


#TODO strategies? For every xp, yp, phase, cable coordinates -- return zero
def test_zero_current(eg_input_single_OH):
    '''TODO docstring
    If current is zero -- B is zero'''
    zero_phasors = np.zeros(4).reshape(2, 2)
    zero_current = 0
    calculated_B_phasors = calculations.calc_B_phasors(zero_current, eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    assert np.allclose(calculated_B_phasors, zero_phasors)

#TODO strategies? For every current value, if it's doubled -- B doubles
def test_current_is_doubled(eg_input_single_OH):
    '''TODO docstring
    If current is doubled -- B doubled'''
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    doubled_current = 2*eg_input_single_OH[0][0]
    doubled_calculated_B_phasors = calculations.calc_B_phasors(doubled_current, eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    assert np.allclose(doubled_calculated_B_phasors, 2*calculated_B_phasors)

def test_one_cable_in_axis_origin(eg_input_single_OH):
    '''TODO docstring
    If one cable in the axis origin -- there's no difference'''
    origin_in_trellis_base_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    new_xp = eg_input_single_OH[1] - eg_input_single_OH[4][0][0][1]
    new_yp = eg_input_single_OH[2] - eg_input_single_OH[4][0][0][2]
    new_cable_array = [eg_input_single_OH[4][0][0][0], 0, 0]
    origin_in_first_cable_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], new_xp, new_yp, new_cable_array)
    assert np.allclose(origin_in_trellis_base_B_phasors, origin_in_first_cable_B_phasors)

def test_null_denominator(eg_input_single_OH):
    '''TODO docstring
    If null denominator -- returns nan'''
    xp_coincident_xcable = eg_input_single_OH[4][0][0][1]
    yp_coincident_ycable = eg_input_single_OH[4][0][0][2]
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], xp_coincident_xcable, yp_coincident_ycable, eg_input_single_OH[4][0][0])
    assert np.all(np.isnan(calculated_B_phasors))
    # FIXME restituisce due warning, da controllare!!


#TESTING CALC_B_EFFECTIVE PROPERTIES


def test_zero_B_eff_input():
    '''TODO docstring
    If input calc_B_effective is zero -- return zero'''
    zero_phasors_first = np.zeros(4).reshape(2, 2)
    zero_phasors_second = np.zeros(4).reshape(2, 2)
    zero_phasors_third = np.zeros(4).reshape(2, 2)
    calculated_zero_B_effective = calculations.calc_B_effective(zero_phasors_first, zero_phasors_second, zero_phasors_third)
    assert np.isclose(calculated_zero_B_effective, 0)

def test_nan_B_eff_input():
    '''TODO docstring
    If input calc_B_effective is nan -- return nan'''
    nan_phasors = np.empty((2, 2))
    nan_phasors[:] = np.nan
    calculated_nan_B_effective = calculations.calc_B_effective(nan_phasors)
    assert np.isnan(calculated_nan_B_effective)


#TESTING MAIN_POINT PROPERTIES


def test_dummy_values(eg_input_UG):
    '''TODO docstring
    If xp, yp too close to cable -- return dummy'''
    dummy_value = 9999
    half_radius_cable = eg_input_UG[3]/4
    too_close_xp = eg_input_UG[4][0][0][1] + half_radius_cable
    too_close_yp = eg_input_UG[4][0][0][2] + half_radius_cable
    is_point_dummy = calculations.main_point(eg_input_UG[0], too_close_xp, too_close_yp, eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
    assert np.isclose(is_point_dummy, dummy_value)

def test_one_cable_radial_symmetry():
    '''TODO docstring
    With only one cable --- radial/circular symmetry'''
    assert True

def test_two_cables_central_symmetry_point():
    '''TODO docstring
    With two cables --- specular symmetry'''
    assert True

def test_commutative_property_point():
    '''TODO docstring
    If I swap the cables (1-2 / 2-1) -- egual result'''
    assert True

def test_balance_point():
    '''TODO docstring
    One cable pos x+1, one cable pos x-1. Middle point is balance point. I.e. where B1 - B2 = 0'''
    assert True


#TESTING MAIN_GRID PROPERTIES


def test_dummy_return_highest_B():
    '''TODO docstring
    If there's a dummy value -- return highest B value not dummy'''
    assert True

def test_matrix_rotational_symmetry():
    '''TODO docstring - mentioned
    Is it rotational symmetry?
    One cable, its coordinates equal to xp,yp. Double matrix reflection --- same matrix again'''
    assert True

def test_two_cables_central_symmetry_grid():
    '''TODO docstring
    Two cables, 2 symmetry axes all around them'''
    assert True

def test_commutative_property_grid():
    '''TODO docstring
    If I swap the cables (1-2 / 2-1) -- same result'''
    assert True

def test_six_cables_axial_symmetry_grid():
    '''TODO docstring
    Six cables -- 1 vertical axis of symmetry'''
    assert True

#TESTING CENTROID PROPERTIES


def test_given_centroid():
    '''TODO docstring
    Three cables (clover-shape) around origin 0,0 -- centroid is where it should be'''
    assert True

#TESTING MAIN_DPA PROPERTIES

def test_dpa_current_doubled():
    '''TODO docstring
    Double current -- double dpa'''
    assert True

def test_dpa_y_independent():
    '''TODO docstring
    Same cable configuration. Different y coordinate -- same dpa'''
    assert True
