import io  # so we can use the type
import logging
from contextlib import closing
# logging.basicConfig(__name__, level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class CSV(object):
    """
This program will read a csv file (passed as a string parameter) with open.
Then it will take the first line as comma seperated list of column names.
These will be the names in the dictionary.
The column names will also be stored in a list so it can be accessed
 sequentially with an index or for each loop.


"""
    def __init__( self, path:str ) -> None:
        """manages context for opening csv file
calls other methods involved in reading and parsing csv file.
Users should only need to call CSV("path/to/file.csv")
:param path:
"""
        self.path = path
        self.df = dict()
        self.headers = []
    
    def get_headers( self, f: io.TextIOWrapper ):
        """gets headers from the opened (by read_csv) csv file f
and initializes the data structure storing the headers.
The data structure is a dictionary with the header names as the keys and a list.
Must be called before reading any lines from f.
First line must include header lines.
Future extensions could allow setting default header names to
deal with files without a header line.

:param f: csv file object
:type f: io.TextIOWrapper (e.g. f = open("path"))

:return:
"""
        s = f.readline()
        l = s.split(",")
        self.headers = list(map(lambda x: x.strip(), l))
        self.df = dict( [ (x, []) for x in self.headers ] )
    
    def get_rows( self, f: io.TextIOWrapper ):
        """
        
        :param f: csv file object
        :type f: io.TextIOWrapper
        :return:
        """
        line_number = 1 # counts from one so text editors show the right line
        for line in f:
            l = [ x.strip() for x in line.strip().split(',')]
            nheaders = len(self.headers)
            if nheaders == 0:
                self.headers = ["col" + str(x) for x in range(len(l))]
                self.df = dict( [ (x, []) for x in self.headers ] )
                nheaders = len( self.headers )
            if len(l) != nheaders:
                logger.log(logging.DEBUG, )
                logger.log(logging.DEBUG, "line: {line_number}".format(line_number=line_number))
                logger.log(logging.DEBUG, str(l))
                logger.log(logging.DEBUG, self.headers)
                raise ValueError("wrong number of columns in line: {line_number}".format(line_number=line_number))
            for i, key in enumerate(self.headers):
                try:
                    num = float(l[i])
                    if num.is_integer():
                        num = int(num)
                    self.df[key].append(num)
                except ValueError:  # keep it as a string if it's not a float
                    self.df[key ].append(l[i ])
            # increment line counter
        line_number += 1
    def read_csv( self , header = True):
        """ reads the csv file specified in constructor and stores in
        dataframe-like data structure
        
        :return: None
        """
        with open(self.path, 'rt') as f:
            if header:
                self.get_headers(f)
            self.get_rows(f)
        