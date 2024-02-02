# lis = [5,9,1,3,2,8]
# for i in range(len(lis)):
#     print(f"value of i {i}")
#     for j in range(i-1 ,-1,-1):
#         print(j)
#         if lis[j+1]> lis[j]:
#             lis[j+1], lis[j] = lis[j],lis[j+1]

# print(lis)           

# import pandas as pd

# # Creating a DataFrame with some sample data
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'San Francisco', 'Los Angeles'],
#         'Cit': ['New York', 'San Francisco', 'Los Angeles']}

# df = pd.DataFrame(data)

# # Displaying the DataFrame
# # print(df)
# print(len(df.head()))
# print(len(df.columns))

# print(df[df["Age"]==30][["Name","City"]])

low = 100
high = 13000

result = []
    
    # Loop through each possible starting digit
for start_digit in range(1, 10):
        num = start_digit
        next_digit = start_digit + 1
        
        # Continue adding digits until the number exceeds the upper limit
        while num <= high and next_digit <= 9:
            num = num * 10 + next_digit
            next_digit += 1
            
            # If the current number is within the specified range, add it to the result
            if low <= num <= high:
                result.append(num)

print( result)
    