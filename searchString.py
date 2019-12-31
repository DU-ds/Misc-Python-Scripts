"""
searchString(argv, duckDuckGoURL)

argv: string in argv[1] correspoding to DuckDuckGo query
duckDuckGoURL: url for duck duck  go search engine. eg 
https://start.duckduckgo.com/
https://duckduckgo.com/
"""
def searchString(argv, duckDuckGoURL):
   from sys import argv

   search = argv[1]

   searchArr = search.split()
   # https://stackoverflow.com/questions/17222355/string-split-formatting-in-python-3
   # print (searchArr)
   # print(searchArr[0])
   # print(searchArr[len(searchArr) - 1])

   # alternate way of creating strings with +
   # query = "+"
   # query = query.join(searchArr)
   # print(query)

   # create string with + seperating words
   query = ""
   for s in searchArr:
      # add control flow (eg an if statement) to deal with quotes and other options
      query += s + "+"


   # https://stackoverflow.com/questions/1798465/python-remove-last-3-characters-of-a-string
   query = query[:-1] #get rid of trailing +

   print(query)

   finalQuery = duckDuckGoURL + "?q=" + query

   # print(finalQuery)
   # https://stackoverflow.com/questions/39212541/unable-to-pipe-python-output-to-program
   import sys
   print(finalQuery)
   sys.stdout.flush()
   return finalQuery