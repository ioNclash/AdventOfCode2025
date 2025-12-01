pos = 50
count = 0
import os.path
py_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(py_path, "input.txt")
with open(txt_path, 'r') as file:
    for line in file:
        if line[0] == "L":
            move = -int(line[1:]) # If left invert negative
            next_pos = pos+move
            zero_adjustment = -1 if pos ==0 else 0 # Adjust for if the value goes negative but started at 0
            count+= (zero_adjustment) - (next_pos - 1) // 100 # Count how many times it wrapped past 0 going left
        else: 
            move =int(line[1:]) 
            next_pos = pos+move
            count += (next_pos)//100 # Count the ammount of times it must have gone past 99 going right
        pos= (next_pos)%100 # Loop back
print(f"The Safe password is {count}!") 
# Answer was 5872