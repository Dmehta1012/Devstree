import json
import os
data=[]

def write_json():
    with open(r'C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day4\demo2.json','w') as f:
        json.dump(data,f)
        print("date written successfully")

def read_json():
    with open(r'C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day4\demo2.json','r') as f :
        data=json.load(f)
        print("Read data from json file:")
        print(data)
# write_json()
# read_json()

def update_json():
    # upd=input("Do you want to update the data(y/n): ")
    # if upd.lower()!='y':
    #     return
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))      
    city=input("Enter your city: ")
    # data.append({"name": name, "age": age, "city": city})
    with open(r'C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day4\demo2.json','r') as f :
        data=json.load(f)
    # Update the data with new entry
    data.append({"name": name, "age": age, "city": city})
    with open(r'C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day4\demo2.json','w') as f:          
        json.dump(data,f)
        print(data)
        print("Data updated successfully")
def remove_json():
    filename =r"C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day4\demo2.json"
    if os.path.exists(filename):
        os.remove(filename)
        print("🗑️ JSON file deleted successfully")
    else:
        print("⚠️ JSON file does not exist")
        

# read_json()
# write_json()
# update_json()
# remove_json()

def main():
    while True:
        print("1.Write json")
        print("2.Read json")
        print("3.Update json")
        print("4.Remove json")
        print("5.Exit")
        
        choice=int(input("Enter your choice:"))
        if choice==1:
            name=input("Enter your name: ")
            age=int(input("Enter your age: "))
            city=input("Enter your city: ")
            print(data.append({"name": name, "age": age, "city": city}))
            write_json()
        elif choice==2:
            read_json()
        elif choice==3:
            update_json()
        elif choice==4:
            remove_json()
        elif choice==5:
            break   
        else:
            print("Invalid choice")
main()