''' 
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).
'''

def two_sum(numbers, target):
    
    # a=1
    # for num in numbers:
    #         print(len(numbers))
    #         diff_val = target - num 
    #         ind = numbers.index(num)
    #         print(f"num {num}, diff value {diff_val}")
    #         if diff_val in numbers:
    #             if numbers.index(diff_val) == ind: 
    #                 a = ind, reversed_index = len(numbers) - 1 - numbers[::-1].index(diff_val), numbers.index(diff_val)
    #             else:
    #                 a = ind, numbers.index(diff_val)
    #             print(a)
    #             if a[0] == a[1]:
    #                 continue
    #             break
            
            
    # return a

    for i, num in enumerate(numbers):
        diff_val = target - num
        if diff_val in numbers[i + 1:]:
            return i, numbers.index(diff_val, i + 1)
    return None




z = two_sum([1234,5678,9012], 14690)
print(z)