import pytest
import io
import csv_parse

# easier to see when not on one long line
header_test1 = io.StringIO( "h1,h2,h3,h4,h5,h1a" )
header_lst1 = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h1a' ]
header_dkt1 = { 'h1': [], 'h2': [], 'h3': [], 'h4': [], 'h5': [], 'h1a': [] }
@pytest.mark.parametrize("f,expected_list, expected_dict", [ (header_test1, header_lst1, header_dkt1) ] )
def test_get_headers(f, expected_list, expected_dict):
	csv = csv_parse.CSV("empty/path")
	csv.get_headers(f)
	assert csv.headers == expected_list
	assert csv.df == expected_dict

#
@pytest.fixture
def csv_headers1():
	csv = csv_parse.CSV( "test1.csv" )
	csv.headers = header_lst1
	csv.df = header_dkt1
	yield csv
	del csv

@pytest.fixture
def csv_headers2():
	csv = csv_parse.CSV( "test2.csv" )
	yield csv
	del csv

# should strip white space
rows_test1 = io.StringIO(
	"""1,2,3,4,5,y
	6,7,8,9,10,y
	11,12,13,14,15,n""")
rows_dkt1 = {'h1': [1,6,11], 'h2': [2,7,12], 'h3': [3,8,13], 'h4': [4,9,14], 'h5': [5,10,15], 'h1a': ['y','y','n']}

@pytest.mark.parametrize("f, expected_dict", [ (rows_test1, rows_dkt1) ] )
def test_get_rows(csv_headers1, f, expected_dict):
	""""""
	csv_headers1.get_rows(f)
	assert expected_dict == csv_headers1.df
rows_dkt2 = {'col0': [1,6,11], 'col1': [2,7,12], 'col2': [3,8,13], 'col3': [4,9,14], 'col4': [5,10,15], 'col5': ['y','y','n']}
@pytest.mark.parametrize("expected_dict",[ (rows_dkt2) ])
def test_read_csv_headers_false(csv_headers2, expected_dict):
	csv_headers2.read_csv(header = False)
	assert csv_headers2.headers == [ "col0", "col1", "col2", "col3", "col4", "col5"]
	assert csv_headers2.df == expected_dict


@pytest.mark.parametrize("expected_list, expected_dict",[ (header_lst1, rows_dkt1) ])
def test_read_csv_headers_true(csv_headers1, expected_list, expected_dict):
	csv_headers1.read_csv( header = True )
	print(csv_headers1.headers)
	print(csv_headers1.df)
	assert csv_headers1.headers == expected_list
	assert csv_headers1.df == expected_dict
	