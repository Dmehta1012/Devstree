with open("practice.txt","w") as f:
    f.write("hi everyone\n we are learning File I/o")
    f.write("\n Using java\n I like programming in java")
with open("practice.txt","r") as f:
    data = f.read()
    print("Before changing Text File \n",data)
n_data=data.replace("java","Pyhton")
print("\nAfter chaning text file\n",n_data)

with open("practice.txt","w") as f:
    f.write(n_data) 

with open("practice.txt","r") as f:
    data = f.read()
    print("\nNumber for word Use :-",data.count("java"))
    print("\nWord (found/not Found) in paragrph")
    if (data.find("learning")!=-1):
        print("found")
    else: 
        print("not found")


