# You have a class of students.
# Ask the user to enter the mark of every student repeatedly.
# Determine if it is a fail, pass or distinction.
# Use a negative value as the sentinel value.
# Use a function to display whether a student failed or passed.

def results(mark=0):
    if mark < 50:
        result = "The student has failed."
        return result
    elif mark >= 50 and mark < 80:
        result = "The student has passed."
        return result
    elif mark >= 80:
        result = "The student has a distinction."
        return result

mark = int(input("Enter a mark: "))

while mark != -1:
    result = results(mark)
    print(result)
    mark = int(input("Enter a mark: "))
    