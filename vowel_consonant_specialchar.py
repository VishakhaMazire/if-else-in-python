ch = input("Enter a character: ")
if (ch=='@' or ch=='#' or ch=='!' or ch=='_'):
    print(ch, "special character")
elif(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")