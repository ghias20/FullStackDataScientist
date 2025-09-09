import string
passwd=input("Enter password to check : ")
if len(passwd)==8:
    has_letter=any(ch in string.ascii_letters for ch in passwd)
    has_digit=any(ch in string.digits for ch in passwd)
    has_punctuation=any(ch in string.punctuation for ch in passwd)
    if has_letter and has_digit and has_punctuation:
        print("Valid Password.")
    else:
        print("Invalid Password.")
else :
    print("Invalid Password")
