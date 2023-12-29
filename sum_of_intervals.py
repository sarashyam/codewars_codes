# def sum_of_intervals(lst):

#     sum = 0
#     for ele in lst:
#         sum += abs(ele[0] - ele[1])
#     print(sum)


# lst =[
#     [1, 5], 
#     [10, 20], 
#    [1, 6], 5
#    [16, 19],
#    [5, 11]
#     ]   
# sum_of_intervals(lst)

def sum_intervals(intervals):
    if not intervals:
        return 0

    # Sort intervals based on the starting pointstha
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize the result with the length of the first interval
    result = sorted_intervals[0][1] - sorted_intervals[0][0]

    # Iterate through the sorted intervals to find non-overlapping intervals
    for i in range(1, len(sorted_intervals)):
        current_start, current_end = sorted_intervals[i]
        previous_start, previous_end = sorted_intervals[i - 1]

        # If the current interval overlaps with the previous one, adjust the result
        if current_start <= previous_end:
            result += max(0, abs(current_end - previous_end))
        else:
            result += abs(current_end - current_start)

    return result

# Example usage:
intervals = [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
]

result = sum_intervals(intervals)
print(result)  # Output: 7
