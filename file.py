my_text = "Hello "

name, newline = input("What is your name: "), "\n"

open_file = open("example.txt", "a") # if theres not already a existing file name example.txt then it will create one with that name

open_file.write(my_text + name.capitalize() + newline)

print("Created or have typed in the file")

input()
