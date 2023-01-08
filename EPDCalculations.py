#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("D:\Dimitra\DATA\properCont.csv")
pd.set_option('display.max_columns', None)
df.drop("Unnamed: 0",axis=1,inplace=True)


# In[3]:


from datetime import datetime,date,time,timedelta


# In[4]:


for i in range(df["Gender"].size):
    a=df.loc[i,"Weaning_Date"]
    if(a=='0'):
        continue
    wd=datetime.strptime(a,"%Y-%m-%d")
#     print(wd)
    b=wd+timedelta(180)
    b=b.date()
    df.loc[i,"Date of weighing at 12 month"]=str(b)
#     print(b)


# In[5]:


# df["Date of weighing at 12 month"]=df["Weaning_Date"]+timedelta(180)


# In[6]:


df["Breed"]="Angus"


# In[7]:


df["BreedingBw"]=0
df["AvgBW"]=0


# In[ ]:





# In[8]:


def AvgBW():
    dict={}
    for i in range(df["AvgBW"].size):
        cont=df.loc[i,"ContBW"]
        if(cont in dict.keys()):
            df.loc[i,"AvgBW"]=dict[cont]
        else:
            sum=0
            n=1
            for j in range(df["AvgBW"].size):
                if(df.loc[j,"ContBW"]==cont):
    #                 print(j)
                    sum+=df.loc[j,"ABW"]
                    n+=1
            df.loc[i,"AvgBW"]=sum/n
            dict[cont]=sum/n


# In[9]:


def BwEPD():
    for i in range(df["BreedingBw"].size):
        a=df.loc[i,"ABW"]
        b=df.loc[i,"AvgBW"]
        df.loc[i,"BreedingBw"]=a-b
        df.loc[i,"Birth weight EPD"]=(a-b)/2
    


# In[10]:


AvgBW()
BwEPD()


# In[11]:


df.head()


# In[12]:


df["BreedingWw"]=0
df["AvgWW"]=0


# In[13]:


def AvgWW():
    dict1={}
    for i in range(df["AvgWW"].size):
        cont=df.loc[i,"ContWW"]
        if(cont in dict1.keys()):
            df.loc[i,"AvgWW"]=dict1[cont]
        else:
            sum=0
            n=1
            for j in range(df["AvgWW"].size):
                if(df.loc[j,"ContWW"]==cont):
    #                 print(j)
                    sum+=df.loc[j,"AWW"]
                    n+=1
            df.loc[i,"AvgWW"]=sum/n
            dict1[cont]=sum/n


# In[14]:


def WwEPD():
    for i in range(df["BreedingWw"].size):
        a=df.loc[i,"AWW"]
        b=df.loc[i,"AvgWW"]
        df.loc[i,"BreedingWw"]=a-b
        df.loc[i,"Weaning Weight EPD"]=(a-b)/2
    


# In[15]:


AvgWW()
WwEPD()


# In[16]:


df.head()


# In[17]:


df["BreedingYw"]=0
df["AvgYW"]=0


# In[18]:


def AvgYW():
    dict2={}
    for i in range(df["AvgYW"].size):
        cont=df.loc[i,"ContYW"]
        if(cont in dict2.keys()):
            df.loc[i,"AvgYW"]=dict2[cont]
        else:
            sum=0
            n=1
            for j in range(df["AvgYW"].size):
                if(df.loc[j,"ContYW"]==cont):
    #                 print(j)
                    sum+=df.loc[j,"AYW"]
                    n+=1
            df.loc[i,"AvgYW"]=sum/n
            dict2[cont]=sum/n


# In[19]:


def YwEPD():
    for i in range(df["BreedingYw"].size):
        a=df.loc[i,"AYW"]
        b=df.loc[i,"AvgYW"]
        df.loc[i,"BreedingYw"]=a-b
        df.loc[i,"Yearling Weight EPD"]=(a-b)/2
    


# In[20]:


AvgYW()
YwEPD()


# In[21]:


df.head()


# In[22]:


df.drop("Long Yearling Weight EPD",axis=1,inplace=True)
df.drop("Weaning Weight Maternal EPD",axis=1,inplace=True)


# In[23]:


df


# In[24]:


df["Actual_Scrotal_Circumfrence"]=0


# In[27]:


Scrotal_Adj={
    
"Angus":0.0374,
"Red Angus":0.0324,
"Brangus":0.0708,
"Charolais":0.0505,
"Gelbvieh":0.0505,
"Hereford":0.0425,
"Polled Hereford":0.0305,
"Limousin":0.0467,
"Salers":0.0574,
"Simmental":0.0543
    
}
# df_Scrotal_Adj=pd.DataFrame(Scrotal_Adj, columns=["Breed","Factor"])


# In[ ]:





# In[28]:



import random
for i in range(df["Actual_Scrotal_Circumfrence"].size):
    if(df.loc[i,"Gender"]==0):
        continue
    a=35*random.random()
    df.loc[i,"Actual_Scrotal_Circumfrence"]=a
    


# In[29]:


df


# In[30]:


a=df["Date of weighing at 12 month"]


# In[31]:


df


# In[32]:


a


# In[33]:


df["Scrotal_Date"]=0


# In[34]:


df["Scrotal_Date"]=a


# In[35]:


df["AdjScrotal"]=0


# In[36]:


from datetime import datetime,time,date


# In[37]:


for i in range(df["AdjScrotal"].size):
    if(df.loc[i,"Actual_Scrotal_Circumfrence"]==0):
        continue
    d1=df.loc[i,"Scrotal_Date"]
    d2=df.loc[i,"Birth date"]
    if(d1=='0' or d2=='0'):
        continue
#     datetime.strptime(d3,"%Y-%m-%d")
    SD=datetime.strptime(d1,"%Y-%m-%d")
    BD=datetime.strptime(d2,"%Y-%m-%d")
    days=(SD-BD).days
    fact=Scrotal_Adj[df.loc[i,"Breed"]]
    a=np.abs(365-days)
    df.loc[i,"AdjScrotal"]=(a*fact)+df.loc[i,"Actual_Scrotal_Circumfrence"]


# In[38]:


df["AvgScrotal"]=0
df["BreedingSc"]=0
df["EPD_Scrotal"]=0


# In[39]:


fact


# In[40]:


def AvgSc():
    dict3={}
    for i in range(df["AvgScrotal"].size):
        cont=df.loc[i,"ContWW"]
        if(cont in dict3.keys()):
            df.loc[i,"AvgScrotal"]=dict3[cont]
        else:
            sum=0
            n=1
            for j in range(df["AvgScrotal"].size):
                if(df.loc[j,"ContWW"]==cont):
    #                 print(j)
                    sum+=df.loc[j,"AdjScrotal"]
                    n+=1
            df.loc[i,"AvgScrotal"]=sum/n
            dict3[cont]=sum/n


# In[41]:


def ScEPD():
    for i in range(df["EPD_Scrotal"].size):
        a=df.loc[i,"AdjScrotal"]
        b=df.loc[i,"AvgScrotal"]
        df.loc[i,"BreedingSc"]=a-b
        df.loc[i,"EPD_Scrotal"]=(a-b)/2
    


# In[42]:


AvgSc()
ScEPD()


# In[43]:


df


# In[44]:


df["HipHeight"]=0


# In[45]:


for i in range(df["HipHeight"].size):
    r=(random.random())
    n=random.randint(30,60)
    df.loc[i,"HipHeight"]=r+n


# In[ ]:





# In[46]:


a=df["Date of weighing at 12 month"]
df["HipDate"]=a


# In[ ]:





# In[47]:


df["FrameScore"]=0


# In[48]:


df


# In[49]:


for i in range(df["FrameScore"].size):
    d1=df.loc[i,"HipDate"]
    d2=df.loc[i,"Birth date"]
    if(d1=='0' or d2=='0'):
        continue
#     datetime.strptime(d3,"%Y-%m-%d")
    HD=datetime.strptime(d1,"%Y-%m-%d")
    BD=datetime.strptime(d2,"%Y-%m-%d")
#     print(HD)
#     print(BD)
    diff=(HD-BD).days
#     print(diff)
    if(diff>1440):
        diff=1440
    if(df.loc[i,"Gender"]==1 and diff>630):
        Ht=df.loc[i,"HipHeight"]
        FC=((((((((((-0.5662-0.0115) * diff) - 0.1264) * Ht)+0.0000648) * diff) * Ht+0.000003) * (diff**2))+0.0057) * (Ht**2))
        df.loc[i,"FrameScore"]=FC
    elif((df.loc[i,"Gender"]==0) and diff>630):
        Ht=df.loc[i,"HipHeight"]
        FC=((((((((-19.42-0.00417) * diff) + 0.5263) * Ht)+0.0000014) * (diff**2)) - 0.0000001) * (Ht**2))
        df.loc[i,"FrameScore"]=FC
    elif((df.loc[i,"Gender"]==1) and diff>150 and diff<=630):
        Ht=df.loc[i,"HipHeight"]
        FC=-11.548+(0.4878 * Ht)-(0.0289 * diff)+(0.00001947 * (diff**2))+(0.0000334 * Ht * diff)
        df.loc[i,"FrameScore"]=FC
    elif((df.loc[i,"Gender"]==0) and diff>150 and diff<=630):
        Ht=df.loc[i,"HipHeight"]
        FC=-11.7086 + (0.4723 * Ht) - (0.0239 * diff) + (0.0000146 * (diff**2)) + (0.0000759 * Ht * diff)
        df.loc[i,"FrameScore"]=FC
    else:
        continue
        
        


# In[50]:



df["AvgFrameScore"]=0
df["BreedingFrame"]=0
df["EPD_Frame"]=0


# In[51]:


def AvgFs():
    dict4={}
    for i in range(df["AvgFrameScore"].size):
        cont=df.loc[i,"ContYW"]
        if(cont in dict4.keys()):
            df.loc[i,"AvgFrameScore"]=dict4[cont]
        else:
            sum=0
            n=1
            for j in range(df["AvgFrameScore"].size):
                if(df.loc[j,"ContYW"]==cont):
    #                 print(j)
                    sum+=df.loc[j,"FrameScore"]
                    n+=1
            df.loc[i,"AvgFrameScore"]=sum/n
            dict4[cont]=sum/n


# In[52]:


def FsEPD():
    for i in range(df["EPD_Frame"].size):
        a=df.loc[i,"FrameScore"]
        b=df.loc[i,"AvgFrameScore"]
        df.loc[i,"BreedingFrame"]=a-b
        df.loc[i,"EPD_Frame"]=(a-b)/2
    


# In[53]:


AvgFs()
FsEPD()


# In[54]:


df


# In[ ]:


# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


# In[ ]:


# df=pd.read_csv("D:\Dimitra\DATA\properCont.csv")
# pd.set_option('display.max_columns', None)
# # df.drop("Unnamed: 0",axis=1,inplace=True)


# In[55]:


df.to_csv("D:\Dimitra\DATA\EpdsCalculated.csv")


# In[56]:


df=pd.read_csv("D:\Dimitra\DATA\EpdsCalculated.csv")


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




