import pandas as pd

#file_path = 'input.txt'
file_path = "/home/travis/build/aml-spring-19/homework-1-MingfengKeith/task1/input.txt"

data = pd.read_csv(file_path,encoding='utf-16', header=0, na_values=["--","NA"], escapechar = '\\',index_col=0, error_bad_lines = False)

def test_input():
    assert data.shape[0] == 225
    assert data.shape[1] == 31


def test2_input():
    assert int(data['2010'].sum()) == 7065
