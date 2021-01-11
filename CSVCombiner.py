import pandas as pd

list_names = []
list_number = []
combined = ''

# loop for exception handling
for x in range(3):
    # Ask user for number of lists to combine.
    number_of_lists = int(input('Please enter number of CSVs to combine: '))
    if number_of_lists > 1:
        for i in range(number_of_lists):
            # set the list variable  TODO make this into a popup entry box thing
            #                           Possibly a "browse files"

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

        # Ask the user what to sort list by and sort list
        user_sorted = input('What would you like your new list ordered by? ')
        output = combined.sort_values(by=user_sorted)

        # Print out the final list of combined lists and exit loop
        output.to_csv('CombinedCSV.csv', index=False)
        # print('FINAL OUTPUT =\n', output)
        print('Your lists have been combined and saved as: CombinedCSV.csv in the same location as this program.')
        exit()
    else:
        # Exception handling for attempting to combine < 1 CSV
        print('You must enter more than one CSV file to combine!')
        if (2 - x) == 0:
            print('You have run out of attempts! Please restart the program!')
        else:
            print('You have %s more tries!' % (2 - x))



