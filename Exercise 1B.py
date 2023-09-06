

def find_middle_3Char(string):
    mid_index = int(len(string)/2)
    processed_string = string[mid_index-1:mid_index+2]
    print(processed_string)

str1 = "JhonDipPeta"
str2 = "JaSonAy"

find_middle_3Char(str2)