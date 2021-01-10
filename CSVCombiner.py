import pandas as pd

# set the list variable  TODO: make this an input later
list1name = 'list1.csv'
list2name = 'list2.csv'

list1 = pd.read_csv(list1name)
list2 = pd.read_csv(list2name)

print(list1, "\n")

print(list2)



