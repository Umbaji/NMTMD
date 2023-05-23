with open('out.txt, 'r') as file:
    lines = file.readlines()
keyword = 'ewe'
select_word = 'ewe'
for line in lines:
    if keyword in line:
        index = line.find(select_word)
        new_line = line[index+len(select_word):]
        print(new_line)