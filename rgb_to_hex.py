red, green , blue = -20, 275, 125
if red < 0:
    red = 0
elif red > 255:
    red = 255
if blue < 0:
    blue = 0
elif blue > 255:
    blue = 255
if green < 0:
    green = 0
elif green > 255:
    green = 255

hex_color = "{:02X}{:02X}{:02X}".format(red, green, blue)
print(hex_color)