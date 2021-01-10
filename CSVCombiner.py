import pandas as pd

list_names = []
list_number = []
combined = ''

number_of_lists = int(input('Please enter number of CSVs to combine: '))

for i in range(number_of_lists):
    # set the list variable  TODO: make this an input later
    user_input = input('Please enter a CSV: ')
    user_input = user_input.replace(",", '.')
    list_names.append(user_input)
    list_number.append(pd.read_csv(list_names[i]))

    print(list_number[i], '\n')

    if i == 1:  # i is how many times the list is combined in this if statement
        combined = pd.merge(list_number[i-1], list_number[i])
        print('Combined:\n', combined)
    elif i > 1:  # this should let it go for however many you have
        combined = pd.merge(combined, list_number[i])
        print('Combined:\n', combined)

user_sorted = input('What would you like your new list ordered by? ')

output = combined.sort_values(by=user_sorted)

print('FINAL OUTPUT =\n', output)


