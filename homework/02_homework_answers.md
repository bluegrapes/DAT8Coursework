## Class 2 Homework: Command Line Chipotle [Solutions]
### This document describes the solutions.

**Command Line Tasks:**

> 1. Look at the head and the tail of **chipotle.tsv** in the **data**
> subdirectory of this repo. Think for a minute about how the data is
> structured. What do you think each column means? What > do you think each row
> means? Tell me! (If you're unsure, look at more of the file contents.)

```
$ head data/chipotle.tsv
$ tail data/chipotle.tsv

The column represents the attributes, features of a purchase item.
The row represents a purchase item in the order.  
```

> 2. How many orders do there appear to be?

```
$  cut -f1 data/chipotle.tsv | uniq | wc -l
1835

Minus the header line "order_id", there appears to be 1834 orders.
```

> 3. How many lines are in this file?

```
$ wc -l data/chipotle.tsv
4623

And this returns 4623 lines
```

> 4. Which burrito is more popular, steak or chicken?

```
$ grep 'Chicken Burrito' data/chipotle.tsv | wc -l
553

$ grep 'Steak Burrito' data/chipotle.tsv | wc -l
368

Chicken Burrito is more popular

```


> 5. Do chicken burritos more often have black beans or pinto beans?

```
$ grep 'Chicken Burrito' data/chipotle.tsv | grep 'Pinto Beans' | wc -l
105

$ grep 'Chicken Burrito' data/chipotle.tsv | grep 'Black Beans' | wc -l
282

It appears that Chicken Burrito with Black Beans is more often ordered.

```

> 6. Make a list of all of the CSV or TSV files in the DAT8 repo (using a single
> command). Think about how wildcard characters can help you with this task.

```
$ ls data/*.tsv data/*.csv
data/airlines.csv  data/chipotle.tsv  data/sms.tsv
```



> 7. Count the approximate number of occurrences of the word "dictionary"
> (regardless of case) across all files in the DAT8 repo.

```
$ grep -rio 'dictionary' ../DAT8 | wc -l
15

There are 15 occurences
```


> 8. **Optional:** Use the the command line to discover something "interesting"
> about the Chipotle data. Try using the commands from the "advanced" section!

```
$ for i in `seq 1 15`; do cut -f 1,2 data/chipotle.tsv | uniq -c | grep "$i " | wc -l; done
403
1039
448
123
28
11
0
5
0
1
1
1
0
1
0

This commands query the number of items per order. From the results it appears
that most orders include only 2 purchase items (1039 orders), followed by 3
items (448 orders), and 1 item (403 orders)
```
