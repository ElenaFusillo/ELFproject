from B_field import cli


def test_single_point_bidim_dpa(capsys, eg_input_single_conf_file, eg_output_single_point_bidim_dpa):
    '''
    This test verifies that the CLI (command line interface), given the proper
    input of a single triad, returns what is expected to in case of
    optional arguments: -point -bidim -dpa 3
    '''
    cli.main(eg_input_single_conf_file)
    captured = capsys.readouterr()
    assert captured.out == eg_output_single_point_bidim_dpa
    assert captured.err == ''


def test_double_point_bidim_dpa(capsys, eg_input_double_conf_file, eg_output_double_point_bidim_dpa):
    '''
    This test verifies that the CLI (command line interface), given the proper
    input of a double triad, returns what is expected to in case of
    optional arguments: -point -bidim -dpa 3
    '''
    cli.main(eg_input_double_conf_file)
    captured = capsys.readouterr()
    assert captured.out == eg_output_double_point_bidim_dpa
    assert captured.err == ''
