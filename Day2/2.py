import os.path
py_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(py_path, "input.txt")
with open(txt_path, 'r') as file:
    text = file.read()
    ranges = [range(int(start),int(end)+1) # Turn Text input into python ranges
              for start,end in (t.split("-")
              for t in text.split(","))]

sum = 0
for r in ranges:
    for i in r:
        s = str(i)
        if s in (s + s)[1:-1]:
            sum+=i
print(sum)