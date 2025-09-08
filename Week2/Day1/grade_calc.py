def grade_calculator(marks):
    avg=sum(marks)/len(marks)
    if avg>=90:
        grade="A+"
    elif avg>=80:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=60:
        grade="C"
    elif avg>=50:
        grade="D"
    else:
        grade="F"
    return f"Grade:{grade}"
marks = list(map(int, input("Enter marks separated by space: ").split()))
print(grade_calculator(marks))
