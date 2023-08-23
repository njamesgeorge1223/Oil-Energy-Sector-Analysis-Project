#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyOilSectorAnalysisSubroutines.py
 #
 #  File Description:
 #      This Python script, PySubroutines.py, contains Python subroutines for Week # 7,
 #      Project #1 tasks.  Here is the list:
 #
 #      DisplaySeriesCountAndRedundancies
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/22/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyFunctions as function

import matplotlib.pyplot as plt


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyOilSectorAnalysisSubRoutines.py'


# In[3]:


def DisplaySeriesCountAndRedundancies \
        (inputSeriesParameter,
         seriesDescriptionStringParameter):
    
    numberOfTickersIntegerVariable \
        = inputSeriesParameter.count()

    numberOfRedundanciesIntegerVariable \
        = function \
            .ReturnNumberOfRedundanciesInSeries \
                (inputSeriesParameter)

    print \
        (f'There are now {numberOfTickersIntegerVariable} stock tickers '
         + f'with {numberOfRedundanciesIntegerVariable} '
         + f'redundancies in {seriesDescriptionStringParameter}.')


# In[ ]:




