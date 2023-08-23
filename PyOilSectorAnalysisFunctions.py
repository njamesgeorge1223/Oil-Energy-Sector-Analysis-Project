#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyOilSectorAnalysisFunctions.py
 #
 #  File Description:
 #      This Python script, PyOilSectorAnalysisFunctions.py, contains generic 
 #      Python functions for completing common tasks in the Week #7, Project #1,
 #      Challenge.  Here is the list:
 #
 #      IsCompanyStartDateValidForAnalysis
 #      ReturnEconomicIndicatorPricesStandardFormat
 #      ReturnStylerObjectCOVIDStandardFormat
 #      DisplayFormattedMarketCapDataFrame
 #      ReturnIndustryMarketCapStatisticsSummary
 #      DisplayFormattedLeadingOilCompanyIndexWeights
 #      ReturnTopCompanyByIndustry
 #      ReturnOilCompanyStylerObjectStandardFormat
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/14/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyConstants as constant
import PyFunctions as function

import PyOilSectorAnalysisConstants as local_constant
    
import datetime


import numpy as np
import pandas as pd


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyOilSectorAnalysisFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  IsCompanyStartDateValidForAnalysis
 #
 #  Function Description:
 #      This function returns true if the start date for the stock's trading began
 #      at or before the analysis period.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Object
 #          yahooFinanceObjectParameter
 #                          This parameter is a object containing dictionaries about a
 #                          particular company.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def IsCompanyStartDateValidForAnalysis \
        (yahooFinanceObjectParameter):

    try:
        
        firstTradingDateTime \
            = datetime \
                .datetime \
                    .fromtimestamp \
                        (yahooFinanceObjectParameter \
                            .info \
                                ['firstTradeDateEpochUtc'])

        analysisStartDateTime \
            = datetime \
                .datetime \
                    .strptime \
                        (local_constant.START_DATE, 
                         '%Y-%m-%d')

            
        if analysisStartDateTime < firstTradingDateTime:
                
            return \
                False
        
        else:
            
            return \
                True
            
            
    except:
        
        print(f'The function, IsCompanyStartDateValidForAnalysis, '
              + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
              + f'was unable determine whether the trading start '
              + f'date of the stock came at or before the analysis'
              + f'start date.')
    
        return \
            False


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnEconomicIndicatorPricesStandardFormat
 #
 #  Function Description:
 #      This function receives a economic indicator historical prices DataFrame,
 #      formats a copy of it as a Styler Object, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ReturnEconomicIndicatorPricesStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        inputDataFrame \
            .index \
                .name \
                    = None
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                        '1.3px solid red',
                        'color':
                        'blue'}) \
                .format \
                    ({'Crude Oil':
                            constant.CURRENCY_FLOAT_FORMAT, 
                      'S&P 500':
                            constant.CURRENCY_FLOAT_FORMAT, 
                      'Gold':
                            constant.CURRENCY_FLOAT_FORMAT,
                      '10-Year Bond Yield':
                            constant.PERCENT_FLOAT_FORMAT}) 
        
    except:
            
        print \
            ('The function, ReturnEconomicIndicatorPricesStandardFormat, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to format an economic indicator historical prices '
             + 'DataFrame as a Styler object.')
        
        return \
            None


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectCOVIDStandardFormat
 #
 #  Function Description:
 #      This function receives a COVID-19 Data DataFrame, formats a copy of it 
 #       as a Styler Object, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def ReturnStylerObjectCOVIDStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        inputDataFrame \
            .index \
                .name \
                    = None
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                        '1.3px solid red',
                        'color':
                        'blue'}) \
                .format \
                    (precision \
                        = 0, 
                     thousands \
                        = ',', 
                     decimal \
                        = '.') \
                .highlight_min \
                    (color = 'yellow') \
                .highlight_max \
                    (color = 'lime')
        
    except:
            
        print \
            ('The function, ReturnStylerObjectCOVIDStandardFormat, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to format an COVID-19 new cases and new deaths '
             + 'DataFrame as a Styler object.')
        
        return \
            None


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  DisplayFormattedMarketCapDataFrame
 #
 #  Function Description:
 #      This function receives a market capitalization DataFrame, formats a copy of it 
 #       as a Styler Object, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayFormattedMarketCapDataFrame \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
    
        inputDataFrame \
            .index \
            .name \
                = None

        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 
                           'caption', 
                       'props':
                            [('color', 
                                  'black'), 
                             ('font-size', 
                                  '20px'),
                             ('font-style', 
                                  'bold'),
                             ('text-align', 
                                  'center')]}]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                            '1.3px solid red',
                        'color':
                            'blue'}) \
                .format \
                    ({'Ticker':
                        constant.GENERAL_TEXT_FORMAT, 
                      'Company Name':
                        constant.GENERAL_TEXT_FORMAT, 
                      'Industry':
                        constant.GENERAL_TEXT_FORMAT,
                      'Market Cap (Min)':
                        constant.CURRENCY_FLOAT_FORMAT,
                      'Market Cap (Max)':
                        constant.CURRENCY_FLOAT_FORMAT,
                      'Market Cap (Mean)':
                        constant.CURRENCY_FLOAT_FORMAT,
                      'Market Cap (Median)':
                        constant.CURRENCY_FLOAT_FORMAT}) \
                .highlight_max \
                    (subset \
                        = ['Market Cap (Min)',
                           'Market Cap (Max)',
                           'Market Cap (Mean)',
                           'Market Cap (Median)'],
                     color='lime') \
                .highlight_min \
                    (subset \
                        = ['Market Cap (Min)',
                           'Market Cap (Max)',
                           'Market Cap (Mean)',
                           'Market Cap (Median)'],
                     color='yellow') \
                .hide()
    except:
                
        print \
            ('The function, DisplayFormattedMarketCapDataFrame, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to format market capitalization DataFrame.')
        
        return \
            None


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnIndustryMarketCapStatisticsSummary
 #
 #  Function Description:
 #      This function receives a market capitalization DataFrame, calculates the statistics
 #      for a box plot, and resturns the statistics in a DataFrame.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          columnNameStringParameter
 #                          This parameter is the DataFrame column with the input Series 
 #                          information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnIndustryMarketCapStatisticsSummary \
        (inputDataFrameParameter,
         columnNameStringParameter):
    
    try:
    
        quantileSeries \
            = inputDataFrameParameter \
                .groupby \
                    ('Industry') \
                        [columnNameStringParameter] \
                .quantile \
                    ([0.25,
                      0.50,
                      0.75])
    
    
        industryList \
            = []
    
        lowerQuartileList \
            = []
    
        upperQuartileList \
            = []
    
        interquartileRangeList \
            = []
    
        lowerBoundList \
            = []
    
        upperBoundList \
            = []
    
        meanList \
            = []
    
        medianList \
            = []
    
        percentDifferenceList \
            = []
    
        numberOfCompaniesList \
            = []
    
        numberOfOutliersList \
            = []
    
    
        for index, quartile in enumerate(quantileSeries):
        
            modulusConditionIntegerVariable \
                = index % 3
        
        
            if modulusConditionIntegerVariable == 0:
            
                industryListStringVariable \
                    = quantileSeries.keys() \
                        [index] \
                        [0]
            
            
                lowerQuartileFloatVariable \
                    = quantileSeries \
                        [index]

                upperQuartileFloatVariable \
                    = quantileSeries \
                        [index + 2]

            
                interquartileRangeFloatVariable \
                    = upperQuartileFloatVariable - lowerQuartileFloatVariable

            
                lowerBoundFloatVariable \
                    = lowerQuartileFloatVariable - (1.5*interquartileRangeFloatVariable)

                upperBoundFloatVariable \
                    = lowerQuartileFloatVariable + (1.5*interquartileRangeFloatVariable)
            
            
                meanFloatVariable \
                    = inputDataFrameParameter \
                        .loc \
                            [inputDataFrameParameter \
                                 ['Industry'] \
                            == industryListStringVariable] \
                                 [columnNameStringParameter] \
                        .mean()

                medianFloatVariable \
                    = quantileSeries \
                        [index + 1]
            
                percentDifferenceFloatVariable \
                    = abs \
                        (meanFloatVariable - medianFloatVariable) \
                      / meanFloatVariable
            

                numberOfOutliersIntegerVariable \
                    = len \
                        (inputDataFrameParameter \
                             .loc \
                                 [(inputDataFrameParameter['Industry'] \
                                   == industryListStringVariable) \
                                  & ((inputDataFrameParameter[columnNameStringParameter] \
                                      < lowerBoundFloatVariable) \
                                  |  (inputDataFrameParameter[columnNameStringParameter] \
                                      > upperBoundFloatVariable))])
            
                industryList \
                    .append \
                        (industryListStringVariable)
            
            
                lowerQuartileList \
                    .append \
                        (lowerQuartileFloatVariable)
            
                upperQuartileList \
                    .append \
                        (upperQuartileFloatVariable)
            
            
                interquartileRangeList \
                    .append \
                        (interquartileRangeFloatVariable)
            
            
                lowerBoundList \
                    .append \
                        (lowerBoundFloatVariable)
    
                upperBoundList \
                    .append \
                        (upperBoundFloatVariable)
        
        
                meanList \
                    .append \
                        (meanFloatVariable)
            
                medianList \
                    .append \
                        (medianFloatVariable)
            
                percentDifferenceList \
                    .append \
                        (percentDifferenceFloatVariable)
        
        
                numberOfCompaniesList \
                    .append \
                        (inputDataFrameParameter \
                            .loc \
                                [inputDataFrameParameter['Industry'] \
                                 == industryListStringVariable] \
                             ['Ticker'] \
                            .count())
        
        
                numberOfOutliersList \
                    .append \
                        (numberOfOutliersIntegerVariable)
            

        summaryStatisticsDataFrame \
            = pd \
                .concat({'Industry': pd.Series(industryList), 
                         'Lower Quartile': pd.Series(lowerQuartileList),
                         'Upper Quartile': pd.Series(upperQuartileList),
                         'Interquartile Range': pd.Series(interquartileRangeList),
                         'Lower Boundary': pd.Series(lowerBoundList),
                         'Upper Boundary': pd.Series(upperBoundList),
                         'Mean': pd.Series(meanList),
                         'Median': pd.Series(medianList),
                         '% Difference': pd.Series(percentDifferenceList),
                         'Number of Companies': pd.Series(numberOfCompaniesList),
                         'Number of Outliers': pd.Series(numberOfOutliersList)},
                        axis = 1)

        return \
            summaryStatisticsDataFrame
    
    except:
        
        print \
            ('The function, ReturnIndustryMarketCapStatisticsSummary, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to calculate market capitalization statistics.')
        
        return \
            None


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  DisplayFormattedLeadingOilCompanyIndexWeights
 #
 #  Function Description:
 #      This function receives an oil company index weight DataFrame, formats it, and
 #      returns a Styler object.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          columnNameStringParameter
 #                          This parameter is the DataFrame column with the input Series 
 #                          information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayFormattedLeadingOilCompanyIndexWeights \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
    
        inputDataFrame \
            .index \
            .name \
                = None

    
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 
                           'caption', 
                       'props':
                            [('color', 
                                  'black'), 
                             ('font-size', 
                                  '16px'),
                             ('font-style', 
                                  'bold'),
                             ('text-align', 
                                  'center')]}]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                            '1.3px solid red',
                        'color':
                            'blue'}) \
                .format({'Ticker':
                                constant.GENERAL_FORMAT, 
                         'Company Name':
                                constant.GENERAL_FORMAT, 
                         'Industry':
                                constant.GENERAL_FORMAT,   
                         'Market Cap (Median)':
                                constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                         'Index Weight':
                                constant.FLOAT_FORMAT}) \
                .highlight_max \
                    ('Market Cap (Median)',
                     color \
                         = 'lime') \
                .highlight_min \
                    ('Market Cap (Median)',
                     color \
                         = 'yellow') \
                .hide()
    
    except:
        
        print \
            ('The function, DisplayFormattedLeadingOilCompanyIndexWeights, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to format an oil company index weight DataFrame.')
        
        return \
            None


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnTopCompanyByIndustry
 #
 #  Function Description:
 #      This function receives an oil company index weight DataFrame, formats it, and
 #      returns a Styler object.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          criterionStringVariable
 #                          This parameter is the column name used for the sorting.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnTopCompanyByIndustry \
        (inputDataFrame,
         criterionStringVariable):
    
    try:
    
        maximumMedianMarketCapByIndustrySeries \
            = inputDataFrame \
                .groupby \
                    ('Industry') \
                        [criterionStringVariable] \
                .max()


        topTickerList \
            = []

        topCompanyList \
            = []

        industryList \
            = []

        medianMarketCapList \
            = []

    
        for index, marketCap in enumerate(maximumMedianMarketCapByIndustrySeries):
    
            topTickerStringVariable \
                = (inputDataFrame \
                      .loc \
                          [inputDataFrame \
                               [criterionStringVariable] \
                           == marketCap] \
                               ['Ticker']) \
                  .iloc[0]
    
            topCompanyNameStringVariable \
                = (inputDataFrame \
                        .loc \
                            [inputDataFrame \
                                ['Ticker'] \
                             == topTickerStringVariable] \
                               ['Company Name']) \
                  .iloc[0]
    
            industryStringVariable \
                = maximumMedianMarketCapByIndustrySeries \
                    .keys() \
                        [index]

    
            topTickerList \
                .append \
                    (topTickerStringVariable)
    
            topCompanyList \
                .append \
                    (topCompanyNameStringVariable)
    
            industryList \
                .append \
                    (industryStringVariable)
    
            medianMarketCapList \
                .append \
                    (marketCap)
    
    
        indexWeightList \
            = []

        totalMedianMarketCapFloatVariable \
            = sum \
                (medianMarketCapList)


        for index, marketCap in enumerate(medianMarketCapList):
        
            indexWeightFloatVariable \
                = marketCap \
                  / totalMedianMarketCapFloatVariable
    
            indexWeightList \
                .append \
                    (indexWeightFloatVariable)

    
        indexWeightDataFrame \
            = pd \
                .DataFrame \
                    (list \
                        (zip \
                            (topTickerList, 
                             topCompanyList, 
                             industryList, 
                             medianMarketCapList, 
                             indexWeightList)),
                             columns \
                                = ['Ticker', 
                                   'Company Name', 
                                   'Industry', 
                                   'Market Cap (Median)', 
                                   'Index Weight'])
    
    
        return \
            indexWeightDataFrame
    
    except: 
        
        print \
            ('The function, ReturnTopCompanyByIndustry, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return the top company by industry.')
        
        return \

    None


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOilCompanyStylerObjectStandardFormat
 #
 #  Function Description:
 #      This function receives an input DataFrame anf formatting parameters and returns
 #      a formatted Styler Object.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the column name used for the sorting.
 #  Integer
 #          displayOptionIntegerParameter
 #                          This parameter specifies which columns the program displays.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/22/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnOilCompanyStylerObjectStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter,
         displayOptionIntegerParameter \
             = local_constant \
                 .oilCompanyDisplayOptionsEnumeration \
                     .NAMES \
                         .value):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        if displayOptionIntegerParameter \
            == local_constant \
                 .oilCompanyDisplayOptionsEnumeration \
                     .NAMES \
                         .value:
            
            return \
                inputDataFrame \
                    .style \
                    .set_caption \
                        (captionStringParameter) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        ({'Ticker':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Company Name':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Industry':
                            constant.GENERAL_TEXT_FORMAT,
                          'Market Cap (Min)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Max)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Mean)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Address',
                                'Market Cap (Min)', 
                                'Market Cap (Max)', 
                                'Market Cap (Mean)', 
                                'Market Cap (Median)'],
                         axis = 'columns') \
                    .hide \
                        (axis \
                          = 'index')
        
        elif displayOptionIntegerParameter \
                == local_constant \
                 .oilCompanyDisplayOptionsEnumeration \
                     .NAMES_MARKET_CAP \
                         .value:
        
            return \
                inputDataFrame \
                    .style \
                    .set_caption \
                        (captionStringParameter) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        ({'Ticker':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Company Name':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Industry':
                            constant.GENERAL_TEXT_FORMAT,
                          'Market Cap (Min)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Max)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Mean)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Address'],
                         axis = 'columns') \
                    .hide \
                        (axis \
                          = 'index')
        
        elif displayOptionIntegerParameter \
                == local_constant \
                     .oilCompanyDisplayOptionsEnumeration \
                         .NAMES_ADDRESS \
                             .value:
            
            return \
                inputDataFrame \
                    .style \
                    .set_caption \
                        (captionStringParameter) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        ({'Ticker':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Company Name':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Industry':
                            constant.GENERAL_TEXT_FORMAT,
                          'Market Cap (Min)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Max)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Mean)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Market Cap (Min)', 
                                'Market Cap (Max)', 
                                'Market Cap (Mean)', 
                                'Market Cap (Median)'],
                         axis = 'columns') \
                    .hide \
                        (axis \
                          = 'index')
        
        elif displayOptionIntegerParameter \
                == local_constant \
                     .oilCompanyDisplayOptionsEnumeration \
                         .ALL \
                             .value:
            
            return \
                inputDataFrame \
                    .style \
                    .set_caption \
                        (captionStringParameter) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        ({'Ticker':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Company Name':
                            constant.GENERAL_TEXT_FORMAT, 
                          'Industry':
                            constant.GENERAL_TEXT_FORMAT,
                          'Market Cap (Min)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Max)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Mean)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_FORMAT}) \
                    .hide \
                        (axis \
                          = 'index')
        
        else:
            
            print \
                ('The program did not specify a valid display option ' \
                 + 'for the oil company DataFrame in subroutine, ' \
                 + 'ReturnOilCompanyStylerObjectStandardFormat')
        
        
    except:
            
        print \
            (f'The subroutine, ReturnOilCompanyStylerObjectStandardFormat, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to format a DataFrame as a Styler object.')
        
        return \
            None


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOilSectorIndicesStandardFormat
 #
 #  Function Description:
 #      This function receives an oil energy sector indicies DataFrame, formats
 #      a copy of it as a Styler Object, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/22/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ReturnOilSectorIndicesStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        inputDataFrame \
            .index \
                .name \
                    = None
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                        '1.3px solid red',
                        'color':
                        'blue'}) \
                .format \
                    ({'OESI (Top)':
                            constant.CURRENCY_FLOAT_FORMAT, 
                      'OESI (All)':
                            constant.CURRENCY_FLOAT_FORMAT}) 
        
    except:
            
        print \
            ('The function, ReturnOilSectorIndicesStandardFormat, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to format an oil energy sector indices '
             + 'DataFrame as a Styler object.')
        
        return \
            None

