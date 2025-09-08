import os
def count_files(path="."):
    t_count=0
    p_count=0
    for file in os.listdir(path):
        if file.endswith(".txt"):
            t_count += 1
        elif file.endswith(".py"):
            p_count += 1
    print(f"Text files: {t_count}")
    print(f"Python files: {p_count}")
count_files(".")
