'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''
import csv

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
f = open('../data/chipotle.tsv', 'r')
file_nested_list = csv.reader(f, delimiter='\t')

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested_list.next()
data = [row for row in file_nested_list]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
print "PART 3 ******"
# check range, that there are no missing gaps in order_id
maxidx = int(data[len(data)-1][0])
assert(range(1, maxidx+1) == list(set([int(el[0]) for el in data]))), "missing gaps in order_id"
# ok, now calculate
total_orders = sum([float(row[4][1:]) for row in data])
print "average price of an order: %.2f" % (total_orders / float(maxidx))


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
print "PART 4 ******"
soda = [row[3][1:-1] for row in data if "Canned Soda" in row[2] or "Canned Soft Drink" in row[2]]
uniqsoda = list(set(soda))
print "unique sodas and soft drinks", uniqsoda


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
print "PART 5 ******"
bucket = {}
# get the distinct burrito, and toppings
burrito_orders = [[row[2], row[3]] for row in data if "Burrito" in row[2]]
for key, val in burrito_orders:
    if not key in bucket:
        bucket[key] = []
    # remove []
    val = val[1:-1]
    # find the toppings, remove the Salsa....
    toppings = val[val.find(", [")+3:-1]
    # add the counts to bucket
    bucket[key].append(len(toppings.split(',')))
# now print the average
for key in bucket:
    print key, "average toppings = %d" % (sum(bucket[key]) / len(bucket[key]))


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''