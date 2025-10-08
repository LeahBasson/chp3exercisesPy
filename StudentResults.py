# class of five students.
# ask the user to enter the mark of every student.
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

for count in range(5):
    mark = int(input("Enter mark: "))
    result = results(mark)
    print("result:", result)
