# def format_duration(seconds):
seconds = 132030240
if seconds == 0:
         print("now")
lst =[]
year = seconds // (360*24*60*60)
if year != 0:
        lst.append(f"{year} years" if year>1 else f"{year} year")
rem = seconds % (360*24*60*60)
    
days = rem // (24*60*60)
if days != 0:
        lst.append(f"{days} days" if days>1 else f"{days} day")  
rem = rem % (24*60*60)
    
hours = rem // (60*60)
if hours != 0:
        lst.append(f"{hours} hours" if hours>1 else f"{hours} hour")  
rem = rem % (60*60)
    
min = rem // (60)
if min != 0:
        lst.append(f"{min} minutes" if min>1 else f"{min} minute")  
sec = rem % (60)
if sec != 0:
        lst.append(f"{sec} seconds" if sec>1 else f"{sec} second")  
    
print(lst)
result = ""
if (len(lst)>1):
    result += ", ".join(lst)
    print(result)
    
    replacement = " and "

    # Split the string from the right side at the first occurrence of ", "
    parts = result.rsplit(", ", 1)

    # Join the parts back together with the replacement
    result = replacement.join(parts)
   
    
elif  len(lst)==1:
    result = "".join(lst)
print(result)

# format_duration(3662)

