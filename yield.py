# range is a function, how does one iterate through something that is a function?

# crete an empty list
students = []

def read_file():
    try:
#         new file variable
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read/open file")

# this function just returns a line from the file
def read_students(f):
    for line in f:
        print(line)
        yield line

read_file()
print(students)