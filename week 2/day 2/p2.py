s=input("Enter your sentence ")
wc={}

if s=="".strip(): 
    print()
else:
    for word in s.split():
        if word in wc:
            wc[word]+=1
        else:
            wc[word]=1
    print(wc)