#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("D:\Dimitra\DATA\AgroSaiva Data.csv")


# In[3]:


df.drop('Unnamed: 20',inplace=True,axis=1)
df.drop('Unnamed: 21',inplace=True,axis=1)
df.drop('Unnamed: 22',inplace=True,axis=1)
df.drop('Unnamed: 23',inplace=True,axis=1)
df.drop('Unnamed: 24',inplace=True,axis=1)
df.drop('Unnamed: 25',inplace=True,axis=1)


# In[4]:


df["Gender"]=1
ids=df["Animal ID"]
ids.pop(0)
Hids=df["mother's id"]
Hids.pop(0)
Bids=df["father's id"]
Bids.pop(0)


# In[5]:


index=1
for i in ids:
    for j in Hids:
        if(i==j):
            df.at[index,'Gender']=0
            break
    for j in Bids:
        if(i==j):
            df.at[index,'Gender']=1
            break
    index+=1


# In[6]:


df=df[df["Gender"]==1]
df


# In[7]:


df.replace([np.inf, -np.inf], np.nan, inplace=True)


# In[8]:


from datetime import datetime,timedelta,date
df["Weaning_Date"]='0'
df["Weaning_Weight"]=0


# In[9]:


df.drop(0, axis=0, inplace=True)
df.columns = df.columns.str.strip()


# In[10]:


df['Weight at 4 months'] = df['Weight at 4 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
df['Birth weight'] = df['Birth weight'].replace([np.inf, -np.inf], np.nan).astype('Int64')
df['Weight at 8 months'] = df['Weight at 8 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
df['Weight at 12 months'] = df['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
df['Weight at 16 months'] = df['Weight at 16 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
df['Weight at 24 months'] = df['Weight at 24 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')


# In[11]:



x=df["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
df.insert(loc=1, column="index", value=ind)
df.set_index("index",inplace=True)


# In[12]:


for i in range(df["Gender"].size):
    df.loc[i,"Weaning_Weight"]=round((df.loc[i,"Weight at 4 months"]+df.loc[i,"Weight at 8 months"])/2)
    d11=df.loc[i,"Date of weighing at 4 months"]
#     print(d11)
    if(d11=='0'):
        continue
    d1=datetime.strptime(d11, "%Y-%m-%d")
#     print(d1)
    d21=df.loc[i,"weaning date (8 months)"]
    if(d21=='0'):
        continue
#     print(d21)
    d2=datetime.strptime(d21,"%Y-%m-%d")
#     print(d2)
    
    diff=round(((d2-d1).days)/2)
#     print(diff)
    nd=d1+timedelta(days=diff)
# #     nd=date(nd)
#     nd=datetime.strptime(str(nd),'%d%b%Y')
    nd=nd.date()
    df.loc[i,"Weaning_Date"]=nd
    


# In[13]:


df


# In[14]:


df["Age_of_Dam"]=5


# In[15]:


ids2=df["Animal ID"]

BWB=df["Birth weight"]


# In[16]:


data1=[[2,60,54],
      
[3,40,36],
[4,20,18],
[5,0,0],
[6,0,0],
[7,0,0],
[8,0,0],
[9,0,0],
[10,0,0],
[11,20,18],
[12,20,18],
[13,20,18],
[14,20,18],
[15,20,18],
[16,20,18],
[17,20,18],
[18,20,18],
[19,20,18],
[20,20,18]
]


# In[17]:


WWAdj=pd.DataFrame(data1, columns=['Age_of_Dam', 'Male','Female'])


# In[18]:


WWAdj


# In[19]:


data2=[
[2,8,8],
[3,5,5],
[4,2,2],
[5,0,0],
[6,0,0],
[7,0,0],
[8,0,0],
[9,0,0],
[10,0,0],
[11,3,3],
[12,3,3],
[13,3,3],
[14,3,3],
[15,3,3],
[16,3,3],
[17,3,3],
[18,3,3],
[19,3,3],
[20,3,3]
    
]


# In[20]:


BWAdj=pd.DataFrame(data2, columns=['Age_of_Dam', 'Male','Female'])


# In[21]:


BWAdj


# In[22]:


ActualBwMean = df["Birth weight"].mean()


# In[23]:


ActualWwMean=df["Weaning_Weight"].mean()


# In[24]:


ActualBwMean


# In[ ]:





# In[25]:


AvgAdjWwB=WWAdj['Male'].mean()
AvgAdjWwB


# In[26]:


AvgAdjBW=BWAdj['Male'].mean()
AvgAdjBW


# In[27]:


IncrementedBwMean=AvgAdjBW+ActualBwMean
IncrementedBwMean


# In[28]:


IncrementedMeanWwB=ActualBwMean+AvgAdjWwB
IncrementedMeanWwB


# In[31]:


import random
num = random.random()
index=0
l=0
x=df["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
for (i,j) in zip(BWB, ids2):
    z=float(i)-IncrementedBwMean
    diff=round(abs(z))
    if diff<2:
        diff=0
    elif diff<4:
        diff=3
    elif diff<7:
        diff=8
    else:
        diff=8
#     print(i)
#     print(j)
#     print(diff)
    a=BWAdj.loc[BWAdj['Male']==diff]
    sz=a["Male"].size
#     print(a)
#     print(sz)
    randomNum= random.randint(0,sz-1)
    indices = [*range(0, sz, 1)]
#     a['index']= indices
    a.insert(loc=1, column="index", value=indices)
#     print(indices)
#     print(randomNum)
    a.set_index("index",inplace=True)
#     print(a.Age_of_Dam[randomNum])
#     print(a.loc[randomNum,'Age_of_Dam'])
    print(index)
 

    df.loc[index,'Age_of_Dam']=a.loc[randomNum,'Age_of_Dam']
    index+=1


# In[36]:


df


# In[34]:


WWB=df["Weaning_Weight"]
print(WWB)


# In[35]:


import random
num = random.random()
index=0
l=0
x=df["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
for (i,j) in zip(WWB, ids2):
    z=float(i)-IncrementedMeanWwB
    diff=round(abs(z))
    if diff<10:
        diff=0
    elif diff<30:
        diff=20
    elif diff<50:
        diff=40
    else:
        diff=60
#     print(i)
#     print(j)
#     print(diff)
    a=WWAdj.loc[WWAdj['Male']==diff]
    sz=a["Male"].size
#     print(a)
#     print(sz)
    randomNum= random.randint(0,sz-1)
    indices = [*range(0, sz, 1)]
#     a['index']= indices
    a.insert(loc=1, column="index", value=indices)
#     print(indices)
#     print(randomNum)
    a.set_index("index",inplace=True)
#     print(a.Age_of_Dam[randomNum])
#     print(a.loc[randomNum,'Age_of_Dam'])
    
    xz=df.loc[index,'Age_of_Dam']
#     print(xz)
#     print()
#     print(df_GenderKnown1.Age_of_Dam[l])
    df.loc[index,'Age_of_Dam']=round((a.loc[randomNum,'Age_of_Dam']+xz)/2)
    index+=1


# In[38]:


df.to_csv('D:\Dimitra\DATA\CorrectedAge.csv')


# In[ ]:




