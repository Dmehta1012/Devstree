import json
data=[]
name=input("Enter your name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")
print(data.append({"name": name, "age": age, "city": city}))
def write_json():
    with open('demo1.json','w') as f:
        json.dump(data,f)
        print("date written successfully")

def read_json():
    with open('demo1.json','r') as f :
        data=json.load(f)
        print("Read data from json file:")
        print(data)
write_json()
read_json()

# def update_json():
#     with open('demo1.json','r') as f :
#         data=json.load(f)
#         data["hobby"]="gaming"
#         data["age"]=21
#     with open('demo1.json','w') as f:          
#         json.dump(data,f)
#         print(data)
#         print("Data updated successfully")
        
        

read_json()
write_json()
# update_json()