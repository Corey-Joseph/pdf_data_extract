import camelot

#state file name
#must be in working directory folder
file = "Table.pdf"

#READ pdf
tables = camelot.read_pdf(file)

#How many tables read?
print("Total tables extracted:", tables.n)

#Print first table
print(tables[0].df)

#Export table to csv file
tables.export("test.csv", f="csv")
#OR
#tables[0].to_excel("test.xlsx")