import math
import statistics
scores=list(map(int,input("ENter list elements : ").split(" ")))
print("Mean : ",sum(scores)/len(scores))
print("Median : ",statistics.median(scores))
print("Mode : ",statistics.mode(scores))
