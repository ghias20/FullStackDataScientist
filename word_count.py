a=input("Enter a sentence : ")
word=a.split()
print(word)
visited=[]
for i in range(0,len(word)):
    if word[i] not in visited:
        wcount=1
        for j in range(i+1,len(word)):
            if (word[i]==word[j]):
                wcount=wcount+1
        visited.append(word[i])
        print(word[i]," : ",wcount)