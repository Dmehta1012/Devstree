i=1
n=int(input("how many details you wnat to enter"))
for i in range(n):
    dic={
    "name":str(input("enter your name ")),
    "phone_number":int(input("enter your Phone number")),
    "city":str(input("Enter your city ")),
    "pincecode":int(input("enter your pincode"))
}
    print(f" you enter {i+1} information",dic)

