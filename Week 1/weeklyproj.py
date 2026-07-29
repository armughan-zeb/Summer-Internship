def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


def main():
    print("===== Student Grade Calculator =====")

    while True:
        try:
            name = input("Enter Student Name: ")
            marks = float(input("Enter Marks (0-100): "))

            if marks < 0 or marks > 100:
                raise ValueError

            grade = calculate_grade(marks)

            print("\n----- Result -----")
            print("Student Name :", name)
            print("Marks        :", marks)
            print("Grade        :", grade)
            print("------------------")
            break

        except ValueError:
            print("Invalid input! Please enter marks between 0 and 100.\n")


if __name__ == "__main__":
    main()