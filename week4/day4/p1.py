import requests
p={'name':'Devarsh Mehta','age':20,'city':'Ahmedabad'}
r=requests.get("https://httpbin.org/get",params=p)
print(r.url)
