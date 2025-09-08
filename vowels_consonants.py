def vowels_consonents(a):
    vcount=0
    ccount=0
    for char in a:
        if char in ['a','e','i','o','u']:
            vcount=vcount+1
        else:
            ccount=ccount+1
    return "The no of vowels are ",vcount," and the no of consonants are ",ccount
a=input("Enter a word to count vowels and consonants : ")
print(vowels_consonents(a))