import os.path
py_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(py_path, "input.txt")
with open(txt_path, 'r') as file:
    sum = 0
    for line in file: # For every line in the file
        line = line.strip() # Remove the \n so it doesnt freak out
        length = len(line) 
        max_sequence = ""
        last_used_index = 0
        for minimum_remaining_characters_needed in range(11,-1,-1): # To Ensure theres always enough numbers 
            max_char_seen = ""
            temp = -1
            for index,char in enumerate(line[last_used_index:length-minimum_remaining_characters_needed]): # For every character in the reduced line
                if char > max_char_seen: # Find the largest character
                    max_char_seen = char
                    temp = last_used_index + index + 1
            last_used_index = temp #Reduce size of input
            max_sequence += max_char_seen # Add largest character to sequence

        sum += int(max_sequence)
    print(sum)

