
# coding: utf-8

# # Importância do uso de gráficos

# In[ ]:

import pandas as pd
import numpy as np
get_ipython().magic('matplotlib inline')


# In[ ]:

datasauro = pd.read_csv('Datasaurus_data.csv', names=['X', 'Y'], decimal=',', sep=';')


# In[ ]:

datasauro.head()


# In[ ]:

datasauro.describe()


# In[ ]:

datasauro.corr()


# In[ ]:

datasauro.plot.scatter('X', 'Y');


# ## Dozen datasource

# In[ ]:

dozen = pd.read_csv('DatasaurusDozen.csv', decimal=',', sep=';')


# In[ ]:

dozen.head()


# In[ ]:

dozen.tail()


# In[ ]:

dozen.pivot_table(index='dataset', values=['x', 'y'], aggfunc=[np.mean, np.std])


# In[ ]:

dozen.groupby('dataset').apply(lambda df: df.plot.scatter('x', 'y', title=df.name));


# In[ ]:



