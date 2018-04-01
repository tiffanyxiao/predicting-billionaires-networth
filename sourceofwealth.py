import csv

def main():
    # keep all rows in a variable
    rows = []
    # get all rows in csv file
    with open('oldBillionaires.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
    # get number of sources of wealth
    n = 0
    for row in rows:
        # different case if its the first row
        if n == 0:
            row.append("numsourceofwealth")
        else:
            # calculate number of commas in source of wealth column and add one for number of sources of wealth (numSOW)
            numSOW = row[23].count(',') + 1
            # add numSOW to row
            row.append(numSOW)
        n += 1
    # write the new csv file
    myFile = open('Billionaires.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(rows)

    print("Writing complete")
main()
