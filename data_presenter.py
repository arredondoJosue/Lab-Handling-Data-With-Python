import csv

open_file = open('CupcakeInvoices.csv')
csvreader = csv.reader(open_file)

# 1. Loop through all the data and print each row.

for row in open_file:
    print(row)


open_file.seek(0,0)

# 2. Loop through all the data and print the type of cupcakes purchased.

rows = []
for row in csvreader:
    rows.append(row)
    print(row[2])


open_file.seek(0,0)

# 3. Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

for row in csvreader:
    rows.append(row)
    qty = float(row[3])
    price = float(row[4])
    invoice_total = qty * price
    print("$", "%.2f" % invoice_total)    



open_file.seek(0,0)

# 4. Loop through all the data, and print out the total for all invoices combined.

total = 0

for row in csvreader:
    rows.append(row)
    qty = float(row[3])
    price = float(row[4])
    sub_total = qty * price
    total += sub_total
print("$", "%.2f" % total)    



# 5. Close your open file.

open_file.close()