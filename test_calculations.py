import numpy as np
from B_field import calculations


def test_calc_B_phasors_overhead(eg_input_single_OH, eg_output_B_phasors_OH):
    '''
    This test verifies that the function calc_B_phasors, given the proper input
    of a single cable OVERHEAD (OH), returns for each element of the numpy array
    what is expected to.
    '''
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0][0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    assert np.allclose(calculated_B_phasors, eg_output_B_phasors_OH)

def test_calc_B_phasors_underground(eg_input_UG, eg_output_B_phasors_UG):
    '''
    This test verifies that the function calc_B_phasors, given the proper input
    of a single cable UNDERGROUND (UG), returns for each element of the numpy array
    what is expected to.
    '''
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_UG[0][0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[4][0][0])
    assert np.allclose(calculated_B_phasors, eg_output_B_phasors_UG)


def test_calc_B_effective_overhead(eg_input_B_eff_single_OH, eg_input_B_eff_double_OH, eg_output_single_OH, eg_output_double_OH):
    '''
    This test verifies that the function calc_B_effective, given the proper input
    of a single triad or double triad OVERHEAD (OH), returns what is expected to.
    '''
    calculated_B_effective_single_OH = calculations.calc_B_effective(eg_input_B_eff_single_OH[0], eg_input_B_eff_single_OH[1], eg_input_B_eff_single_OH[2])
    calculated_B_effective_double_OH = calculations.calc_B_effective(eg_input_B_eff_double_OH[0], eg_input_B_eff_double_OH[1], eg_input_B_eff_double_OH[2],
                                                                  eg_input_B_eff_double_OH[3], eg_input_B_eff_double_OH[4], eg_input_B_eff_double_OH[5])
    assert np.isclose(calculated_B_effective_single_OH, eg_output_single_OH[0])
    assert np.isclose(calculated_B_effective_double_OH, eg_output_double_OH[0])


def test_calc_B_effective_underground(eg_input_B_eff_UG, eg_output_UG):
    '''
    This test verifies that the function calc_B_effective, given the proper input
    of a single triad UNDERGROUND (UG), returns what is expected to.
    '''
    calculated_B_effective_UG = calculations.calc_B_effective(eg_input_B_eff_UG[0], eg_input_B_eff_UG[1], eg_input_B_eff_UG[2])
    assert np.isclose(calculated_B_effective_UG, eg_output_UG[0])


def test_main_point(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    This test verifies that the function main_point, given the proper input
    of either a single triad OVERHEAD (OH) or UNDERGROUND (UG),
    or a double triad OVERHEAD (OH), returns what is expected to.
    '''
    calculated_point_single_OH = calculations.main_point(eg_input_single_OH[0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[3], eg_input_single_OH[4], eg_input_single_OH[5])
    calculated_point_single_UG = calculations.main_point(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
    calculated_point_double_OH = calculations.main_point(eg_input_double_OH[0], eg_input_double_OH[1], eg_input_double_OH[2], eg_input_double_OH[3], eg_input_double_OH[4], eg_input_double_OH[5])
    assert np.isclose(calculated_point_single_OH, eg_output_single_OH[0])
    assert np.isclose(calculated_point_single_UG, eg_output_UG[0])
    assert np.isclose(calculated_point_double_OH, eg_output_double_OH[0])

def test_main_grid(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    This test verifies that the function main_grid, given the proper input
    of either a single triad OVERHEAD (OH) or UNDERGROUND (UG),
    or a double triad OVERHEAD (OH), returns what is expected to.
    '''
    calculated_grid_single_OH = calculations.main_grid(eg_input_single_OH[0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[3], eg_input_single_OH[4], eg_input_single_OH[5])
    calculated_grid_single_UG = calculations.main_grid(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
    calculated_grid_double_OH = calculations.main_grid(eg_input_double_OH[0], eg_input_double_OH[1], eg_input_double_OH[2], eg_input_double_OH[3], eg_input_double_OH[4], eg_input_double_OH[5])
    #assert Single Overhead
    assert np.allclose(calculated_grid_single_OH[0], eg_output_single_OH[1])
    assert np.allclose(calculated_grid_single_OH[1], eg_output_single_OH[2])
    assert np.allclose(calculated_grid_single_OH[2], eg_output_single_OH[3], rtol=1e-02)
    #assert Single Underground
    assert np.allclose(calculated_grid_single_UG[0], eg_output_UG[1])
    assert np.allclose(calculated_grid_single_UG[1], eg_output_UG[2])
    assert np.allclose(calculated_grid_single_UG[2], eg_output_UG[3], rtol=1e-02)
    #assert Double Overhead
    assert np.allclose(calculated_grid_double_OH[0], eg_output_double_OH[1])
    assert np.allclose(calculated_grid_double_OH[1], eg_output_double_OH[2])
    assert np.allclose(calculated_grid_double_OH[2], eg_output_double_OH[3], rtol=1e-02)


def test_centroid():
    #TODO write a test
    return True


def test_is_underground():
    #TODO write a test
    return True


def test_lim_val_checker():
    #TODO write a test
    return True


def test_main_dpa():
    #TODO write a test
    return True
