# import hypothesis.strategies as st
# from hypothesis import given, settings

import numpy as np
#import pytest
from B_field import calculations


def test_calc_B_phasors_overhead(eg_input_single_OH, eg_output_B_phasors_OH):
    '''
    This test verifies that the function calc_B_phasors, given the proper input
    of a single cable OVERHEAD (OH), returns for each element of the numpy array
    what is expected to.
    '''
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_single_OH[0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[3][0])
    assert np.isclose(calculated_B_phasors[0, 0], eg_output_B_phasors_OH[0, 0])
    assert np.isclose(calculated_B_phasors[0, 1], eg_output_B_phasors_OH[0, 1])
    assert np.isclose(calculated_B_phasors[1, 0], eg_output_B_phasors_OH[1, 0])
    assert np.isclose(calculated_B_phasors[1, 1], eg_output_B_phasors_OH[1, 1])

def test_calc_B_phasors_underground(eg_input_UG, eg_output_B_phasors_UG):
    '''
    This test verifies that the function calc_B_phasors, given the proper input
    of a single cable UNDERGROUND (UG), returns for each element of the numpy array
    what is expected to.
    '''
    calculated_B_phasors = calculations.calc_B_phasors(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3][0])
    assert np.isclose(calculated_B_phasors[0, 0], eg_output_B_phasors_UG[0, 0])
    assert np.isclose(calculated_B_phasors[0, 1], eg_output_B_phasors_UG[0, 1])
    assert np.isclose(calculated_B_phasors[1, 0], eg_output_B_phasors_UG[1, 0])
    assert np.isclose(calculated_B_phasors[1, 1], eg_output_B_phasors_UG[1, 1])

def test_calc_B_effective_overhead(eg_input_B_eff_single_OH, eg_input_B_eff_double_OH, eg_output_B_eff_single_OH, eg_output_B_eff_double_OH):
    '''
    This test verifies that the function calc_B_effective, given the proper input
    of a single triad or double triad OVERHEAD (OH), returns what is expected to.
    '''
    calculated_B_effective_single_OH = calculations.calc_B_effective(eg_input_B_eff_single_OH[0], eg_input_B_eff_single_OH[1], eg_input_B_eff_single_OH[2])
    calculated_B_effective_double_OH = calculations.calc_B_effective(eg_input_B_eff_double_OH[0], eg_input_B_eff_double_OH[1], eg_input_B_eff_double_OH[2],
                                                                  eg_input_B_eff_double_OH[3], eg_input_B_eff_double_OH[4], eg_input_B_eff_double_OH[5])
    assert np.isclose(calculated_B_effective_single_OH, eg_output_B_eff_single_OH)
    assert np.isclose(calculated_B_effective_double_OH, eg_output_B_eff_double_OH)

def test_calc_B_effective_underground(eg_input_B_eff_UG, eg_output_B_eff_UG):
    '''
    This test verifies that the function calc_B_effective, given the proper input
    of a single triad UNDERGROUND (UG), returns what is expected to.
    '''
    calculated_B_effective_UG = calculations.calc_B_effective(eg_input_B_eff_UG[0], eg_input_B_eff_UG[1], eg_input_B_eff_UG[2])
    assert np.isclose(calculated_B_effective_UG, eg_output_B_eff_UG)

def test_main_single(eg_input_single_OH, eg_output_B_eff_single_OH, eg_input_UG, eg_output_B_eff_UG):
    '''
    This test verifies that the function main_single, given the proper input
    of a single triad OVERHEAD (OH) or UNDERGROUND (UG), returns what is expected to.
    '''
    calculated_main_single_OH = calculations.main_single(eg_input_single_OH[0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[3])
    calculated_main_single_UG = calculations.main_single(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3])
    assert np.isclose(calculated_main_single_OH, eg_output_B_eff_single_OH)
    assert np.isclose(calculated_main_single_UG, eg_output_B_eff_UG)

def test_main_double(eg_input_double_OH, eg_output_B_eff_double_OH):
    '''
    This test verifies that the function main_double, given the proper input
    of a double triad OVERHEAD (OH), returns what is expected to.
    '''
    calculated_main_double_OH = calculations.main_double(eg_input_double_OH[0], eg_input_double_OH[1], eg_input_double_OH[2], eg_input_double_OH[3])
    assert np.isclose(calculated_main_double_OH, eg_output_B_eff_double_OH)
