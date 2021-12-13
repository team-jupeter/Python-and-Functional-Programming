# 3.3.12 Other flavours of loops
# The middle-test loop
total = 0
while True: # while bool-expr:
    response = input("Enter the next number. (Leave blank to end)")
    if response == "" or response == "-1":
        break
    total += int(response)
print("The total of the numbers you entered is ", total)

# # Post-test loops
# while True:
#     play_the_game_once()
#     response = input("Play again? (yes or no)")
#     if response != "yes":
#         break
# print("Goodbye!")