# x=open('./sample.txt','r') #file opening
# op=x.read()
# op=x.readline()
# op2=x.readline()
# op3=x.readline()
# print(op)
# print(op2)
# print(op3)

# print(x.closed) #checking before closing
# x.close()
# print(x.closed) #checking after closing
# i=1
# for line in x:
#     if i==2 or i==5:
#         print(line)
#     i+=1
#read,readline,readlines
# op=x.readlines()
# print(op)

#write mode
# try:
#     f=open('basic1.txt','r')    
#     op=f.read()
#     print(op)
# except FileNotFoundError:
#     print('file is not available')
# except:
#     print('something went wrong')

#in write mode-->if file is not available then it will create

# f=open('basic.txt','w')
# f.write('something')
# f.close()
#manual closing
#write--->re write the content in the file

#with statement
# with open('basic.txt','r') as f:
#     op=f.read() 
#     print(op)
# print(f.closed)


# with open('basic.txt','w') as f:
#     f.writelines(['a\n','b\n','c\n','d\n'])


#w mode--->re write the content in the file

with open('basic.txt','a') as f:
    f.writelines(['a\n','b\n','c\n','d\n'])

#a mode--->update the existing file with new data

