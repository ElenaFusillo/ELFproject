# import numpy as np
# import hypothesis.strategies as st
# from hypothesis import given, settings

#import pytest
from B_field import cli


def test_main_single(capsys, eg_input_single_OH_conf_file):
    '''
    This test verifies that the CLI (command line interface), given the proper
    input of a single triad OVERHEAD (OH), returns what is expected to.
    '''
    cli.main(eg_input_single_OH_conf_file)
    out, err = capsys.readouterr()
    assert out == 'In point of coordinates ( -20.5 , 1.0 ), the magnetic induction is  2.99  microTesla.\n'
    assert err == ''

def test_main_double(capsys, eg_input_double_OH_conf_file):
    '''
    This test verifies that the CLI (command line interface), given the proper
    input of a double triad OVERHEAD (OH), returns what is expected to.
    '''
    cli.main(eg_input_double_OH_conf_file)
    out, err = capsys.readouterr()
    assert out == 'In point of coordinates ( -5.0 , 1.0 ), the magnetic induction is  21.95  microTesla.\n'
    assert err == ''
