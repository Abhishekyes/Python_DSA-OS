#!/usr/bin/env python
# coding: utf-8

# In[16]:


a = "Abhishek is a good boy "


# In[4]:


# jumps and access
a[0:300:2]


# In[7]:


#access last
a[0:300:-1]


# In[8]:


#go negative side there is nothing
a[-1:-4]


# In[13]:


# reverse direction not define point
a[::-1]
a[-1::-1]


# In[17]:


a[-5:5]


# In[18]:


a[-5:5:-1]


# In[19]:


#find length
len(a)


# In[21]:


a*2


# In[22]:


a.find('a')


# In[27]:


l = a.split(" ")
l


# In[28]:


a.upper()


# In[29]:


a.title()


# In[30]:


a.capitalize()


# In[31]:


b = "it a good guy"


# In[32]:


b.join(a)


# In[35]:


" ".join("abhi")


# In[36]:


for i in reversed("abhi"):
    print(i)


# In[2]:


s = "Abhishek"


# In[42]:


#NOT working???
s.rstrip()


# In[43]:


s.lstrip()


# In[3]:


s.isupper()
s.isdigit()


# In[ ]:


s.endswith()
s.startwith()
s.istitle()#start with cap letter
s.encode()


# In[ ]:


#List


# In[ ]:


# mutable entity (change data any index)
#string indexes is immutable entity


# In[ ]:





# In[ ]:





# In[9]:


# List is collection of hetro or homo data
l = ["fsef",544,"dtecr",5,68,9,7,5,True,]


# In[10]:


type(s)


# In[11]:


l[0:4]


# In[12]:


l[::-1]


# In[19]:


l[-1:12]


# In[24]:


l[0][2]


# In[47]:


l1 = ["dfs","sdf","sfdd","sdf"]
l2=["sdf","sdf","dfs","ssff"]


# In[26]:


l1+l2


# In[27]:


l1+ ["kdkdkdkd"]


# In[28]:


l1*2


# In[31]:


l1[0] = "your name"


# In[32]:


l1


# In[42]:


a = "sudh"


# In[43]:


a.replace('s','v')


# In[44]:


a


# In[45]:


a[0]


# In[49]:


"kumar" in l1


# In[50]:


l1.append("abhishek")


# In[51]:


l1


# In[52]:


#defult -1 otherwise ive index 
l1.pop()


# In[53]:


l1


# In[54]:


l1.pop(2)


# In[55]:


l1


# In[56]:


l1.append(5145451)


# In[57]:


l1.insert(1,"no")


# In[58]:


l1


# In[59]:


l1.insert(1,["sdf","Sfs",4548,48])


# In[60]:


l1


# In[61]:


l1.reverse()


# In[62]:


l1


# In[63]:


l1[::-1]


# In[64]:


l1


# In[65]:


l1[4][2]


# In[67]:


l1.count('sdf')


# In[68]:


l1.append([1,5,8,6])


# In[69]:


l1


# In[70]:


l1


# In[71]:


# all element insert after last index
l1.extend([1,1,1,1,1,2,])


# In[72]:


l1


# In[76]:


for i in range(10,-5,-2):
    print(i)


# In[85]:


n =5 
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end ="")
    print("\r")


# In[87]:


t = (3,4,5,2,6,8,2,8,2)
len(t)


# In[90]:


for i in range(len(t)):
    print(i,t[i])


# In[95]:


t


# In[92]:


t[::-1]


# In[97]:


list(t)


# In[101]:


list(range(len(t)))


# In[100]:


for i in range(len(t)-1,-1,-1):
    print(i, t[i])


# In[ ]:


#Dictionary


# In[102]:


d = {"a":"dfsdf","d":[1,2,5,6,8]}


# In[104]:


d['d']


# In[105]:


for i in d:
    print(i,d[i])


# In[106]:


# kry+value return 
for i in d:
    print(i,d[i])


# In[109]:


for i in d.items():
    print(i)


# In[110]:


s = {1,2,5,4,3,6,5,8,4,9,287,6,59,2,8,5,928,8}


# In[111]:


s


# In[112]:


for i in s:
    print(i)


# In[114]:


a = 7

while i<7:
    pass


# In[115]:


for i in range(6):
    print("num")
    if i==2:
        continue
    print(i)


# In[ ]:





# In[ ]:


## loop use string  ..................................


# In[120]:


s = " this is a guy who want a good job"
len(s)


# In[117]:


# length with looop
count =0
for i in s:
    count+=1
print(count)


# In[122]:


for i in range(len(s)-1,-1,-1):
    #print(s[i])


# In[124]:


i = len(s)-1
while(i>=0):
    print(s[i],end=" ")
    i -=1


# In[128]:


a = "ineuron"
b = "Aeiou"


# In[129]:


for i in a:
    if i in b:
        print("vowel",i)
    else:
        print("not",i)


# In[130]:


"u" in "sudh"


# In[141]:


# palindrom string

x = list(range(len(s)-1))


# In[139]:


x


# In[1]:


k = "yeye"
for i in range(len(k)):
    if(k[i] != k[len(k)-i-1]):
        print("not P",k)
        #print(k[i],k[len(k)-i-1])
        break
else:
    print("yes",k)


# In[6]:


s =input()
s=k
n = len(s)-1
while(n>=0):
    #f= f+s[i]
    n=n-1
    
if(s==k):
    print("yes")
else:
    print("no")


# In[5]:


x ={4,1,3,5,6,8,5,"ghjg"}


# In[4]:


x


# In[5]:


k = [2,65,8,6,8,5]


# In[6]:


set(k)


# In[7]:


k


# In[8]:


type(x)


# In[9]:


d = {4:"sudh"}


# In[19]:


d1 = {"kurd":54546,"key2":"raju","kud":[3,2,5,4,1],"ydd":[3,4,2,5,2],"hndj":{2,8,4,5,9}}


# In[11]:


d1


# In[13]:


d1['kurd']


# In[14]:


m1 = {"key":{2,1,5,4,6}}


# In[20]:


d1


# In[22]:


type(d1['hndj'])


# In[23]:


d1['ydd'][4]


# In[24]:


d1.keys()


# In[25]:


d1.values()


# In[26]:


d1.items()


# In[27]:


type(d1.items())


# In[28]:


d1['kurd'] = "rajkumar"


# In[29]:


d1


# In[30]:


d1['kuku'] = [2,8,4,6,5]


# In[31]:


d1


# In[32]:


d1.get("kurd")


# In[34]:


## add two dictionary in one


# In[35]:


# same list append in list
k.append(k)


# In[36]:


k


# In[37]:


k[6]


# In[38]:


t1 = ("aditya",1,1+2j,True)
t1.index(True)


# In[44]:


keys = ("dfd","sdf","jaksh")
values = (2,9)


# In[45]:


p = d1.fromkeys(keys,values)


# In[46]:


p


# In[47]:


d1


# In[15]:


# play with dictionary 

d = { "iN":"india",
      "c":"canada",
      "u":"united state"
    
    }


# In[26]:


# create two seperate list
#l1 havig key <5
#l2 having key  >5
lG =[]
lL=[]
for i in d:
    if len(i) <= 5:
        lG.append(i)
    else:
        lL.append(i)


# In[27]:


print(lG)
print(lL)


# In[28]:


# nested dic find the max val of both dic 
d1 = {"ineuron":{
               "a":14,
                "b":15,
                "c":55
                }, 
      'course':{
              'd':45,
              "E":66,
              'f':1
            }  
     }


# In[30]:


l1 =[]
l2 = []
for i in d1:
    if d1[i]== "ineuron":
        for j in d1[i].values():
            l1.append(j)
    elif d1[i]=="course":
        for j in d1[i].values():
            l2.append(j)
            
sort(l1)
sort(l2)
print(max(l1))
print(max(l2))


# In[33]:


# print max number in given value of diff keys
d1 = {"ineuron":{
               "a":14,
                "b":15,
                "c":55
                }, 
      'course':{
              'd':45,
              "E":66,
              'f':1
            }  
     }

for i in d1.values():
    mx =0
    for j in i.values():
        if mx<j:
            mx =j
    print(mx)


# In[34]:


# show max value of dic with diff key 
for i in d1.keys():
    print(i)
    print(max(d1[i].values()))


# In[38]:


d2 = {"ineuron":{"a":14,"b":525,"c":45},"course":{"d":5,"df":96},"g":6,"h":[4,5,8,6,80],'k':"fsdf"}


# In[39]:


l1 =[]
for i in d2.values():
    if type(i)==dict:
        l1.append(max(i.values()))
    elif type(i)==list:
        l1.append(max(i))
    elif type(i)==tuple:
        l1.append(max(i))
    elif type(i)==str:
        pass
    else:
        l1.append(i)
        
print(max(l1))


# In[43]:


l =[]
for i in d2.values():
    if type(i) != str and type(i) != complex:
        if type(i) ==list or type(i)== tuple or type(i) == set:
            l.extend(list(i))
        elif type(i) == dict:
            for j in i.values():
                l.append(j)
                
                
print(max(l))


# In[11]:


# palindrom for num

a =121
c=0
def test(a):
        while(a>0):
            b=a%10
            #print(b)
            c = c*10+b
            #print(c)
            a = int(a/10)
            #print(a)
        return c
if(a == c):
    print("yes")
else:
    print("not")


# In[9]:


a =121
if(a == c):
    print("yes")
else:
    print("not")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


##find  india is available in dic or not


# In[17]:


#check present check in key 
"iN" in d


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




