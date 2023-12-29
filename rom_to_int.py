

rom = {"I":1,"IV":4, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

rom_str = "MDCCCXCII"
if(len(rom_str) == 1):
    print(rom[rom_str])
    exit()
elif(len(rom_str) == 0):
    print(0)
    exit()
num_list = []
for i in rom_str:
    if i in rom.keys():
        num_list.append(rom[i])
    
print(num_list)
sum = 0

print(f"length of string {len(rom_str)}")

if (num_list[0] >= num_list[1]):
        sum = num_list[0] + num_list[1]
elif (num_list[0] < num_list[1]):
        sum = num_list[1] - num_list[0]
        
i = 1

while i<(len(rom_str)-1):
    if (num_list[i] >= num_list[i+1]):
        sum = sum + num_list[i+1]
    elif (num_list[i] < num_list[i+1]):
            sum = (sum - num_list[i])+ (num_list[i+1] - num_list[i])
    i += 1
            
print(sum)  