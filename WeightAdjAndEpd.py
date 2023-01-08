#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,date,timedelta


# In[2]:


df=pd.read_csv("D:/Dimitra/DATA/CorrectedAge.csv")


# In[3]:


df


# In[4]:


df["ABW"]=0
df["AWW"]=0
df["AYW"]=0


# In[5]:



def EpdCal(birthDate,Gender,AgeOfDam,BW,WeaningWTDate,WW,YDD,YW):

    BD = datetime.strptime(birthDate, "%Y-%m-%d")





    #Dictionary to store the Adjustment values for Birth Weight
    AdjForBW={2:8,3:5,4:2,11:3,5:0,6:0,7:0,8:0,9:0,10:0,12:3,13:3,14:3,15:3,16:3,17:3,18:3,19:3,20:3}

    #Dictionary to store the Adjustment values for Weining weight
    AdjForWW={2:{'b':60,'h':54},3:{'b':40,'h':36},4:{'b':20,'h':18},11:{'b':20,'h':18},5:{'b':0,'h':0},6:{'b':0,'h':0},7:{'b':0,'h':0},8:{'b':0,'h':0},9:{'b':0,'h':0},10:{'b':0,'h':0},
             
             12:{'b':20,'h':18},13:{'b':20,'h':18},14:{'b':20,'h':18},15:{'b':20,'h':18},16:{'b':20,'h':18},17:{'b':20,'h':18},18:{'b':20,'h':18},19:{'b':20,'h':18},20:{'b':20,'h':18},
             }
#     AdjForWW= pd.DataFrame.from_dict(AdjForWW)
    #Getting the approraite valu of birth weight adjustmment as per Age of the Dam
    BWAdj=AdjForBW[AgeOfDam]

    #Calculating the Adjusted Birth weight to overcome the age factor of the Dam
    ABW=BW+BWAdj


    #Weaning Weight Calculation



    #Cheking Wheather the weaning weight date is appropraite for weanig weight calculation i.e betweeen 160 to 250 days
    WD = datetime.strptime(WeaningWTDate, "%Y-%m-%d")
    DaysWeanig=(WD-BD).days
    print(DaysWeanig)
    if DaysWeanig<160 or DaysWeanig>250:
        print("The time of weaning should be betweeen 160 and 250 days but the animal does not satisfy this cretirea")
        return 0,0,0
    else:

        #Getting the Age factor
        if(Gender==0):
            g='h'
        else :
            g='b'
        AdjFact=AdjForWW[AgeOfDam][g]

        A_205_WW=(((WW-BW)*205)/DaysWeanig)+BW+AdjFact

        #Yearlling Weight Calcuation




        #Cheking Wheather the YEarling weight date is appropraite for weanig weight calculation i.e betweeen 320 to 410 days
        YD = datetime.strptime(YDD, "%Y-%m-%d")
        DaysYearing=(YD-BD).days
        if DaysYearing<320 or DaysYearing>410:
            print("The time of Yearling should be betweeen 320 and 410 days but the animal does not satisfy this cretirea")
            return 0,0,0
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


# In[6]:


for i in range(df["Gender"].size):
    bd=str(df.loc[i,"Birth date"])
    G=df.loc[i,"Gender"]
    A=df.loc[i,"Age_of_Dam"]
    bw=df.loc[i,"Birth weight"]
    wd=str(df.loc[i,"Weaning_Date"])
    ww=df.loc[i,"Weaning_Weight"]
    yd=df.loc[i,"Date of weighing at 12 month"]
    yw=df.loc[i,"Weight at 12 months"]
    if(bw=='0' or wd=='0' or yd=='0'):
        continue
    tup1=EpdCal(bd,G,A,bw,wd,ww,yd,yw)
    df.loc[i,"ABW"]=tup1[0]
    df.loc[i,"AWW"]=tup1[1]
    df.loc[i,"AYW"]=tup1[2]

    


# In[7]:


df


# In[8]:


df.to_csv('D:\Dimitra\DATA\AdjustedCalculated.csv')


# In[8]:


df["ContBW"]='p'


# In[9]:


index=0
for i in range(df["ContBW"].size):
    if(df.loc[i,"ContBW"]=='p'):
        d1=df.loc[i,"Birth date"]
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
                if(diff<90):
                    df.loc[j,"ContBW"]="C"+str(index)
        index+=1

        


# In[10]:


df


# In[11]:


df["ContWW"]='p'


# In[12]:


df


# In[13]:


index=0
for i in range(df["ContWW"].size):
    if(df.loc[i,"ContWW"]=='p'):
        d1=df.loc[i,"Birth date"]
        d2=df.loc[i,"Weaning_Date"]
        if(d1=='0' or d2=='0'):
            continue
        Bd=datetime.strptime(d1, "%Y-%m-%d")
        Wd=datetime.strptime(d2, "%Y-%m-%d")
        df.loc[i,"ContWW"]="K"+str(index)
        for j in range(df["ContWW"].size):
            if(df.loc[j,"ContWW"]=='p'):
                d3=df.loc[j,"Birth date"]
                d4=df.loc[j,"Weaning_Date"]
                if(d3=='0' or d4=='0'):
                    continue
                bd=datetime.strptime(d3, "%Y-%m-%d")
                wd=datetime.strptime(d4, "%Y-%m-%d")
                diff1=int((bd-Bd).days)
                diff2=int((wd-Wd).days)
                if(diff1<90 and diff2<3 ):
                    df.loc[j,"ContWW"]="K"+str(index)
        index+=1

        


# In[14]:


df


# In[15]:


df["ContYW"]='p'


# In[16]:


index=0
for i in range(df["ContYW"].size):
    if(df.loc[i,"ContYW"]=='p'):
        d1=df.loc[i,"Birth date"]
        d2=df.loc[i,"Weaning_Date"]
        d3=df.loc[i,"Date of weighing at 12 month"]
        if(d1=='0' or d2=='0' or d3=='0'):
            continue
        Bd=datetime.strptime(d1, "%Y-%m-%d")
        Wd=datetime.strptime(d2, "%Y-%m-%d")
        Yd=datetime.strptime(d3, "%Y-%m-%d")
        df.loc[i,"ContYW"]="Y"+str(index)
        for j in range(df["ContYW"].size):
            if(df.loc[j,"ContYW"]=='p'):
                d4=df.loc[j,"Birth date"]
                d5=df.loc[j,"Weaning_Date"]
                d6=df.loc[j,"Date of weighing at 12 month"]
                if(d3=='0' or d4=='0' or d5=='0'):
                    continue
                bd=datetime.strptime(d4, "%Y-%m-%d")
                wd=datetime.strptime(d5, "%Y-%m-%d")
                yd=datetime.strptime(d6, "%Y-%m-%d")
                diff1=int((bd-Bd).days)
                diff2=int((wd-Wd).days)
                diff3=int((Yd-yd).days)
                if(diff1<90 and diff2<3 and diff3<3 ):
                    df.loc[j,"ContYW"]="Y"+str(index)
        index+=1

        


# In[17]:


df


# In[18]:


df.to_csv('D:\Dimitra\DATA\ContCreated.csv')


# In[ ]:





# In[ ]:




