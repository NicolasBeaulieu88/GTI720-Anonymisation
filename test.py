# importation des librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# importation du jeux de données
adult_df = pd.read_csv('https://github.com/tisl-lab/data-privacy-class/blob/main/data/adult_small.csv?raw=true')


#Algo
def k_anonymity(adult_df,qid,k):
    adult_df = adult_df[qid]
    grouped = adult_df.groupby(qid).size().reset_index(name='Count');
    grouped = grouped[grouped['Count']<k]
    return len(grouped)==0

#Question 21
res = k_anonymity(adult_df,['Sex', 'Race'],2)
print("Q 21")
print(res)

#Question 22-24

def k_test_pairs(k_param):
    list = []
    for column in columns:
        for column2 in columns:
            if(column != column2):
                res = k_anonymity(adult_df,[column,column2],k_param)
                if(res):
                    list.append([column,column2])
    return list

def k_test_triplets(k_param):
    list = []
    for column in columns:
        for column2 in columns:
            for column3 in columns:
                if(column == column2 or column2 == column3 or column == column3):
                    pass
                else:
                    res = k_anonymity(adult_df,[column,column2,column3],k_param)
                    if(res):
                        list.append([column,column2,column3])
    return list


columns = adult_df.columns
k_param = 2
print("for k_param: "+str(k_param))
print(k_test_pairs(k_param))
k_param = 5
print("for k_param: "+str(k_param))
print(k_test_pairs(k_param))
k_param = 2
print("for k_param: "+str(k_param))
print(k_test_triplets(k_param))


#Algo 25-26
def l_diversity(adult_df,qid,k,s,l):
    if(k_anonymity(adult_df,qid,k) == False):
        return False
    else:
        adult_df = adult_df.groupby(qid)[s].nunique()
        return adult_df.min()>=l

#Q 27-28
print("Q 27")
print(l_diversity(adult_df,['Sex','Race'],3,'Occupation',2))
print("Q 28 a)")
print(l_diversity(adult_df,['Sex','Race'],3,'Age',2))
print("Q 28 b)")
print(l_diversity(adult_df,['Sex','Race'],3,'Workclass',2))
print("Q 28 c)")
print(l_diversity(adult_df,['Sex','Race'],3,'Relationship',2))
print("Q 29 d)")
print(l_diversity(adult_df,['Sex','Race'],3,'Country',2))

#Q 29
def generalise(adult_df,qid,n):
    return adult_df[qid].map(lambda x: str(x)[:-n] + '0' * n)

print("Q 29")
print(generalise(adult_df,'Zip',2).to_frame())
