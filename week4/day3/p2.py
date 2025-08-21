import matplotlib.pyplot as plt

n=int(input("how many point do you want to plot:-"))
x=[]
y=[]
for i in range(n):
    xi=int(input(f"enter x coordinate {i+1}:"))
    yi=int(input(f"enter y coordinate {i+1}:"))
    x.append(xi)
    y.append(yi)
    
plt.plot(x,y,marker='*',color='red',linestyle='dotted')
plt.title("user input graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend
plt.show()
