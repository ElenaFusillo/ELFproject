from B_field import cli


def test_single_point_bidim_dpa(capsys, eg_input_single_conf_file, eg_output_single_point_bidim_dpa):
    '''
    Tests:
    CLI output

    Given:
    single triad, optional arguments: -point -bidim -dpa 3
    '''
    cli.main(eg_input_single_conf_file)
    captured = capsys.readouterr()
    assert captured.out == eg_output_single_point_bidim_dpa
    assert captured.err == ''


def test_double_point_bidim_dpa(capsys, eg_input_double_conf_file, eg_output_double_point_bidim_dpa):
    '''
    Tests:
    CLI output

    Given:
    double triad, optional arguments: -point -bidim -dpa 3
    '''
    cli.main(eg_input_double_conf_file)
    captured = capsys.readouterr()
    assert captured.out == eg_output_double_point_bidim_dpa
    assert captured.err == ''
