with open("friends.txt", "r") as input_file:
    all_lines = input_file.readlines()

all_lines.sort()

with open("sortedfriends.txt", "w") as output_file:
    for line in all_lines:
        output_file.write(line)