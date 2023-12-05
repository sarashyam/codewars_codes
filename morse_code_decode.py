MORSE_CODE = {'.-':'A', '--...':'7', '...-..-': '$' }
print(MORSE_CODE['.-'] )
print(MORSE_CODE['--...'])
print(MORSE_CODE['...-..-'])
print(MORSE_CODE.keys())

morse_code = "  .- --... ...-..-   ...-..- ...-..- ...-..- .- .-   .-      "
morse_code1 = morse_code.strip()
print(morse_code1)
outer_list = [inner.split(" ") for inner in morse_code1.split("   ")]
print(outer_list)

string_list = []

for index,inner_list in enumerate(outer_list):
    for element in inner_list:
        print("Element:", element)
        if element in MORSE_CODE.keys():
            string_list.append(MORSE_CODE[element])
    if index != (len(outer_list) -1) :    
        string_list.append(" ")

print(string_list)
result_string = "".join(string_list)
print(result_string)