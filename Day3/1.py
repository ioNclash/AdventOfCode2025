import os.path
py_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(py_path, "input.txt")
with open(txt_path, 'r') as file:
    sum = 0
    for line in file:
        previous=0
        maxi=0
        for char in line.strip():
            total = previous*10 + int(char)
            if total > maxi:
                maxi = total
            if int(char) > previous:
                previous = int(char)
        sum+=maxi

print(sum)
            