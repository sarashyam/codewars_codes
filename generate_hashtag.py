
original_string = "  srfadfasdsghbFFF gfgfGG"
# if len(original_string) == 0 or -1:
#     print("false")
#     exit()
# original_string = original_string.strip()
# s = original_string.split(" ")
# lst =["#"] 
# for indx, word in enumerate(s):
#     st = f"{word[0].upper()}{word.lower()[1::]}"
#     lst.append(st)
# print(''.join(map(str, lst)))
# res = ''.join(map(str, lst))
# print(len(res))
# l = len(res)
# if l <= 140:
#     print(f"len {l} ress {res}")
# else :
#     print("flse")


#=========================================

#     if len(original_string) < 0:
#         return False
    # original_string = original_string.strip()
    # s = original_string.split(" ")
    
    # lst =["#"] 
    # for indx, word in enumerate(s):
    #     st = f"{word[0].upper()}{word.lower()[1::]}"
    #     lst.append(st)
    # res =''.join(map(str, lst))

    # return ''.join(map(str, lst))
    
if original_string == '':
    print("false")
lst =["#"] 
for  word in original_string.split():
        lst.append(word.capitalize())
res =''.join(map(str, lst))
l = len(res)
if l <= 140:
        print(f"len {l} ress {res}")

       
else :
        print("flse")
        