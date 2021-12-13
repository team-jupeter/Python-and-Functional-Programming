wordsfile = open("/usr/share/dict/words", "r")
wordlist = wordsfile.readlines()
print(wordlist[:6]) # ['\n', 'A\n', "A's\n", 'AOL\n', "AOL's\n", 'Aachen\n']