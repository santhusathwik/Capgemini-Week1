str=input("Enter String")
vowel=con=sp=num=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel+=1
    elif i=='1'or i=='2'or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        num+=1
    elif i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*':
        sp+=1
    else:
        con+=1
print(f"Vowel:{vowel}\nConsonants:{con}\nSpecial Char:{sp}\nNumbers:{num}\n")