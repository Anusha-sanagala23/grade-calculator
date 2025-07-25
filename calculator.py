def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def main():
    name = input("Enter student name: ")
    n = int(input("Enter number of subjects: "))
    total = 0

    for i in range(n):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        total += mark

    avg = total / n
    grade = calculate_grade(avg)

    print("\n--- Student Report ---")
    print(f"Name      : {name}")
    print(f"Total     : {total}")
    print(f"Average   : {avg:.2f}")
    print(f"Grade     : {grade}")

if __name__ == "__main__":
    main()
