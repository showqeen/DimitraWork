#!/usr/bin/env python
# coding: utf-8

# In[61]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[62]:


df=pd.read_csv("D:\Dimitra\DATA\AdjustedCalculated.csv")


# In[63]:


df.drop("Unnamed: 0",axis=1,inplace=True)
df.drop("Weight at 4 months",axis=1,inplace=True)
df.drop("weaning date (8 months)",axis=1,inplace=True)
df.drop("Date of weighing at 4 months",axis=1,inplace=True)
df.drop("Weight at 8 months",axis=1,inplace=True)
# df.drop("Date of weighing at 12 month",axis=1,inplace=True)
# df.drop("Weight at 12 months",axis=1,inplace=True)
df.drop("Date of weighing at 16 month",axis=1,inplace=True)
df.drop("Weight at 16 months",axis=1,inplace=True)
df.drop("Date of weighing at 24 month",axis=1,inplace=True)
df.drop("Weight at 24 months",axis=1,inplace=True)


# In[64]:


df


# In[ ]:





# In[65]:


from datetime import datetime,date


# In[66]:


a=date.today()
d1 = a.strftime("%m/%Y")


# In[ ]:





# In[67]:


df["BreederCode"]="B"+str(d1)


# In[68]:


df


# In[69]:


df["BirthMgntCode"]="BM1"


# In[70]:


df["BreedComp"]=100


# In[71]:


dfT=pd.read_csv("D:\Dimitra\DATA\AgroSaiva Data.csv")


# In[72]:


Hids=dfT["mother's id"]


# In[73]:


Hids.pop(0)


# In[74]:


ids=df["Animal ID"]


# In[75]:


ids


# In[76]:


import random
index=0
for i in ids:
    ran1=random.randrange(0,100)
    if ran1<50:
        ran2=random.randrange(25,100,25)
        df.loc[index,"BreedComp"]=ran2
    index=1
    


# In[ ]:





# In[77]:


df


# In[78]:


df["WeaningSex"]=1
df["YearlingSex"]=1


# In[79]:


import random
index=0
for i in ids:
    ran1=random.randrange(0,100)
    if ran1<30:
        df.loc[index,"YearlingSex"]=0
        if ran1<28:
            df.loc[index,"WeaningSex"]=0
    index+=1
    
    


# In[80]:


df


# In[81]:


df["ServiceType"]="N"
df["ContBW"]='p'
df["ContWW"]='p'
df["ContYW"]='p'


# In[82]:


df


# In[ ]:





# In[83]:


df


# In[84]:


df.to_csv("D:\Dimitra\DATA\DataForContGrps.csv")


# In[85]:


def BwCont():
    index=0
    for i in range(df["ContBW"].size):
        if(df.loc[i,"ContBW"]=='p'):
            d1=df.loc[i,"Birth date"]
            G1=df.loc[i,"Gender"]
            BH1=df.loc[i,"BreederCode"]
            BC1=df.loc[i,"BreedComp"]
            BMC1=df.loc[i,"BirthMgntCode"]
            ST1=df.loc[i,"ServiceType"]
            if(d1=='0'):
                continue
            Bd=datetime.strptime(d1, "%Y-%m-%d")
            df.loc[i,"ContBW"]="C"+str(index)
            for j in range(df["ContBW"].size):
                if(df.loc[j,"ContBW"]=='p'):
                    d2=df.loc[j,"Birth date"]
                    if(d2=='0'):
                        continue
                    bd=datetime.strptime(d2, "%Y-%m-%d")
                    diff=int((bd-Bd).days)
                    g1=df.loc[j,"Gender"]
                    bh1=df.loc[j,"BreederCode"]
                    bc1=df.loc[j,"BreedComp"]
                    bmc1=df.loc[j,"BirthMgntCode"]
                    st1=df.loc[j,"ServiceType"]
                    if(diff<90 and g1==G1 and BH1==bh1 and BC1==bc1 and BMC1==bmc1 and ST1==st1):
                        df.loc[j,"ContBW"]="C"+str(index)
            index+=1

        


# In[87]:


def WwCont():
    index=0
    for i in range(df["ContWW"].size):
        if(df.loc[i,"ContWW"]=='p'):
            d1=df.loc[i,"Weaning_Date"]
            if(d1=='0'):
                continue
            Bd=datetime.strptime(d1, "%Y-%m-%d")
            CG=df.loc[i,"ContBW"]
            WS=df.loc[i,"WeaningSex"]
            df.loc[i,"ContWW"]="K"+str(index)
            for j in range(df["ContWW"].size):
                if(df.loc[j,"ContWW"]=='p'):
                    d3=df.loc[j,"Weaning_Date"]
                    if(d3=='0'):
                        continue
                    wd=datetime.strptime(d3, "%Y-%m-%d")
                    diff=int((wd-Wd).days)
                    cg=df.loc[i,"ContBW"]
                    ws=df.loc[i,"WeaningSex"]
                    if(CG==cg and WS==ws and diff<4):
                        df.loc[j,"ContWW"]="K"+str(index)
            index+=1

        


# In[89]:


def YwCont():
    index=0
    for i in range(df["ContYW"].size):
        if(df.loc[i,"ContYW"]=='p'):
            CG=df.loc[i,"ContWW"]
            YS=df.loc[i,"YearlingSex"]
            d3=df.loc[i,"Date of weighing at 12 month"]
            if(d3=='0'):
                continue
            Yd=datetime.strptime(d3,"%Y-%m-%d")
            df.loc[i,"ContYW"]="Y"+str(index)
            for j in range(df["ContYW"].size):
                if(df.loc[j,"ContYW"]=='p'):
                    d4=df.loc[i,"Date of weighing at 12 month"]
                    if(d4=='0'):
                        continue
                    yd=datetime.strptime(d4,"%Y-%m-%d")
                    cg=df.loc[i,"ContWW"]
                    ys=df.loc[i,"YearlingSex"]
                    diff=int((yd-Yd).days)
                    if(cg==CG and ys==YS and diff<4):
                        df.loc[j,"ContYW"]="Y"+str(index)
            index+=1

        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




