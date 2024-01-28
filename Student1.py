def calculate_grade(score):
    if score >= 90:
        grade = "A"
    else:
        grade = "Undefined"
    return grade

def main():
    # Prompt the user to enter the student's score
    score = float(input("Enter the student's score: "))

    # Calculate the grade based on the score
    grade = calculate_grade(score)

    # Print out the corresponding grade
    print(f"The corresponding grade for the score {score} is: {grade}")

if __name__ == "__main__":
    main()
