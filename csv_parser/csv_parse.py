from contextlib import closing
import io # so we can use the type
"""
This program will read a csv file (passed as a string parameter) with open.
Then it will take the first line as comma seperated list of column names. These will be the names in the dictionary.
The column names will also be stored in a list so it can be accessed sequentially with an index or for each loop.


"""

class CSV(object): # explicit is better than implicit
	def __init__( self, path ):
		self.path = path
		self.df = dict()
		self.headers = []
	
	def get_headers( self, f: io.TextIOWrapper ):
		"""
		gets headers from the opened (by read_csv) csv file f and initializes the datastructure storing the headers.
		The data structure is a dictionary with the header names as the keys and a list.
		Must be called before reading any lines from f.
		First line must include header lines.
		Future extensions could allow setting default header names to deal with files without a header line.
		
		:param f: csv file object
		:type f: io.TextIOWrapper (e.g. f = open("path"))
		
		:return:
		"""
		s = f.readline()
		l = s.split(",")
		self.headers = list(map(lambda x: x.strip(), l))
		self.df = dict([(x, []) for x in self.headers])
		return None
	
	def get_rows( self, f: io.TextIOWrapper ):
		"""
		
		:param f: csv file object
		:type f: io.TextIOWrapper
		:return:
		"""
		return None
	
	def read_csv( self ):
		"""
		manages context for opening csv file and calls other methods involved in reading and parsing csv file.
		Users should only need to call CSV("path/to/file.csv").read_csv()
		:return:
		"""
		
		return None
	
	