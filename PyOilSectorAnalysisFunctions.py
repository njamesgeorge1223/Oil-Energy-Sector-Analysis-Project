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
 #      ReturnIndustryMarketCapStatisticsSummary
 #      DisplayFormattedLeadingOilCompanyIndexWeights
 #      ReturnTopCompanyByIndustry
 #      ReturnOilCompanyStylerObjectStandardFormat
 #      ReturnOilSectorIndicesStandardFormat
 #      ConvertOilCompanyToGeoDataFrame
 #      ReturnSharesSeriesAlignedWithPrices
 #      ReturnNormalizedOutstandingSharesToPricesSeries
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/14/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyConstants as constant
import PyFunctions as function
import PyLogSubRoutines as log_subroutine

import PyOilSectorAnalysisAPIFunctions as api_function
import PyOilSectorAnalysisConstants as local_constant
    
import datetime

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
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, IsCompanyStartDateValidForAnalysis, '
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
            
        log_subroutine \
            .PrintAndLogWriteText \
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
            
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnStylerObjectCOVIDStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to format an COVID-19 new cases and new deaths '
                 + 'DataFrame as a Styler object.')
        
        return \
            None


# In[6]:


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
                    = inputDataFrameParameter \
                        .loc \
                            [inputDataFrameParameter \
                                 ['Industry'] \
                            == industryListStringVariable] \
                                 [columnNameStringParameter] \
                        .median()
                    #= quantileSeries \
                    #    [index + 1]
            
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
                         'Number of Companies': pd.Series(numberOfCompaniesList),
                         'Number of Outliers': pd.Series(numberOfOutliersList)},
                        axis = 1)

        return \
            summaryStatisticsDataFrame
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnIndustryMarketCapStatisticsSummary, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to calculate market capitalization statistics.')
        
        return \
            None


# In[7]:


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
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, DisplayFormattedLeadingOilCompanyIndexWeights, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to format an oil company index weight DataFrame.')
        
        return \
            None


# In[8]:


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
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnTopCompanyByIndustry, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to return the top company by industry.')
        
        return \

    None


# In[9]:


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
                            constant.GENERAL_TEXT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Address',
                                'Market Cap (Min)', 
                                'Market Cap (Max)', 
                                'Market Cap (Mean)', 
                                'Market Cap (Median)',
                                'Market Cap (Var)',
                                'Market Cap (Stdev)',
                                'Market Cap (SEM)',
                                'Latitude',
                                'Longitude'],
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
                          'Market Cap (Mean)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Stdev)':
                            constant.FLOAT_FORMAT,
                          'Market Cap (SEM)':
                            constant.FLOAT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Address',
                                'Market Cap (Min)',
                                'Market Cap (Max)',
                                'Market Cap (Var)',
                                'Latitude',
                                'Longitude'],
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
                          'Address':
                            constant.GENERAL_TEXT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Market Cap (Min)', 
                                'Market Cap (Max)', 
                                'Market Cap (Mean)', 
                                'Market Cap (Median)',
                                'Market Cap (Var)',
                                'Market Cap (Stdev)',
                                'Market Cap (SEM)',
                                'Latitude',
                                'Longitude'],
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
                          'Address':
                            constant.GENERAL_TEXT_FORMAT,           
                          'Market Cap (Mean)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Median)':
                            constant.CURRENCY_FLOAT_FORMAT,
                          'Market Cap (Stdev)':
                            constant.FLOAT_FORMAT,
                          'Market Cap (SEM)':
                            constant.FLOAT_FORMAT}) \
                    .hide \
                        (subset \
                             = ['Market Cap (Min)',
                                'Market Cap (Max)',
                                'Market Cap (Var)',
                                'Latitude',
                                'Longitude'],
                         axis = 'columns') \
                    .hide \
                        (axis \
                          = 'index')
        
        else:
            
            log_subroutine \
                .PrintAndLogWriteText \
                    ('The program did not specify a valid display option ' \
                     + 'for the oil company DataFrame in subroutine, ' \
                     + 'ReturnOilCompanyStylerObjectStandardFormat')
        
        
    except:
            
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, ReturnOilCompanyStylerObjectStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to format a DataFrame as a Styler object.')
        
        return \
            None


# In[10]:


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
            
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnOilSectorIndicesStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to format an oil energy sector indices '
                 + 'DataFrame as a Styler object.')
        
        return \
            None


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  ConvertOilCompanyToGeoDataFrame
 #
 #  Function Description:
 #      This function receives an inputDataFrame, and creates a geoDataFrame from it.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          frameDictionaryParameter
 #                          This parameter is a input DataFrame.
 #  String
 #          addressFieldStringParameter
 #                          This parameter is the column name for the address information.
 #  String
 #          sizeFieldStringParameter
 #                          This parameter is the column name for the marker size information.
 #  Integer
 #          sizeOrderFactorIntegerParameter
 #                          This optional parameter is the order of magnitude to reduce
 #                          the marker size parameter.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/23/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ConvertOilCompanyToGeoDataFrame \
        (inputDataFrameParameter,
         sizeFieldStringParameter,
         sizeOrderFactorIntegerParameter \
            = 1):

    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
        
        
        if sizeOrderFactorIntegerParameter == 0:
            
            sizeOrderFactorIntegerParameter = 1
        
        
        inputDataFrame \
            [sizeFieldStringParameter] \
                = inputDataFrame \
                       [sizeFieldStringParameter] \
                            / sizeOrderFactorIntegerParameter
        
        frameDictionary \
            = {'Ticker': 
                    inputDataFrame \
                       ['Ticker'], 
               'Company Name': 
                    inputDataFrame \
                       ['Company Name'], 
               'Industry': 
                    inputDataFrame \
                       ['Industry'], 
               'Address': 
                    inputDataFrame \
                       ['Address'],
               'Latitude': 
                    inputDataFrame \
                       ['Latitude'],             
               'Longitude': 
                    inputDataFrame \
                       ['Longitude'],            
               'Marker Size': 
                    inputDataFrame \
                       [sizeFieldStringParameter], 
               }
        

        return \
            pd \
                .DataFrame \
                    (frameDictionary)
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ConvertOilCompanyToGeoDataFrame, ' \
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' \
                 + 'was unable to convert an oil company DataFrame ' \
                 + 'to a GeoDataFrame.')
        
        return \
            None 


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  ConvertOilCompanyToGeoDataFrame
 #
 #  Function Description:
 #      This function receives an inputDataFrame, and creates a geoDataFrame from it.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          pricesSeriesParameter
 #                          This parameter is a the Series with the reference indices
 #  Series
 #          sharesSeriesParameter
 #                          This parameter is the Series with the requisite values.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/31/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnSharesSeriesAlignedWithPrices \
        (pricesSeriesParameter,
         sharesSeriesParameter):
    
    try:
        
        pricesFirstIndexDateObject \
            = pricesSeriesParameter.index[0]
    
        sharesFirstIndexDateObject \
            = sharesSeriesParameter.index[0]
    
    
        indexList \
            = []
    
        valueList \
            = []
    
    
        pricesIndex = 0
    
        sharesIndex = 0
    
    
        if pricesFirstIndexDateObject < sharesFirstIndexDateObject:
        
            while pricesSeriesParameter.index[pricesIndex] < sharesFirstIndexDateObject:
                
                indexList \
                    .append \
                        (pricesSeriesParameter \
                             .index \
                                 [pricesIndex])
                
                valueList \
                    .append \
                        (sharesSeriesParameter \
                            [sharesIndex])
                
                pricesIndex += 1
        
        
            if pricesFirstIndexDateObject in sharesSeriesParameter.index:
            
                indexList \
                    .append \
                        (pricesSeriesParameter \
                             .index \
                                 [pricesIndex])
                
                valueList \
                    .append \
                        (sharesSeriesParameter \
                             [sharesIndex])
            
                pricesIndex += 1
        
        elif pricesFirstIndexDateObject > sharesFirstIndexDateObject:
        
            while sharesSeriesParameter.index[sharesIndex] < pricesFirstIndexDateObject:
 
                sharesIndex += 1
               
                
            indexList \
                .append \
                    (pricesSeriesParameter \
                         .index \
                             [pricesIndex])
                
            valueList \
                .append \
                    (sharesSeriesParameter \
                         [sharesIndex])
        
            pricesIndex += 1
        
        
        pricesSeriesSizeIntegerVariable \
            = pricesSeriesParameter \
                .count()
    
        sharesSeriesSizeIntegerVariable \
            = sharesSeriesParameter \
                .count()
    

        for loopIndex in range (pricesIndex, pricesSeriesSizeIntegerVariable):     

            if loopIndex == pricesIndex \
                and sharesIndex < sharesSeriesSizeIntegerVariable:
            
                if pricesSeriesParameter.index[pricesIndex] == sharesSeriesParameter.index[sharesIndex]:
                
                    indexList \
                        .append \
                            (pricesSeriesParameter \
                                 .index \
                                     [pricesIndex])
                
                    valueList \
                        .append \
                            (sharesSeriesParameter \
                                 [sharesIndex])
                
                
                    if pricesIndex < pricesSeriesSizeIntegerVariable - 1:
                
                        pricesIndex += 1
                
                    if sharesIndex < sharesSeriesSizeIntegerVariable - 1:
                
                        sharesIndex += 1
                
                elif sharesIndex == sharesSeriesSizeIntegerVariable - 1:
                
                    while pricesIndex < pricesSeriesSizeIntegerVariable:
                        
                        indexList \
                            .append \
                                (pricesSeriesParameter \
                                     .index \
                                         [pricesIndex])
                
                        valueList \
                            .append \
                                (sharesSeriesParameter \
                                     [sharesIndex])
                    
                        pricesIndex += 1    
            
                elif pricesSeriesParameter.index[pricesIndex] < sharesSeriesParameter.index[sharesIndex]:
                
                    while pricesIndex < pricesSeriesSizeIntegerVariable \
                            and pricesSeriesParameter.index[pricesIndex] < sharesSeriesParameter.index[sharesIndex]:

                        indexList \
                            .append \
                                (pricesSeriesParameter \
                                     .index \
                                         [pricesIndex])
                
                        valueList \
                            .append \
                                (sharesSeriesParameter \
                                     [sharesIndex - 1])
                    
                        pricesIndex += 1
            
                else:
                    
                    if pricesIndex < pricesSeriesSizeIntegerVariable \
                            and sharesIndex < sharesSeriesSizeIntegerVariable:
                        
                        indexList \
                            .append \
                                (pricesSeriesParameter \
                                     .index \
                                         [pricesIndex])
                
                        valueList \
                            .append \
                                (sharesSeriesParameter \
                                     [sharesIndex])
                        
                    while sharesIndex < sharesSeriesSizeIntegerVariable \
                            and sharesSeriesParameter.index[sharesIndex] < pricesSeriesParameter.index[pricesIndex]:

                        sharesIndex += 1
                    
                    
                if sharesIndex < sharesSeriesSizeIntegerVariable \
                    and sharesSeriesParameter.index[sharesIndex] not in pricesSeriesParameter.index:
                
                    while sharesIndex < sharesSeriesSizeIntegerVariable - 1\
                            and sharesSeriesParameter.index[sharesIndex] not in pricesSeriesParameter.index:

                        sharesIndex += 1
    
    
        return \
            pd \
                .Series \
                    (valueList, 
                     index \
                         = indexList)
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnSharesSeriesAlignedWithPrices, ' \
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' \
                 + 'was unable to convert extrapolate share values ' \
                 + 'a Series with historical prices indices.')
        
        return \
            None


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnNormalizedOutstandingSharesToPricesSeries
 #
 #  Function Description:
 #      This function receives a full shares Series, extrapolates its values to fit
 #      a historical price Series, and returns the new Series to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          pricesSeriesParameter
 #                          This parameter is a the Series with the reference indices
 #  Series
 #          sharesSeriesParameter
 #                          This parameter is the Series with the requisite values.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/31/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnNormalizedOutstandingSharesToPricesSeries \
        (pricesSeriesParameter,
         sharesSeriesParameter):
    
    if sharesSeriesParameter.count() == 0:
        
        print('The length of the shares Series is zero.')
        
        return None
    
    elif sharesSeriesParameter.count() == 1:
        
        tempSeries \
            = pricesSeriesParameter.copy()
        
        sharesSeries \
            = (tempSeries.astype(int) * 0) + sharesSeriesParameter[0]
        
        return \
            sharesSeries
    
    
    firstPricesSeries \
        = function \
            .ReturnSeriesWithUniqueIndicesLastValues \
                (pricesSeriesParameter)

    firstSharesSeries \
        = function \
            .ReturnSeriesWithUniqueIndicesLastValues \
                (sharesSeriesParameter)
    
    
    pricesSeries \
        = function \
            .ReturnSeriesWithDateObjectIndices \
                (firstPricesSeries)
    
    sharesSeries \
        = function \
            .ReturnSeriesWithDateObjectIndices \
                (firstSharesSeries)
    
    return \
        ReturnSharesSeriesAlignedWithPrices \
            (pricesSeries,
             sharesSeries)     


# In[ ]:




