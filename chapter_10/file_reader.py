filepath = 'chapter_10/text_file/pi_digits.txt'

with open(filepath) as file_object:
    lines = file_object.readlines()    

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
