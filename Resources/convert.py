import pandas as pd

a = pd.read_csv('cleaned.csv')

a.to_html('Table.htm')
html_file = a.to_html()