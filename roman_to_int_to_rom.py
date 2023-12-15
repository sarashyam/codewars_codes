
    
    
def to_roman(val : int) -> str:
        
        if val == 0:  # there is no corresponding value for 0
            return ''
        symbols = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
        ]
        # eg: val = 14
        roman = '' # an empty string to store the roman number
        for value, symbol in symbols:  # accessing value and symbol ie. tuple (10, 'X')
            while val >= value: # 14 > 10
                roman += symbol # " " + 10
                val -= value #  14 - 10

        return roman

 
def from_roman(roman_num : str) -> int:
                    
            rom = {"I":1,"IV":4, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
            
            rom_str = roman_num
            
            if(len(rom_str) == 1): # if the string has only one letter then return the value of corresponding letter
                print(rom[rom_str])
                return rom[rom_str]
                exit()
            elif(len(rom_str) == 0): # if there is nothing return 0
                print(0)
                return 0
                exit()
                
            num_list = [] # list to store the letter values
            for i in rom_str:
                if i in rom.keys():
                    num_list.append(rom[i])

            print(num_list)
            sum = 0

            print(f"length of string {len(rom_str)}")
            
             #----------- initial checking------
            if (num_list[0] >= num_list[1]): # 500 > 100  D C
                    sum = num_list[0] + num_list[1] 
            elif (num_list[0] < num_list[1]): # 100 < 500  C D
                    sum = num_list[1] - num_list[0]
            #-------------------------------

            i = 1

            while i<(len(rom_str)-1): # starting iterating from index 1 
                if (num_list[i] >= num_list[i+1]):  
                    sum = sum + num_list[i+1] # follow same procedure as above 
                elif (num_list[i] < num_list[i+1]):
                        sum = (sum - num_list[i])+ (num_list[i+1] - num_list[i])
                i += 1

            print(sum) 
            return sum