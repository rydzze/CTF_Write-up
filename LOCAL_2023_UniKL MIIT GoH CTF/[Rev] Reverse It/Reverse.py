my_string = "My_Strings"  #before encode
my_result = ""

for i in range(0, len(my_string), 2):
    my_first_letter = ord(my_string[i]) << 8
    my_second_letter = ord(my_string[i + 1])
    my_final = chr(my_first_letter + my_second_letter)
    my_result += my_final

print(my_result) #after encode

# ----------------------------------------------------

encoded_string = "杯桵湩歬㈰㈳筎ㅣ敟剥癥牳ㅮ杽"
decoded_result = ""

for i in range(0, len(encoded_string)):
    my_first_letter = ord(encoded_string[i])
    second_char = chr(my_first_letter & 0xFF)
    first_char = chr((my_first_letter >> 8) & 0xFF)
    decoded_result += first_char + second_char  

print(decoded_result)
