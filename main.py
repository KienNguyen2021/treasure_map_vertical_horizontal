row1 = [" "," "," "]     # means : index 0
row2 = [" "," "," "]     # means : index 1
row3 = [" "," "," "]     # means : index 3

map = [row1,row2,row3]

position = input (" Where do you keep your treasure ? ") 
# if 23 - that string data type : means column 2, row 3 - index 0 is 2; index 1 is 3
# 2- column : index 0, index 1, index 2  - 3- row : index 0, index 1, index 2, index 3 doest not EXIST, so index 3 -1

horizontal = int(position [0])  # use int to convert this string into integer
vertical =  int(position [1])   # use int to convert this string into integer

#selected_row = map [horizontal -1]
#selected_row[horizontal -1] = "X"
# or another way :

map[vertical-1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

