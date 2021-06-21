word=input("Enter your word: ")
count=0
i=0
while i<len(word):
    if word[i] in ("a","e","i","o","u"):
        count=count+1
    i=i+1
print(count,"is count")

# count1 = 0  
# count2 = 0
# str = "anzum"
# for i in range(0,len(str)):   
#     if str[i] in ('a',"e","i","o","u"):  
#         count1 = count1 + 1 
#     elif (str[i] >= 'a' and str[i] <= 'z'):  
#         count2 = count2 + 1
# print("Total number of vowel and consonant are" )  
# print(count1,"vowel count")
# print(count2,"consonant count")