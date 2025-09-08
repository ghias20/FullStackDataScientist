def longest_word(a):
    word=a.split()
    b=max(word,key=len)
    return b
a=input("Enter a sentence to find longest word : ")
print(longest_word(a))