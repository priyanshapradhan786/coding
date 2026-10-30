print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter your name: ")

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks in {subject}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

subjects = ["Subject 1", "Subject 2", "Subject 3",
            "Subject 4", "Subject 5"]

total = 0

for subject in subjects:
    total += get_marks(subject)

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n===== STUDENT RESULT =====")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")