import pandas as pd

# set the list variable  TODO: make this an input later
list1name = 'list1.csv'
list2name = 'list2.csv'
list3name = 'list3.csv'

list1 = pd.read_csv(list1name)
list2 = pd.read_csv(list2name)
list3 = pd.read_csv(list3name)

print(list1, "\n")
print(list2, '\n')
print(list3, '\n')

combined = pd.merge(list1, list2)
combined = pd.merge(combined, list3)

print(combined, '\n')

output = combined.sort_values(by='Login')

print(output)


