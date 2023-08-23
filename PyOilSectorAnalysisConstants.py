#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyOilSectorAnalysisConstants.py
 #
 #  File Description:
 #      This Python script, PySubroutines.py, contains constants and enumerations 
 #      for Week 7, Project #1, tasks.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/22/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

from enum import Enum


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyOilSectorAnalysisConstants.py'


# In[3]:


SP_500_YAHOO_TICKER \
    = '^GSPC'

CRUDE_OIL_YAHOO_TICKER \
    = 'CL=F'

GOLD_YAHOO_TICKER \
    = 'GC=F'

TEN_YEAR_BOND_YIELD_YAHOO_TICKER \
    = '^TNX'

BITCOIN_YAHOO_TICKER \
    = 'BTC-USD'


WHO_COVID_19_DATA_URL \
    = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'


ALL_OIL_COMPANIES_FILE_PATH \
    = './Resources/AllOilCompanies.csv'


START_DATE \
    = '2020-01-03'

END_DATE \
    = '2022-10-16'


# In[4]:


class oilCompanyDisplayOptionsEnumeration(Enum):

    NAMES = 0

    NAMES_MARKET_CAP = 1
    
    NAMES_ADDRESS = 2
    
    ALL = 3

