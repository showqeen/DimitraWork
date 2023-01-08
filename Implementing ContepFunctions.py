#!/usr/bin/env python
# coding: utf-8

# In[104]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,date
import random


# In[105]:


df=pd.read_csv('D:\Dimitra\DATA\DataForContGrps.csv')


# In[106]:


df.drop("Unnamed: 0",inplace=True,axis=1)


# In[107]:


df


# In[120]:


df.columns


# In[108]:


df.columns=df.columns.str.strip()


# In[109]:


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

        


# In[110]:


def WwCont():
    index=0
    for i in range(df["ContWW"].size):
        if(df.loc[i,"ContWW"]=='p'):
            d1=df.loc[i,"Weaning_Date"]
            if(d1=='0'):
                continue
            Wd=datetime.strptime(d1, "%Y-%m-%d")
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

        


# In[111]:


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
                    d4=df.loc[j,"Date of weighing at 12 month"]
                    if(d4=='0'):
                        continue
                    yd=datetime.strptime(d4,"%Y-%m-%d")
                    cg=df.loc[j,"ContWW"]
                    ys=df.loc[j,"YearlingSex"]
                    diff=int((yd-Yd).days)
                    if(cg==CG and ys==YS and diff<4 ):
                        df.loc[j,"ContYW"]="Y"+str(index)
            index+=1

        


# In[112]:


df.loc[1,"Date of weighing at 12 month"]


# In[113]:


BwCont()


# In[114]:


df


# In[115]:


WwCont()


# In[116]:


df


# In[117]:


YwCont()


# In[ ]:





# In[ ]:





# In[118]:


df


# In[119]:


df.to_csv("D:\Dimitra\DATA\properCont.csv")


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




