with open('output.txt', 'r') as file:
    lines = file.readlines()
keyword = 'ewe'
select_word = 'ewe'
modified_lines = []
for line in lines:
    if keyword in line:
        index = line.find(select_word)
        new_line = line[index+len(select_word):]
        modified_lines.append(new_line)
    else:
        modified_lines.append(line)
with open('out_new.txt', 'w') as file:
    file.writelines(modified_lines)
print('Output file created successfully!')