song = "The rain in Spain..."
words = song.split()
words # ['The', 'rain', 'in', 'Spain...']

song.split("ai") # ['The r', 'n in Sp', 'n...']

print(song)

glue = ";"
phrase = glue.join(words)
phrase # 'The;rain;in;Spain...'

print(words)

" --- ".join(words) # 'The --- rain --- in --- Spain...'
"".join(words) # 'TheraininSpain...'