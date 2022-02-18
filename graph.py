# Explore the graphing tools covered in today’s lecture. See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.
import csv
import plotly.express as px

open_file = open('CupcakeInvoices.csv')
csvreader = csv.reader(open_file)

choco_count = 0
van_count = 0
straw_count = 0

choco_total = 0
van_total = 0
straw_total = 0

rows = []
for row in csvreader:
    rows.append(row)
    # print(row[2])
    if row[2] == "Chocolate":
        choco_count += 1
        choco_total += (float(row[3]) * float(row[4]))
    elif row[2] == "Vanilla":
        van_count += 1
        van_total += (float(row[3]) * float(row[4]))
    elif row[2] == "Strawberry":
        straw_count += 1
        straw_total += (float(row[3]) * float(row[4]))

print(choco_count,"$", "%.2f" %  choco_total)
print(van_count,"$", "%.2f" %  van_total)
print(straw_count,"$", "%.2f" %  straw_total)   

open_file.close()


cupcakes = ["Chocolate", "Vanilla", "Strawberry"]
fig = px.bar(x=cupcakes, y=[choco_total,van_total,straw_total],
             labels=dict(x="Cupakes", y="Sales in $"))

fig.show()

cupcakes = ["Chocolate", "Vanilla", "Strawberry"]
fig = px.bar(x=cupcakes, y=[choco_count,van_count,straw_count],
             labels=dict(x="Cupakes", y="# of Cupcakes Sold"))

fig.show()