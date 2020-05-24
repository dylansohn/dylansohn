import pandas as pd


# In[106]:

df_bj = pd.read_excel("型号清单.xlsx")
df_bj.head()


# In[107]:

df_jg = pd.read_excel("Bravat Price list 海外牌价表--20200102.xlsx")
df_jg.head()


# In[108]:

df_jg = df_jg[['Item Code', 'Description', 'Specification']]
df_jg.head()


# In[109]:

df_merge = pd.merge(left=df_bj,right=df_jg,left_on="Item Code",right_on="Item Code")
df_merge.head()


# In[110]:

df_merge = df_merge.drop_duplicates(subset=None, keep='first', inplace=False)
df_merge.head()


# In[111]:

des_name = '报价单.xls'
df_merge.to_excel(des_name)

