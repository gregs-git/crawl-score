import pandas as pd

url = 'http://crawl.akrasiac.org/scoring/top-N.html'

tables = pd.read_html(url)

print("There are : ",len(tables)," tables")
print("Take look at table 0")
print(tables[0])

