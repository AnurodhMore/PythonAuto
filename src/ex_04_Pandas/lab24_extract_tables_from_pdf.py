# need to install ->  tk, ghostscript, camelot-py
import camelot

tables = camelot.read_pdf('/Users/anurodhmore/Downloads/BlackRock_MASS_Income_Interview_Playbook.pdf',pages='3')
print(tables)

tables.export('MASS.csv', f='csv',compress=True)
tables[0].to_csv('MASS.csv')