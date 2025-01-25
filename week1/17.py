file={}
sent=input("Enter the sentence: ").split()
for i in sent:
    if(i not in file):
        file[i]=1
    else:
        file[i]+=1
print(file)