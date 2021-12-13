with open("test.txt", "r") as my_new_handle:
    for the_line in my_new_handle:
        # Do something with the line we just read.
        # Here we just print it.
        print(the_line, end="")
        print(the_line)

mynewhandle = open("wharrah.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: "wharrah.txt"