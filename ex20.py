from sys import argv
script,input_file= argv

def print_all(f):     #f means formatted  or a manner as to make it easy to read
    print(f.read())   # its read & return it as a string(in txt mode)
    
def rewind(f):     #repostions the file pointer associated with stream to the starting of the file
    f.seek(0)     #its position at beginning of file

def print_a_line(line_count, f):                  #
    print(line_count, f.readline())

current_file = open(input_file)
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file )

