import json

# with open('./data.json','w')as f:
#     cnvrt=str(ip)
#     f.write(cnvrt)

# with open('./data.json','r')as f:
#     data=f.read()
#     print(data)
#     print(type(data))
#     cnvrt=dict(data)
#     print(type(cnvrt))

# ip=[1,2,3,4,5]

# # with open('./data.json','w') as f:
# #     json.dump(ip,f)

# with open('./data.json','r') as f:
#     data=json.load(f)
#     print(data)
#     print(type(data))

# ip=['tejaswini','tarun','kusuma','mallesh','yashwasri']

# with open('./data.json','w')as f:
#     json.dump(ip,f)

# with open('./data.json','r') as f:
#     data=json.load(f)
#     print(data,type(data))

# ip=input('enter name :')
# with open('./data.json','r+') as f:
#     data=json.load(f)
#     print(data)
#     data.append(ip)
#     f.seek(0)
#     json.dump(data,f)

prod_info={"prod_name":input("enter prod name : "),"price":int(input("enter price : "))}
with open('./data.json','r+') as f:
    data=json.load(f)
    print(data)
    data.append(prod_info)
    f.seek(0)
    json.dump(data,f,indent=2)
