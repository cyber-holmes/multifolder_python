#impot modules
import os
import getpass
#create path
a="c:\\Users\\"
b=getpass.getuser()
c="\\Desktop"
d=a+b+c
os.chdir(d)
#path done

#create folder
j="haha"
for i in range(20):
  m=str(i)
  k=j+m 
  os.mkdir(k)