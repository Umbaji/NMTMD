with open('out_new.txt', 'r', errors='ignore') as file:
    lines = file.readlines()
keyword = '1.'
select_word = '1.'
modified_lines = []
for line in lines:
    if keyword in line:
        index = line.find(select_word)
        modified_lines.append(line[index:])
    else:
        modified_lines.append(line)
with open('out_new_new1.txt', 'w') as file:
    file.writelines(modified_lines)
print('Output file created successfully!')