def two_sum(numbers, target):
    
    a=1
    for num in numbers:
            print(len(numbers))
            diff_val = target - num 
            ind = numbers.index(num)
            print(f"num {num}, diff value {diff_val}")
            if diff_val in numbers:
                if numbers.index(diff_val) == ind: 
                    a = ind, reversed_index = len(numbers) - 1 - numbers[::-1].index(diff_val), numbers.index(diff_val)
                else:
                    a = ind, numbers.index(diff_val)
                print(a)
                if a[0] == a[1]:
                    continue
                break
            
            
    return a

z = two_sum([1234,5678,9012], 14690)
print(z)