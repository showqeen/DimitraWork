#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


df=pd.read_csv("D:\Dimitra\DATA\AgroSaiva Data.csv")


# In[12]:


df


# In[13]:


df.drop('Unnamed: 20',inplace=True,axis=1)


# In[14]:


df.drop('Unnamed: 21',inplace=True,axis=1)
df.drop('Unnamed: 22',inplace=True,axis=1)
df.drop('Unnamed: 23',inplace=True,axis=1)


# In[15]:


df.drop('Unnamed: 24',inplace=True,axis=1)
df.drop('Unnamed: 25',inplace=True,axis=1)


# 

# In[16]:


df


# In[17]:


df["Gender"]='Pending'


# In[18]:


df


# In[19]:


ids=df["Animal ID"]


# In[20]:


ids.pop(0)


# In[21]:


ids


# In[22]:


Hids=df["mother's id"]
Hids.pop(0)
    


# In[23]:


Bids=df["father's id"]
Bids.pop(0)


# In[24]:


Bids


# In[25]:


index=1
for i in ids:
    for j in Bids:
        if(i==j):
            df.at[index,'Gender']='B'
            break
    for j in Hids:
        if(i==j):
            df.at[index,'Gender']='H'
            break
    index+=1


# In[26]:


df


# In[27]:


cities=df.Gender.unique()


# In[28]:


cities


# In[29]:


# ypoints=df_GenderKnown["Birth weight"]

# xpoints=df_GenderKnown["Gender"]


# In[30]:


# plt.scatter(xpoints, ypoints,color = 'hotpink')
# plt.show()


# In[31]:


df_new = df[df['Gender'] == 'B']


# In[32]:


df_new


# In[33]:


df_new2=df[df['Gender']=='H']
df_new2


# In[34]:


df_new3=df[df['Gender']=="Pending"]
df_new3


# In[35]:


pichart_data=np.array([6385,5517,578])
Labels=["GenderPendng","dam","Bull"]


# In[36]:


plt.pie(pichart_data,labels=Labels)
plt.show() 


# In[37]:


df


# In[38]:


df_GenderKnown1=df[df['Gender']=='H']


# In[39]:


df_GenderKnown2=df[df['Gender']=='B']


# In[40]:


frames = [df_GenderKnown1, df_GenderKnown2]
  
df_GenderKnown = pd.concat(frames)


# In[41]:


df_GenderKnown1


# In[42]:


df_GenderKnown1.replace([np.inf, -np.inf], np.nan, inplace=True)


# In[43]:


pd.set_option('use_inf_as_na',True)


# In[44]:


df_GenderKnown1['Weight at 12 months'] = df_GenderKnown1['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
ActualMeanH=df_GenderKnown1["Weight at 12 months"].mean()
ActualMeanH


# In[45]:


df_GenderKnown2


# In[46]:


df_GenderKnown2['Weight at 12 months'] = df_GenderKnown2['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')


# In[47]:


ActualMeanB=df_GenderKnown2["Weight at 12 months"].mean()
ActualMeanB


# In[48]:


df_GenderKnown


# In[49]:


pd.set_option('display.max_columns', None)


# In[50]:


df_GenderKnown


# In[51]:


df_GK=df_GenderKnown


# In[52]:


index=0
l=0
x=df_GenderKnown["Animal ID"].size
ind=[*range(0, x, 1)]


# In[53]:


df_GK["index"]=ind


# In[54]:


df_GK.set_index("index",inplace=True)


# In[55]:


from datetime import datetime


# In[56]:


df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 12 month'] = df_GK['Date of weighing at 12 month'].replace([np.inf, -np.inf], np.nan).astype('O')


# In[57]:


df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 24 month'] = df_GK['Date of weighing at 24 month'].replace([np.inf, -np.inf], np.nan).astype('O')


# In[78]:


df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 16 month'] = df_GK['Date of weighing at 16 month'].replace([np.inf, -np.inf], np.nan).astype('O')


# In[79]:


df_GK['Birth date'].fillna(value=df_GK['Birth date'].mode()[0], inplace=True)


# In[80]:


df_GK['Date of weighing at 12 month'].fillna(value=df_GK['Date of weighing at 12 month'].mode()[0], inplace=True)


# In[81]:


df_GK['Date of weighing at 16 month'].fillna(value=df_GK['Date of weighing at 16 month'].mode()[0], inplace=True)


# In[82]:


df_GK['Date of weighing at 24 month'].fillna(value=df_GK['Date of weighing at 24 month'].mode()[0], inplace=True)


# In[83]:


df_GK.loc[151,"Birth date"]


# In[84]:


df_GK["D4"]=3


# In[85]:


df_GK["D12"]=3


# In[86]:


df_GK["D24"]=3


# In[87]:


df_GK["D16"]=3


# In[88]:


for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 12 month"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 12 month"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D12"]=diff
#     print(i)


# In[89]:


for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 4 months"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 4 months"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D4"]=diff
#     print(i)


# In[90]:


for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 24 month"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 24 month"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D24"]=diff
#     print(i)


# In[91]:


for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 16 month"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 16 month"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D16"]=diff
#     print(i)


# In[92]:


df_GK


# In[93]:


x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D12"].size):
    x.append (int(df_GK.loc[index,"D12"]))
    y.append (int(df_GK.loc[index,"Weight at 12 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("red")
    else:
        z.append("Green")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])


# In[ ]:





# In[94]:


plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()


# In[95]:


x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D4"].size):
    x.append (int(df_GK.loc[index,"D4"]))
    y.append (int(df_GK.loc[index,"Weight at 4 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("blue")
    else:
        z.append("pink")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])


# In[96]:


plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()


# In[105]:


df_GK


# In[109]:


df_GK.columns = df_GK.columns.str.strip()


# In[110]:


for col in df_GK.columns:
    print(col)


# In[ ]:





# In[111]:


df_GK["Weight at 24 months"]


# In[112]:


x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D4"].size):
    x.append (int(df_GK.loc[index,"D4"]))
    y.append (int(df_GK.loc[index,"Weight at 24 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("blue")
    else:
        z.append("pink")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])


# In[114]:


plt.scatter(x[4939:6095],y[4939:6095],s=100,c=z[4939:6095])
plt.show()


# In[115]:


x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D16"].size):
    x.append (int(df_GK.loc[index,"D16"]))
    y.append (int(df_GK.loc[index,"Weight at 16 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("red")
    else:
        z.append("Green")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])


# In[116]:


plt.scatter(x[4939:6095],y[4939:6095],s=100,c=z[4939:6095])
plt.show()


# In[117]:


df_GK["ND24"]=3


# In[119]:


for i in range(df_GK["ND24"].size):
    df_GK.loc[i,"ND24"]=(int(df_GK.loc[i,"Weight at 24 months"])/int(df_GK.loc[i,"D24"]))*100


# In[120]:


df_GK


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import numpy as np
import pandas as pd
import matplotlib

import matplotlib.pyplot as plt

df=pd.read_csv("D:\Dimitra\DATA\AgroSaiva Data.csv")

df

df.drop('Unnamed: 20',inplace=True,axis=1)

df.drop('Unnamed: 21',inplace=True,axis=1)
df.drop('Unnamed: 22',inplace=True,axis=1)
df.drop('Unnamed: 23',inplace=True,axis=1)


df.drop('Unnamed: 24',inplace=True,axis=1)
df.drop('Unnamed: 25',inplace=True,axis=1)



df

df["Gender"]='Pending'

df

ids=df["Animal ID"]

ids.pop(0)

ids

Hids=df["mother's id"]
Hids.pop(0)
    

Bids=df["father's id"]
Bids.pop(0)

Bids

index=1
for i in ids:
    for j in Bids:
        if(i==j):
            df.at[index,'Gender']='B'
            break
    for j in Hids:
        if(i==j):
            df.at[index,'Gender']='H'
            break
    index+=1

df

cities=df.Gender.unique()

cities

ypoints=df_GenderKnown["Birth weight"]

xpoints=df_GenderKnown["Gender"]


plt.scatter(xpoints, ypoints,color = 'hotpink')
plt.show()

df_new = df[df['Gender'] == 'B']

df_new

df_new2=df[df['Gender']=='H']
df_new2

df_new3=df[df['Gender']=="Pending"]
df_new3

pichart_data=np.array([6385,5517,578])
Labels=["GenderPendng","dam","Bull"]

plt.pie(pichart_data,labels=Labels)
plt.show() 

df

df_GenderKnown1=df[df['Gender']=='H']

df_GenderKnown2=df[df['Gender']=='B']

frames = [df_GenderKnown1, df_GenderKnown2]
  
df_GenderKnown = pd.concat(frames)

df_GenderKnown1

df_GenderKnown1.replace([np.inf, -np.inf], np.nan, inplace=True)

pd.set_option('use_inf_as_na',True)

df_GenderKnown1['Weight at 12 months'] = df_GenderKnown1['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
ActualMeanH=df_GenderKnown1["Weight at 12 months"].mean()
ActualMeanH

df_GenderKnown2

df_GenderKnown2['Weight at 12 months'] = df_GenderKnown2['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')


ActualMeanB=df_GenderKnown2["Weight at 12 months"].mean()
ActualMeanB

df_GenderKnown

pd.set_option('display.max_columns', None)


df_GenderKnown


df_GK=df_GenderKnown

index=0
l=0
x=df_GenderKnown["Animal ID"].size
ind=[*range(0, x, 1)]

df_GK["index"]=ind

df_GK.set_index("index",inplace=True)

from datetime import datetime

df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 12 month'] = df_GK['Date of weighing at 12 month'].replace([np.inf, -np.inf], np.nan).astype('O')


df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 24 month'] = df_GK['Date of weighing at 24 month'].replace([np.inf, -np.inf], np.nan).astype('O')


df_GK['Birth date'].fillna(value=df_GK['Birth date'].mode()[0], inplace=True)

df_GK['Date of weighing at 12 month'].fillna(value=df_GK['Date of weighing at 12 month'].mode()[0], inplace=True)

df_GK['Date of weighing at 24 month'].fillna(value=df_GK['Date of weighing at 24 month'].mode()[0], inplace=True)

df_GK.loc[151,"Birth date"]

df_GK["D4"]=3

df_GK["D12"]=3

df_GK["D24"]=3

for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 12 month"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 12 month"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D12"]=diff
#     print(i)

for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 4 months"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 4 months"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D4"]=diff
#     print(i)

for i in range(df_GenderKnown["Birth date"].size):
    if(df_GK.loc[i,"Birth date"]=='0'):
        continue
    if(df_GK.loc[i,"Date of weighing at 12 month"]=='0'):
        continue
    bd=datetime.strptime(df_GK.loc[i,"Birth date"], "%Y-%m-%d")
    d4=datetime.strptime(df_GK.loc[i,"Date of weighing at 24 month"], "%Y-%m-%d")
    diff=(d4-bd).days
    df_GK.loc[i,"D24"]=diff
#     print(i)

df_GK

x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D12"].size):
    x.append (int(df_GK.loc[index,"D12"]))
    y.append (int(df_GK.loc[index,"Weight at 12 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("red")
    else:
        z.append("Green")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])



plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()

x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D4"].size):
    x.append (int(df_GK.loc[index,"D4"]))
    y.append (int(df_GK.loc[index,"Weight at 4 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("blue")
    else:
        z.append("pink")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])


plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()

