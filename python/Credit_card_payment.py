'''
Date            Credited
23 Nov 2020     1.00
27 Nov 2020     2.00
01 Dec 2020		50.00	
02 Dec 2020		950.00
02 Dec 2020		2,000.00
02 Dec 2020		500.00
17 Dec 2020		500.00
23 Dec 2020		2,500.00
25 Jan 2021     4,000.00

'''
from datetime import date
import csv
import pandas

df = pandas.read_csv('account.csv')

print(df)
with open('account.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Coulumn names are {}'.format(", ".join(row)))
            line_count += 1
        else:
            print('\t{} works in the {} department, and was born in {}.'.format(row[0], row[1], row[2]))
            line_count +=1
    print('Processed {} lines.'.format(line_count))



today_date = date.today()
today = today_date.strftime("%B %d, %Y")
print(today)

total=10503
credit_card_number = int(input("Enter credit card number"))
a = int(input("Enter the amout you credited"))

def sum_credits(y):
    credit = total + y
    return credit

x = sum_credits(a)
print("Total Credited = {} to HDFC Credit card no {} at {}".format(x, credit_card_number, today))