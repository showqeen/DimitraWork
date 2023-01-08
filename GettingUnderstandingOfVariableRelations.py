#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv("D:\Dimitra\DATA\AgroSaiva Data.csv")


# In[4]:


df


# In[5]:


df.drop('Unnamed: 20',inplace=True,axis=1)


# In[6]:


df.drop('Unnamed: 21',inplace=True,axis=1)
df.drop('Unnamed: 22',inplace=True,axis=1)
df.drop('Unnamed: 23',inplace=True,axis=1)


# In[7]:


df.drop('Unnamed: 24',inplace=True,axis=1)
df.drop('Unnamed: 25',inplace=True,axis=1)


# 

# In[8]:


df


# In[9]:


df["Gender"]='Pending'


# In[10]:


df


# In[11]:


ids=df["Animal ID"]


# In[12]:


ids.pop(0)


# In[13]:


ids


# In[14]:


Hids=df["mother's id"]
Hids.pop(0)
    


# In[15]:


Bids=df["father's id"]
Bids.pop(0)


# In[16]:


Bids


# In[17]:


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


# In[218]:


# index=1
# for i in ids:
#     for j in Bids:
#         if(i==j):
#             df.at[index,'Gender']='B'
#             break
#     for j in Hids:
#         if(i==j):
#             if(df.loc[index,"Gender"]=='B'):
#                     df.at[index,'Gender']='BH'
#             df.at[index,'Gender']='H'
#             break
#     index+=1


# In[21]:


df[df["Gender"]==1]


# In[220]:


cities=df.Gender.unique()


# In[221]:


cities


# In[21]:


# ypoints=df_GenderKnown["Birth weight"]

# xpoints=df_GenderKnown["Gender"]


# In[22]:


# plt.scatter(xpoints, ypoints,color = 'hotpink')
# plt.show()


# In[222]:


df_new = df[df['Gender'] == 'B']


# In[223]:


df_new


# In[224]:


df_new2=df[df['Gender']=='H']
df_new2


# In[225]:


df_new3=df[df['Gender']=="Pending"]
df_new3


# In[226]:


pichart_data=np.array([6385,5517,578])
Labels=["GenderPendng","dam","Bull"]


# In[227]:


plt.pie(pichart_data,labels=Labels)
plt.show() 


# In[29]:


df


# In[30]:


df_GenderKnown1=df[df['Gender']=='H']


# In[31]:


df_GenderKnown2=df[df['Gender']=='B']


# In[32]:


frames = [df_GenderKnown1, df_GenderKnown2]
  
df_GenderKnown = pd.concat(frames)


# In[33]:


df_GenderKnown1


# In[34]:


df_GenderKnown1.replace([np.inf, -np.inf], np.nan, inplace=True)


# In[35]:


pd.set_option('use_inf_as_na',True)


# In[36]:


df_GenderKnown1['Weight at 12 months'] = df_GenderKnown1['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')
ActualMeanH=df_GenderKnown1["Weight at 12 months"].mean()
ActualMeanH


# In[37]:


df_GenderKnown2


# In[38]:


df_GenderKnown2['Weight at 12 months'] = df_GenderKnown2['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')


# In[39]:


ActualMeanB=df_GenderKnown2["Weight at 12 months"].mean()
ActualMeanB


# In[40]:


df_GenderKnown


# In[41]:


pd.set_option('display.max_columns', None)


# In[42]:


df_GenderKnown


# In[43]:


df_GK=df_GenderKnown


# In[44]:


index=0
l=0
x=df_GenderKnown["Animal ID"].size
ind=[*range(0, x, 1)]


# In[45]:


df_GK["index"]=ind


# In[46]:


df_GK.set_index("index",inplace=True)


# In[47]:


from datetime import datetime


# In[48]:


df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 12 month'] = df_GK['Date of weighing at 12 month'].replace([np.inf, -np.inf], np.nan).astype('O')


# In[49]:


df_GK['Birth date'] = df_GK['Birth date'].replace([np.inf, -np.inf], np.nan).astype('O')
df_GK['Date of weighing at 24 month'] = df_GK['Date of weighing at 24 month'].replace([np.inf, -np.inf], np.nan).astype('O')


# In[50]:


df_GK['Birth date'].fillna(value=df_GK['Birth date'].mode()[0], inplace=True)


# In[51]:


df_GK['Date of weighing at 12 month'].fillna(value=df_GK['Date of weighing at 12 month'].mode()[0], inplace=True)


# In[52]:


df_GK['Date of weighing at 24 month'].fillna(value=df_GK['Date of weighing at 24 month'].mode()[0], inplace=True)


# In[53]:


df_GK.loc[151,"Birth date"]


# In[54]:


df_GK["D4"]=3


# In[55]:


df_GK["D12"]=3


# In[56]:


df_GK["D24"]=3


# In[57]:


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


# In[58]:


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


# In[59]:


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


# In[60]:


df_GK


# In[61]:


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





# In[62]:


plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()


# In[63]:


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


# In[64]:


plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()


# In[65]:


df_GK.columns = df_GK.columns.str.strip()


# In[66]:


df_GK.loc[0,"Weight at 24 months"]


# In[67]:


x=[]
y=[]
z=[]
index=0
for i in range(df_GK["D24"].size):
    x.append (int(df_GK.loc[index,"D24"]))
    y.append (int(df_GK.loc[index,"Weight at 24 months"]))
    if(df_GK.loc[index,"Gender"]=='H'):
        z.append("red")
    else:
        z.append("Green")
    index+=1
#     z.append(df_GK.loc[index,"Gender"])
#Weight at 24 months


# In[68]:


plt.scatter(x[5480:5550],y[5480:5550],s=100,c=z[5480:5550])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[69]:


# a.set_index("index",inplace=True)


# In[70]:


index=0
l=0
x=df_GenderKnown1["Animal ID"].size
ind=[*range(0, x, 1)]


# In[71]:


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


# In[72]:


WWAdj=pd.DataFrame(data1, columns=['Age_of_Dam', 'Male','Female'])


# In[73]:


WWAdj


# In[74]:


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


# In[75]:


BWAdj=pd.DataFrame(data2, columns=['Age_of_Dam', 'Male','Female'])


# In[76]:


BWAdj


# In[77]:


df_GenderKnown['Birth weight'] = df_GenderKnown['Birth weight'].replace([np.inf, -np.inf], np.nan).astype('Int64')


# In[78]:


df.isna().sum().sum()


# In[ ]:





# In[79]:


ActualBwMean = df_GenderKnown["Birth weight"].mean()


# In[80]:


print(ActualBwMean)


# In[81]:


df_GenderKnown['Birth weight'].fillna(value=ActualBwMean, inplace=True)


# In[82]:


AvgAdjBW=BWAdj['Male'].mean()
AvgAdjBW


# In[83]:


IncrementedBwMean=AvgAdjBW+ActualBwMean
IncrementedBwMean


# In[84]:


df_GenderKnown1['Weight at 12 months'] = df_GenderKnown1['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')


# In[85]:


df_GenderKnown2['Weight at 12 months'].fillna(value=ActualMeanB, inplace=True)


# In[86]:


df_GenderKnown1['Weight at 12 months'].fillna(value=ActualMeanH, inplace=True)


# In[87]:


AvgAdjWwB=WWAdj['Male'].mean()
AvgAdjWwB


# In[88]:


AvgAdjWwH=WWAdj['Female'].mean()
AvgAdjWwH


# In[89]:


df_GenderKnown['Weight at 12 months'] = df_GenderKnown['Weight at 12 months'].replace([np.inf, -np.inf], np.nan).astype('Int64')


# In[90]:


IncrementedMeanWwB=ActualMeanB+AvgAdjWwB
IncrementedMeanWwB


# In[91]:


IncrementedMeanWwH=ActualMeanH+AvgAdjWwH
IncrementedMeanWwH


# In[92]:


df_GenderKnown1["Age_of_Dam"]=5


# In[93]:


df_GenderKnown1


# In[94]:


BWH=df_GenderKnown1["Birth weight"]
BWH


# In[95]:


WWH=df_GenderKnown1["Weight at 12 months"]
WWH


# In[96]:


# WWH=df_GenderKnown1["Weight at 12 months"]
# WWH


# In[97]:


BWH


# In[98]:


df_GenderKnown.size


# In[99]:


df_GenderKnown


# In[100]:


df_GenderKnown1


# In[101]:


df_GenderKnown2


# In[102]:


ids1=df_GenderKnown1["Animal ID"]


# In[ ]:





# In[103]:


ids1


# In[104]:



# import random
# num = random.random()
# index=0
# for i,j in BWH,ids1:
#     diff=round(abs(i-IncrementedBwMean))
#     a=BWAdj[BWAdj['Female']==diff]
#     sz=a.size
#     randomNum= random.randint(0,sz)
#     df_Genderknown1.Age_of_Dam[j]=a[]
    
    


# In[105]:


# df_GenderKnown2.at['C', 'x'] = 10


# In[106]:


# a=BWAdj[BWAdj['Female']==3]


# In[107]:


# a


# In[ ]:





# In[ ]:





# In[108]:


# k=a["Male"].size


# In[109]:


# indices = [*range(0, k, 1)]


# In[110]:


# indices


# In[111]:


# a['index']= indices


# In[112]:


# a


# In[113]:


# a.set_index("index",inplace=True)


# In[114]:


# a.Male[0]


# In[115]:


ids1=df_GenderKnown1["Animal ID"]


# In[116]:


df_GenderKnown1


# In[117]:


a=BWAdj.loc[BWAdj['Female']==diff]
sz=a["Female"].size
print(a)


# In[118]:


df_GenderKnown1=df[df['Gender']=='H']


# In[119]:


df_GenderKnown1["Age_of_Dam"]=5


# In[120]:


df_GenderKnown1


# In[121]:


index=0
l=0
x=df_GenderKnown1["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
df_GenderKnown1.insert(loc=1, column="index", value=ind)


# In[122]:


df_GenderKnown1


# In[123]:


x=df_GenderKnown1["Animal ID"].size


# In[124]:


k=3


# In[125]:


df_GenderKnown1.set_index("index",inplace=True)


# In[126]:


df_GenderKnown1.loc[k,"Age_of_Dam"]


# In[127]:


x


# In[128]:


import random
num = random.random()
index=0
l=0
x=df_GenderKnown1["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
for (i,j) in zip(BWH, ids1):
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
    a=BWAdj.loc[BWAdj['Female']==diff]
    sz=a["Female"].size
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
 
#     print(df_GenderKnown1.Age_of_Dam[l])
    df_GenderKnown1.loc[index,'Age_of_Dam']=a.loc[randomNum,'Age_of_Dam']
    index+=1


# In[129]:


df_GenderKnown1


# In[130]:


df_GenderKnown2=df[df['Gender']=='B']


# In[131]:


df_GenderKnown2["Age_of_Dam"]=5


# In[132]:


df_GenderKnown2


# In[133]:


index=0
l=0
x=df_GenderKnown2["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
df_GenderKnown2.insert(loc=1, column="index", value=ind)


# In[134]:


df_GenderKnown2


# In[135]:


df_GenderKnown2.set_index("index",inplace=True)


# In[136]:


ids2=df_GenderKnown2["Animal ID"]


# In[137]:


BWB=df_GenderKnown2["Birth weight"]
BWB


# In[138]:


import random
num = random.random()
index=0
l=0
x=df_GenderKnown2["Animal ID"].size
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
    a=BWAdj.loc[BWAdj['Female']==diff]
    sz=a["Female"].size
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
 
#     print(df_GenderKnown1.Age_of_Dam[l])
    df_GenderKnown2.loc[index,'Age_of_Dam']=a.loc[randomNum,'Age_of_Dam']
    index+=1


# In[139]:


df_GenderKnown2


# In[140]:


WWB=df_GenderKnown2["Weight at 12 months"]
print(WWB)
WWH=df_GenderKnown1["Weight at 12 months"]
print(WWH)


# In[141]:


WWAdj


# In[142]:


df_GenderKnown2["Age_of_Dam"]


# In[189]:


import random
num = random.random()
index=0
l=0
x=df_GenderKnown2["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
for (i,j) in zip(WWB, ids2):
    z=float(i)-IncrementedBwMean
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
    
    xz=df_GenderKnown2.loc[index,'Age_of_Dam']
#     print(xz)
#     print()
#     print(df_GenderKnown1.Age_of_Dam[l])
    df_GenderKnown2.loc[index,'Age_of_Dam']=round((a.loc[randomNum,'Age_of_Dam']+xz)/2)
    index+=1


# In[190]:


df_GenderKnown2


# In[145]:


import random
num = random.random()
index=0
l=0
x=df_GenderKnown1["Animal ID"].size
ind=[*range(0, x, 1)]
# df_GenderKnown1['index']=ind
for (i,j) in zip(WWH, ids1):
    z=float(i)-IncrementedBwMean
    diff=round(abs(z))
    if diff<8:
        diff=0
    elif diff<26:
        diff=18
    elif diff<45:
        diff=36
    else:
        diff=54
#     print(i)
#     print(j)
#     print(diff)
    a=WWAdj.loc[WWAdj['Female']==diff]
    sz=a["Female"].size
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
#     print(index)
    xz=df_GenderKnown1.loc[index,'Age_of_Dam']
#     print(xz)
#     print(df_GenderKnown1.Age_of_Dam[l])
    df_GenderKnown1.loc[index,'Age_of_Dam']=round((a.loc[randomNum,'Age_of_Dam']+xz)/2)
    index+=1


# In[146]:


df_GenderKnown1


# In[191]:


frames = [df_GenderKnown1, df_GenderKnown2]
  
df_GenderK = pd.concat(frames)


# In[193]:


df_GenderK


# In[194]:


x=df_GenderK["Animal ID"].size
ind=[*range(0, x, 1)]


# In[195]:


df_GenderK.insert(loc=1, column="index", value=ind)


# In[196]:


df_GenderK.set_index("index",inplace=True)


# In[ ]:





# In[197]:


df_GenderK.loc[df_GenderK["Gender"] =="B","Gender"]= 1


# In[198]:


df_GenderK.loc[df_GenderK["Gender"] =="H","Gender"]= 0


# In[199]:


df_GenderK


# In[201]:


df_GenderK.to_csv('D:\Dimitra\DATA\GaKnown.csv')


# In[ ]:





# In[200]:


df_GenderK.dtypes


# In[153]:


print(df_GenderK['Age_of_Dam'].astype('int').corr(df_GenderK['Birth weight'].astype('float')))


# In[154]:


print(df_GenderK['Age_of_Dam'].astype('int').corr(df_GenderK['Weight at 12 months'].astype('float')))


# In[155]:


print(df_GenderK['Gender'].astype('int').corr(df_GenderK['Weight at 12 months'].astype('float')))


# In[156]:


print(df_GenderK['Gender'].astype('int').corr(df_GenderK['Birth weight'].astype('float')))


# In[157]:


li1=df_GenderK["Age_of_Dam"]


# In[158]:


li2=df_GenderK["Birth weight"]


# In[159]:


li4=df_GenderK["Weight at 12 months"]


# In[160]:


li5=[]
index=0
for (i,j) in zip(li1,li2):
#     print(i)
#     print(j)
    a=int(i)*int(j)
#     print(a)
    li5.append(a)
    index+=1


# In[162]:


# lis=np.array(li3)


# In[163]:


# print(df1['Age_of_Dam'].astype('int').corr(df1['addi']).astype('int'))


# In[164]:


df2=df_GenderK


# In[165]:


df2["addi"]=li5


# In[166]:


df2


# In[167]:


print(df2['Gender'].astype('int').corr(df2['addi'].astype('float')))


# In[ ]:





# In[168]:


from sklearn.cluster import KMeans
km=KMeans(2)


# In[169]:


from datetime import datetime


# In[172]:


df_GenderK


# In[173]:


df_GenderK["ABW"]=0
df_GenderK["AWW"]=0
df_GenderK["AYW"]=0


# In[184]:


df_GenderK


# In[186]:


for col in df_GenderK.columns:
    print(col)


# In[188]:


for i in range(df_GenderK["Gender"].size):
    print(i)
    bd=str(df_GenderK.loc[i,"Birth date"])
    print(bd)
    G=df_GenderK.loc[i,"Gender"]
    print(yw)
    A=df_GenderK.loc[i,"Age_of_Dam"]
    bw=df_GenderK.loc[i,"Birth weight"]
    wd=df_GenderK.loc[i,"weaning date (8 months)"]
    ww=df_GenderK.loc[i,"Weight at 8 months"]
    yd=df_GenderK.loc[i,"Date of weighing at 12 month"]
    yw=df_GenderK.loc[i,"Weight at 12 months"]
#     tup1=EpdCal(bd,G,A,bw,wd,ww,yd,yw)
#     GenderK.loc[i,"ABW"]=tup1[0]
#     GenderK.loc[i,"AWW"]=tup1[1]
#     GenderK.loc[i,"AYW"]=tup1[2]
#     print(tup1[0])
#     print(tup1[1])
#     print(tup1[2])
    break


# In[ ]:





# In[ ]:





# In[178]:



def EpdCal(birthDate,Gender,AgeOfDam,BW,WeaningWTDate,WW,YDD,YD):

    BD = datetime.strptime(birthDate, "%Y-%m-%d")





    #Dictionary to store the Adjustment values for Birth Weight
    AdjForBW={2:8,3:5,4:2,11:3}

    #Dictionary to store the Adjustment values for Weining weight
    AdjForWW={2:{'b':60,'h':54},3:{'b':40,'h':36},4:{'b':20,'h':18},11:{'b':20,'h':18}}

    #Getting the approraite valu of birth weight adjustmment as per Age of the Dam
    BWAdj=AdjForBW[AgeOfDam]

    #Calculating the Adjusted Birth weight to overcome the age factor of the Dam
    ABW=BW+BWAdj


    #Weaning Weight Calculation



    #Cheking Wheather the weaning weight date is appropraite for weanig weight calculation i.e betweeen 160 to 250 days
    WD = datetime.strptime(WeaningWTDate, "%Y-%m-%d")
    DaysWeanig=(WD-BD).days
    print(DaysWeaning)
    if DaysWeanig<160 or DaysWeanig>250:
        print("The time of weaning should be betweeen 160 and 250 days but the animal does not satisfy this cretirea")
    else:

        #Getting the Age factor
        AdjFact=AdjForWW[AgeOfDam][Gender]

        A_205_WW=(((WW-BW)*205)/DaysWeanig)+BW+AdjFact

        #Yearlling Weight Calcuation




        #Cheking Wheather the YEarling weight date is appropraite for weanig weight calculation i.e betweeen 320 to 410 days
        YD = datetime.strptime(YDD, "%Y-%m-%d")
        DaysYearing=(YD-BD).days
        if DaysYearing<320 or DaysYearing>410:
            print("The time of Yearling should be betweeen 320 and 410 days but the animal does not satisfy this cretirea")
        else:


            #Calculating Days between the weaning and yearling date

            DaysYW=(YD-WD).days

            A_365_YW=(((YW-WW)*160)/DaysYW)+A_205_WW



            print(ABW)
            print(A_205_WW)
            print(A_365_YW)
            a=[]
            a.append(ABW)
            a.append(A_205_WW)
            a.append(A_205_WW)
            return ABW,A_205_WW,A_365_YW


# In[ ]:





# In[ ]:





# In[ ]:




