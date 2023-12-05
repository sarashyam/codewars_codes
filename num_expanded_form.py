'''
You will be given a number and you will need to return it as a string
expanded_form(70304) # Should return '70000 + 300 + 4'

'''

def expanded_form(num):
        lst = [] # to store the values
        l = len(str(num)) # getting the lenght of num by converting to string

        for indx, dig in enumerate(str(num)):
            dig = int(dig) # converting to digit to perform the calculation
            if dig != 0: # doing operation if the digit is not 0
                print(indx)
                lst.append(dig*(10**((l-indx)-1))) # appending to list the 0's to be added 
                print(lst)
        result_string = ' + '.join(map(str, lst))  # converting to string and joining them by +
        print(result_string)
        return result_string

expanded_form(70304)