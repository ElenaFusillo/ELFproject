import numpy as np

from B_field import calculations


def test_calc_B_phasors(eg_input_single_OH, eg_output_B_phasors_OH, eg_input_UG, eg_output_B_phasors_UG):
    '''
    Tests:
    calc_B_phasors numpy array output element-wise

    Given:
    single cable OVERHEAD (OH)
    single cable UNDERGROUND (UG)
    '''
    calculated_B_phasors_OH = calculations.calc_B_phasors(eg_input_single_OH[0][0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[4][0][0])
    calculated_B_phasors_UG = calculations.calc_B_phasors(eg_input_UG[0][0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[4][0][0])
    assert np.allclose(calculated_B_phasors_OH, eg_output_B_phasors_OH)
    assert np.allclose(calculated_B_phasors_UG, eg_output_B_phasors_UG)


def test_calc_B_effective(eg_input_B_eff_single_OH, eg_output_single_OH, eg_input_B_eff_UG, eg_output_UG, eg_input_B_eff_double_OH, eg_output_double_OH):
    '''
    Tests:
    calc_B_effective function output

    Given:
    single triad OVERHEAD (OH)
    single triad UNDERGROUND (UG)
    double triad OVERHEAD (OH)
    '''
    calculated_B_effective_single_OH = calculations.calc_B_effective(eg_input_B_eff_single_OH[0], eg_input_B_eff_single_OH[1], eg_input_B_eff_single_OH[2])
    calculated_B_effective_UG = calculations.calc_B_effective(eg_input_B_eff_UG[0], eg_input_B_eff_UG[1], eg_input_B_eff_UG[2])
    calculated_B_effective_double_OH = calculations.calc_B_effective(eg_input_B_eff_double_OH[0], eg_input_B_eff_double_OH[1], eg_input_B_eff_double_OH[2],
                                                                     eg_input_B_eff_double_OH[3], eg_input_B_eff_double_OH[4], eg_input_B_eff_double_OH[5])
    assert np.isclose(calculated_B_effective_single_OH, eg_output_single_OH[0])
    assert np.isclose(calculated_B_effective_UG, eg_output_UG[0])
    assert np.isclose(calculated_B_effective_double_OH, eg_output_double_OH[0])


def test_main_point(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    Tests:
    main_point function output
    
    Given:
    single triad OVERHEAD (OH)
    singe triad UNDERGROUND (UG)
    double triad OVERHEAD (OH)
    '''
    calculated_point_single_OH = calculations.main_point(eg_input_single_OH[0], eg_input_single_OH[1], eg_input_single_OH[2], eg_input_single_OH[3], eg_input_single_OH[4], eg_input_single_OH[5])
    calculated_point_single_UG = calculations.main_point(eg_input_UG[0], eg_input_UG[1], eg_input_UG[2], eg_input_UG[3], eg_input_UG[4], eg_input_UG[5])
    calculated_point_double_OH = calculations.main_point(eg_input_double_OH[0], eg_input_double_OH[1], eg_input_double_OH[2], eg_input_double_OH[3], eg_input_double_OH[4], eg_input_double_OH[5])
    assert np.isclose(calculated_point_single_OH, eg_output_single_OH[0])
    assert np.isclose(calculated_point_single_UG, eg_output_UG[0])
    assert np.isclose(calculated_point_double_OH, eg_output_double_OH[0])


def test_main_grid(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    Tests:
    main_grid function output

    Given:
    single triad OVERHEAD (OH)
    single triad UNDERGROUND (UG)
    double triad OVERHEAD (OH)
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


def test_centroid(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    Tests:
    centroid function output
    
    Given:
    single triad OVERHEAD (OH)
    single triad UNDERGROUND (UG)
    double triad OVERHEAD (OH)
    '''
    calculated_centroid_single_OH = calculations.centroid(eg_input_single_OH[4], eg_input_single_OH[5])
    calculated_centroid_single_UG = calculations.centroid(eg_input_UG[4], eg_input_UG[5])
    calculated_centroid_double_OH = calculations.centroid(eg_input_double_OH[4], eg_input_double_OH[5])
    assert np.allclose(calculated_centroid_single_OH, eg_output_single_OH[4:6])
    assert np.allclose(calculated_centroid_single_UG, eg_output_UG[4:6])
    assert np.allclose(calculated_centroid_double_OH, eg_output_double_OH[4:6])


def test_is_underground(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    Tests:
    is_underground function output
    
    Given:
    single triad OVERHEAD (OH)
    single triad UNDERGROUND (UG)
    double triad OVERHEAD (OH)
    '''
    calculated_is_under_single_OH = calculations.is_underground(eg_input_single_OH[4], eg_input_single_OH[5])
    calculated_is_under_single_UG = calculations.is_underground(eg_input_UG[4], eg_input_UG[5])
    calculated_is_under_ouble_OH = calculations.is_underground(eg_input_double_OH[4], eg_input_double_OH[5])
    assert np.allclose(calculated_is_under_single_OH, eg_output_single_OH[7:9])
    assert np.allclose(calculated_is_under_single_UG, eg_output_UG[7:9])
    assert np.allclose(calculated_is_under_ouble_OH, eg_output_double_OH[7:9])


def test_lim_val_checker(eg_output_single_OH, eg_output_UG, eg_output_double_OH):
    '''
    Tests:
    lim_val_checker function output
    
    Given:
    single triad OVERHEAD (OH)
    single triad UNDERGROUND (UG)
    double triad OVERHEAD (OH)
    '''
    calculated_lim_check_single_OH = calculations.lim_val_checker(eg_output_single_OH[4], eg_output_single_OH[9], eg_output_single_OH[8], eg_output_single_OH[10], eg_output_single_OH[11])
    calculated_lim_check_single_UG = calculations.lim_val_checker(eg_output_UG[4], eg_output_UG[9], eg_output_UG[8], eg_output_UG[10], eg_output_UG[11])
    calculated_lim_check_double_OH = calculations.lim_val_checker(eg_output_double_OH[4], eg_output_double_OH[9], eg_output_double_OH[8], eg_output_double_OH[10], eg_output_double_OH[11])
    assert np.isclose(calculated_lim_check_single_OH, eg_output_single_OH[6])
    assert np.isclose(calculated_lim_check_single_UG, eg_output_UG[6])
    assert np.isclose(calculated_lim_check_double_OH, eg_output_double_OH[6])


def test_main_dpa(eg_input_single_OH, eg_output_single_OH, eg_input_UG, eg_output_UG, eg_input_double_OH, eg_output_double_OH):
    '''
    Tests:
    main_dpa function output
    
    Given:
    single triad OVERHEAD (OH) - optional arguments: -dpa 3
    single triad UNDERGROUND (UG) - optional arguments: -dpa 3
    double triad OVERHEAD (OH) - optional arguments: -dpa 3
    '''
    calculated_dpa_single_OH = calculations.main_dpa(eg_input_single_OH[0], eg_input_single_OH[3], eg_input_single_OH[4], eg_input_single_OH[5], eg_input_single_OH[6])
    calculated_dpa_single_UG = calculations.main_dpa(eg_input_UG[0], eg_input_UG[3], eg_input_UG[4], eg_input_UG[5], eg_input_UG[6])
    calculated_dpa_double_OH = calculations.main_dpa(eg_input_double_OH[0], eg_input_double_OH[3], eg_input_double_OH[4], eg_input_double_OH[5], eg_input_double_OH[6])
    assert np.isclose(calculated_dpa_single_OH, eg_output_single_OH[6])
    assert np.isclose(calculated_dpa_single_UG, eg_output_UG[6])
    assert np.isclose(calculated_dpa_double_OH, eg_output_double_OH[6])
