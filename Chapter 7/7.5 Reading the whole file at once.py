with open("somefile.txt") as f:
    content = f.read()

words = content.split()
print(f"There are {len(words)} words in the file.")

def filter(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            # Put any processing logic here
            if not line.startswith('#'):
                outfile.write(line)