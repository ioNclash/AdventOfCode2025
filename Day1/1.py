pos = 50
count = 0
import os.path

py_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(py_path, "input.txt")

with open(txt_path, "r") as file:
    for line in file:
        pos += -int(line[1:]) if line[0] == "L" else int(line[1:]) # Move negative if left
        pos%=100 # Loop back around
        if pos==0: count+=1
print(f"The Safe password is {count}!")
# Answer was 964

