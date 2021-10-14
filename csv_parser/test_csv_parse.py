import pytest
import io
import csv_parse

# easier to see when not on one long line
header_test1 = io.StringIO( "h1,h2,h3,h4,h5,h1n1" )
header_lst1 = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h1n1' ]
header_dkt1 = { 'h1': [], 'h2': [], 'h3': [], 'h4': [], 'h5': [], 'h1n1': [] }
@pytest.mark.parametrize("f,expected_list, expected_dict", [ (header_test1, header_lst1, header_dkt1) ] )
def test_get_headers(f, expected_list, expected_dict):
	csv = csv_parse.CSV("empty/path")
	csv.get_headers(f)
	assert csv.headers == expected_list
	assert csv.df == expected_dict

# should strip white space
rows_test1 = io.StringIO(
	"""1,2,3,4,5,y
	6,7,8,9,10,y
	11,12,13,14,15,n""")
rows_dkt1 = {'h1': [1,6,11], 'h2': [2,7,12], 'h3': [3,8,13], 'h4': [4,9,14], 'h5': [5,10,15], 'h1n1': ['y','y','n']}

@pytest.mark.parametrize("f, expected_dict", [ (rows_test1, rows_dkt1) ] )
def test_read_lines(f, expected_dict):
	pass