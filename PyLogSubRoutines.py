#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyLogSubroutines.py
 #
 #  File Description:
 #      This Python script, PyLogSubroutines.py, contains generic Python subroutines
 #      for writing information to log files.  Here is the list:
 #
 #      CreateDirectory
 #      OpenLogAndDebugFiles
 #      PrintAndLogWriteText
 #      PrintAndDebugWriteText
 #      PrintAllWriteText
 #      BeginProgramExecution
 #      EndProgramExecution
 #      SetDebugMode
 #      SetLogMode
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/24/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyLogConstants as log_constant
import PyLogFunctions as log_function

import os


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyLogSubRoutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPandasBarChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine creates the Resources and Logs Folders if they do not exist.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          directoryNameStringParameter
 #                          This parameter is program name designation for the output files.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def CreateDirectory \
        (directoryNameStringParameter):
    
    try:
    
        doesExistFlagBooleanVariable \
            = os \
                .path \
                    .exists \
                        (directoryNameStringParameter)
    
        if doesExistFlagBooleanVariable == False:
        
            os \
                .makedirs \
                    (directoryNameStringParameter)
            
            print \
                (f'The program created directory, {directoryNameStringParameter}.\n')
    
    except:
        
        print \
            (f'The subroutine, CreateDriectory, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not create the directory, {directoryNameStringParameter}.')


# In[4]:


#*******************************************************************************************
 #
 #  Subroutine Name:  OpenLogAndDebugFiles
 #
 #  Subroutine Description:
 #      This subroutine opens the log and debug files for appending.  If they do not exist,
 #      the subroutine creates them.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          directoryNameStringParameter
 #                          This parameter is program name designation for the output files.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def OpenLogAndDebugFiles \
        (programDesignationStringParameter):
    
    try:

        currentDateStringVariable \
            = log_function \
                .ReturnCurrentDateAsString()

 
        log_constant.LOG_FILE_PATH \
            = log_constant.LOGS_DIRECTORY_PATH \
              + '/' \
              + currentDateStringVariable \
              + programDesignationStringParameter \
              + log_constant.BASE_LOG_FILE_NAME

        log_constant.DEBUG_FILE_PATH \
            = log_constant.LOGS_DIRECTORY_PATH \
                + '/' \
                + currentDateStringVariable \
                + programDesignationStringParameter \
                + log_constant.BASE_DEBUG_FILE_NAME
        
        
        if log_constant.LOG_FLAG == True:
        
            log_constant \
                .logTxtFile \
                    = open \
                        (log_constant.LOG_FILE_PATH, 
                         'a')
        
        if log_constant.DEBUG_FLAG == True:
        
            log_constant \
                .debugTxtFile \
                    = open \
                        (log_constant.DEBUG_FILE_PATH, 
                         'a')

    except:
        
        print \
            (f'The subroutine, SetLogsDebugPaths, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not open the debug and log files.')


# In[5]:


#*******************************************************************************************
 #
 #  Subroutine Name:  PrintAndLogWriteText
 #
 #  Subroutine Description:
 #      This subroutine prints the received message then writes the message to the log file.
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          messageStringParameter
 #                          This parameter is the input message String.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def PrintAndLogWriteText \
        (messageStringParameter \
            = ''):
    
    print \
        (messageStringParameter)
    
    timePointMessageStringVariable \
        = log_function \
            .ReturnTimePointMessage \
                (messageStringParameter)
    
    if log_constant.LOG_FLAG == True:
    
        log_constant \
            .logTxtFile \
                .write \
                    (timePointMessageStringVariable)    


# In[6]:


#*******************************************************************************************
 #
 #  Subroutine Name:  PrintAndDebugWriteText
 #
 #  Subroutine Description:
 #      This subroutine prints the received message then writes the message to the debug
 #      file if the global debug flag is true.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          messageStringParameter
 #                          This parameter is the input message String.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def PrintAndDebugWriteText \
        (messageStringParameter \
            = ''):
       
    timePointMessageStringVariable \
        = log_function \
            .ReturnTimePointMessage \
                (messageStringParameter)
        
        
    if log_constant.DEBUG_FLAG == True:
    
        print \
            (timePointMessageStringVariable)
    
        log_constant \
            .debugTxtFile \
                .write \
                    (timePointMessageStringVariable)
        
    elif log_constant.LOG_FLAG == True:
        
        log_constant \
            .logTxtFile \
                .write \
                    (timePointMessageStringVariable)


# In[7]:


#*******************************************************************************************
 #
 #  Subroutine Name:  PrintAllWriteText
 #
 #  Subroutine Description:
 #      This subroutine prints the received message, prints it, writes it to the log file
 #      and then to the debug file if the global debug flag is true.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          messageStringParameter
 #                          This parameter is the input message String.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def PrintAllWriteText \
        (messageStringParameter \
            = ''):
    
    print \
        (messageStringParameter)
    

    timePointMessageStringVariable \
        = log_function \
            .ReturnTimePointMessage \
                (messageStringParameter)

    
    if log_constant.LOG_FLAG == True:
    
        log_constant \
            .logTxtFile \
                .write \
                    (timePointMessageStringVariable)   

    if log_constant.DEBUG_FLAG == True:
    
        log_constant \
            .debugTxtFile \
                .write \
                    (timePointMessageStringVariable)


# In[8]:


#*******************************************************************************************
 #
 #  Subroutine Name:  BeginProgramExecution
 #
 #  Subroutine Description:
 #      This subroutine prints an announcement concerning program execution, creates the 
 #      appropriate Folders, and writes the same announcement to the log and debug files.
 #
 #
 #  Subroutine Parameters:
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

def BeginProgramExecution \
        (programDesignationStringParameter \
            = ''):
    
    try:

        CreateDirectory \
            (log_constant \
                .RESOURCES_DIRECTORY_PATH)
       
        CreateDirectory \
            (log_constant \
                .LOGS_DIRECTORY_PATH)


        OpenLogAndDebugFiles \
            (programDesignationStringParameter)


        messageStringVariable \
            = 'Program execution begins...\n\n'

        PrintAllWriteText \
            (messageStringVariable)

    except:
        
        print \
            (f'The subroutine, BeginProgramExecution, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + 'could not begin program execution.')    


# In[9]:


#*******************************************************************************************
 #
 #  Subroutine Name:  EndProgramExecution
 #
 #  Subroutine Description:
 #      This subroutine prints an announcement concerning the end of program execution,
 #      creates the appropriate Folders, and writes the same announcement to the log and 
 #      debug files.
 #
 #
 #  Subroutine Parameters:
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

def EndProgramExecution():
    
    try:
        
        currentTimeStampStringVariable \
            = log_function \
                .ReturnCurrentTimestampAsString()
                
        messageStringVariable \
            = f'Program execution ends at {currentTimeStampStringVariable}.\n\n\n\n'
        
        PrintAllWriteText \
            (messageStringVariable)
        
        
        if log_constant.LOG_FLAG == True:
            
            log_constant \
                .logTxtFile \
                    .close()

        if log_constant.DEBUG_FLAG == True:

            log_constant \
                .debugTxtFile \
                    .close()

    except:
        
        print \
            (f'The subroutine, EndProgramExecution, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + 'could not close the log and debug files.')   
        


# In[10]:


#*******************************************************************************************
 #
 #  Subroutine Name:  SetLogMode
 #
 #  Subroutine Description:
 #      This subroutine sets the value for the global debug flag (True/False).
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Boolean
 #          modeFlagBooleanParameter
 #                          This parameter is the desired Boolean value for the global 
 #                          debug flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def SetLogMode \
        (modeFlagBooleanParameter \
            = True):
    
    log_constant \
        .LOG_FLAG \
            = modeFlagBooleanParameter


# In[11]:


#*******************************************************************************************
 #
 #  Subroutine Name:  SetDebugMode
 #
 #  Subroutine Description:
 #      This subroutine sets the value for the global debug flag (True/False).
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Boolean
 #          modeFlagBooleanParameter
 #                          This parameter is the desired Boolean value for the global 
 #                          debug flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def SetDebugMode \
        (modeFlagBooleanParameter \
            = True):
    
    log_constant \
        .DEBUG_FLAG \
            = modeFlagBooleanParameter

