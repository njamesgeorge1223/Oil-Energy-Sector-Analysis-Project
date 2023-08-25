#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyFunctions.py
 #
 #  File Description:
 #      This Python script, PyLogFunctions.py, contains generic Python functions
 #      for writing information to log files.  Here is the list:
 #
 #      ReturnCurrentDateAsString
 #      ReturnCurrentTimestampAsString
 #      DebugReturnObjectWriteObject
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/24/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyLogConstants as log_constant

import datetime

from datetime import date
from datetime import datetime


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyLogFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCurrentDateAsString
 #
 #  Function Description:
 #      This function returns the current date as a formatted string for the names
 #      of log files.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCurrentDateAsString():
    
    todayDateObject \
        = date \
            .today()

    return \
        todayDateObject \
            .strftime('%Y%m%d')


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCurrentTimestampAsString
 #
 #  Function Description:
 #      This function returns the current date and time as a formatted string
 #      for timepoint entries in log files.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCurrentTimestampAsString():
    
    nowDateTimeObject \
        = datetime \
            .now()
    
    return \
        nowDateTimeObject \
            .strftime \
                ('%m/%d/%Y %H:%M:%S')


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  DebugReturnObjectWriteObject
 #
 #  Function Description:
 #      This function takes an object as a parameter, and, if the global debug flag is true, 
 #      writes it to a debug file before returning the object to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DebugReturnObjectWriteObject \
        (inputObjectParameter):
    
    if log_constant.DEBUG_FLAG == True:
        
        log_constant \
            .debugTxtFile \
                .write \
                    (f'\n\n' + str(inputObjectParameter) + f'\n\n')
            
        return \
            inputObjectParameter
    
    else:
        
        log_constant \
            .logTxtFile \
                .write \
                    (f'\n\n' + str(inputObjectParameter) + f'\n\n')

