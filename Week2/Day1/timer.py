import time
def countdown(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)
    print("Time’s up!")
countdown(5)
