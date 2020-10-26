#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')


# In[5]:


df.shape


# In[6]:


pd.set_option('display.max_columns', 61)
pd.set_option('display.max_rows', 61)


# In[7]:


schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')


# In[8]:


df.head()


# In[9]:


schema_df


# In[10]:


schema_df.loc['Trans', 'QuestionText']


# In[11]:


schema_df.sort_index(inplace=True)


# In[12]:


schema_df


# In[13]:


filt = df['LanguageWorkedWith'].str.contains('Python', na=False)


# In[14]:


df.loc[filt, 'LanguageWorkedWith']


# In[15]:


filt


# In[16]:


df.rename(columns={'SOAccount': 'StackOwerflow'}, inplace=True)


# In[17]:


df


# In[18]:


df['StackOwerflow']


# In[19]:


df['StackOwerflow'].map({'Yes':True, 'No':False})


# In[20]:


df['StackOwerflow'] = df['StackOwerflow'].map({'Yes':True, 'No':False})


# In[21]:


df


# In[57]:


df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)


# In[59]:


df[['Country', 'ConvertedComp']].head(15)


# In[60]:


df['ConvertedComp'].nlargest(15)


# In[61]:


df.nsmallest(10, 'ConvertedComp')


# In[62]:


df['ConvertedComp'].median()


# In[46]:


df.median()


# In[47]:


df.describe()


# In[63]:


df['Trans'].count()


# In[64]:


df['Trans'].value_counts()


# In[65]:


schema_df.loc['WebframeWorkedWith']


# In[66]:


df['WebframeWorkedWith'].value_counts(normalize=True)


# In[67]:


df['Country'].value_counts()


# In[68]:


country_grp = df.groupby(['Country'])


# In[69]:


country_grp.get_group('India')


# In[70]:


filt = df['Country'] == 'Turkey'


# In[71]:


df.loc[filt]['WebframeWorkedWith'].value_counts()


# In[72]:


country_grp['WebframeWorkedWith'].value_counts(normalize=True).loc['Canada']


# In[73]:


country_grp['ConvertedComp'].median().loc['Turkey']


# In[74]:


country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Turkey']


# In[75]:


filt = df['Country'] == 'Turkey'


# In[76]:


df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()


# In[77]:


country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[78]:


country_respondents = df['Country'].value_counts()
country_respondents


# In[79]:


country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_uses_python


# In[80]:


python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False)
python_df


# In[81]:


python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)


# In[82]:


python_df


# In[83]:


python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents'])*100
python_df


# In[84]:


python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)


# In[85]:


python_df.head(50)


# In[86]:


python_df.loc['Turkey']


# In[87]:


df['YearsCode'].unique()


# In[88]:


df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df['YearsCode'].replace('More than 50 years', 51, inplace=True)


# In[89]:


df['YearsCode'] = df['YearsCode'].astype(float)


# In[90]:


df['YearsCode']


# In[97]:


filt = (df['Country'] == ('India'))
india_df = df.loc[filt]
india_df.head()


# In[98]:


india_df.to_csv('data/modified.csv')


# In[99]:


india_df.to_csv('data/modified.tsv', sep='\t')


# In[101]:


india_df.to_excel('data/modifier.xlsx')


# In[105]:


test = pd.read_excel('data/modifier.xlsx', index_col='Respondent')


# In[106]:


test.head()


# In[108]:


india_df.to_json('data/modifier.json', orient='records', lines=True)


# In[109]:


test = pd.read_json('data/modifier.json', orient='records', lines=True)


# In[110]:


test.head()


# In[ ]:




