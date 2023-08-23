#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyOilSectorAnalysisAPIFunctions.py
 #
 #  File Description:
 #      This Python script, PyAPIFunctions.py, contains Python functions for API
 #      data retrieval related to Week #7, Project #1.  Here is the list:
 #
 #      ReturnTradingValuesAsSeries
 #      ReturnCompleteTickerListFromYahooFinance
 #      ReturnAllCovidDataFromWHO
 #      ReturnOilEnergySectorCompanies
 #      ReturnOilSectorMarketIndexSeries
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/14/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyFunctions as function
import PyOilSectorAnalysisConstants as local_constant

import datetime

import pandas as pd
import yfinance as yf
import yahoo_fin.stock_info as stock_info

import requests
from io import StringIO


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyOilSectorAnalysisAPIFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnTradingPricesAsSeries
 #
 #  Function Description:
 #      This function receives a Yahoo Finance ticker and returns a Series containing
 #      trading values for the analysis period.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          tickerStringParameter
 #                          This parameter is the Yahoo Finance ticker for the stock,
 #                          or index in question.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ReturnTradingPricesAsSeries \
        (tickerStringParameter):
    
    try:
            
        if tickerStringParameter == None \
            or tickerStringParameter == '':
            
            print('The function, ReturnHistoricalPricesSeries, '
                  + 'did not have a symbol passed to it ' 
                  + f'as a parameter.  Exiting...\n')
            
            return \
                None
                
   
        stockYahooFinanceObject \
            = yf \
                .Ticker \
                    (tickerStringParameter)
        
      
        historicalPricesSeries \
            = (stockYahooFinanceObject \
                .history \
                    (start \
                         = local_constant \
                            .START_DATE, 
                     end \
                        = local_constant \
                            .END_DATE)) \
                                ['Close']
        
        return \
            historicalPricesSeries
            
    except:
        
        print('The function, ReturnHistoricalPricesSeries, '
              + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
              + 'was unable retrieve historical prices for the '
              + f'ticker, {tickerStringParameter}.\n')
        
        return \
            None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCompleteTickerListFromYahooFinance
 #
 #  Function Description:
 #      This function uses an Yahoo Finance API to transfer all tickers in its 
 #      database into a List.  The script sorts the List alphabetically and 
 #      removes any redundancies before returning the List to the caller.
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
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCompleteTickerListFromYahooFinance():

    try:
    
        tickerList \
            = stock_info.tickers_sp500() \
                + stock_info.tickers_nasdaq() \
                    + stock_info.tickers_dow() \
                        + stock_info.tickers_other()
        
        tickerList \
            .sort()
        
        return \
            [i for n, i in enumerate (tickerList) \
             if i not in tickerList [:n]]
    
    except:
        
        print \
            ('The function, ReturnCompleteTickerListFromYahooFinance, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to retrieve a List of tickers '
             + 'from Yahoo Finance.')
    
        return \
            None


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnAllCovidDataFromWHO
 #
 #  Function Description:
 #      This function uses an WHO API to transfer all available COVID-19 Data
 #      for all countries into a DataFrame, which the function returns to the
 #      caller.
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
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnAllCovidDataFromWHO():

    try:
    
        currentResponseObject \
            = requests \
                .get \
                    (local_constant.WHO_COVID_19_DATA_URL)

        dataStringIO \
            = StringIO \
                (currentResponseObject.text)

        
        tempDataFrame \
            = function \
                .ReturnCSVFileAsDataFrame \
                    (dataStringIO, 
                     False)

        tempDataFrame \
            .rename \
                (columns \
                     = {'ï»¿Date_reported': 
                            'Date Reported', 
                        'Country_code': 
                            'Country Code',
                        'Country': 
                            'Country',
                        'WHO_region': 
                            'WHO Region',
                        'New_cases': 
                            'New Cases',
                        'Cumulative_cases': 
                            'Cumulative Cases',
                        'New_deaths': 
                            'New Deaths',
                        'Cumulative_deaths': 
                            'Cumulative Deaths'},
                 inplace \
                     = True)
    
    
        return \
            tempDataFrame
    
    except:
        
        print \
            ('The function, ReturnAllCovidDataFromWHO, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to retrieve COVID-19 Data '
             + 'from the WHO.')
    
        return \
            None


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOilEnergySectorStockTickers
 #
 #  Function Description:
 #      This function receives a list of tickers and returns those for companies
 #      that belong to an oil industry and whose trading date began at or before 
 #      the analysis period.  Information concerning the process is displayed and
 #      written to a log file in the Resources Folder.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          tickerListParameter
 #                          This parameter is a list of tickers from Yahoo Finance.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnOilEnergySectorCompanies \
            (tickerListParameter):

    tickerList \
        = []
    
    companyNameList \
        = []
    
    industryList \
        = []
    
    addressList \
        = []
    
    minimumMarketCapList \
        = []
    
    maximumMarketCapList \
        = []
    
    meanMarketCapList \
        = []
    
    medianMarketCapList \
        = []
    
     
    print \
        (f'\nBegin retrieving oil company information...\n')
    
    print()
  

    for ticker in tickerListParameter:
    
        try:
            
            if ticker == None \
                or ticker == '':
            
                continue
                

            stockYahooFinanceObject \
                = yf \
                    .Ticker \
                        (ticker)
            
            
            firstTradingDateTime \
                = datetime \
                    .datetime \
                        .fromtimestamp \
                            (stockYahooFinanceObject \
                                .info \
                                     ['firstTradeDateEpochUtc'])
            
            anaylysisStartDateTime \
                = datetime \
                    .datetime \
                        .strptime \
                            (local_constant.START_DATE, 
                             '%Y-%m-%d')
            
            if anaylysisStartDateTime < firstTradingDateTime:
                
                print (f'Trading for the ticker, {ticker}, begins ' \
                       + 'after the first day of the analysis period.')
                
                print()
                
                continue
            
            
        
            industryStringVariable \
                = stockYahooFinanceObject \
                    .info \
                        ['industry']

            if industryStringVariable.find('Oil') != -1 \
               and industryStringVariable != 'Independent Oil & Gas':      

                companyNameStringVariable \
                    = stockYahooFinanceObject \
                        .info \
                            ['longName']
                
                addressStringVariable \
                    = ReturnFormattedAddressString \
                        (stockYahooFinanceObject)
                
                
                outstandingSharesList \
                    = stockYahooFinanceObject \
                        .get_shares_full \
                            (start = local_constant.START_DATE, 
                             end = local_constant.END_DATE) \
                        .astype \
                            (float) \
                        .tolist()
                
                closingStockPriceList \
                    = stockYahooFinanceObject \
                        .history \
                            (start = local_constant.START_DATE, 
                             end = local_constant.END_DATE) \
                                ['Close'] \
                        .tolist()
                
                marketCapList \
                    = list \
                        (map \
                            (lambda x, y: x * y, 
                                 outstandingSharesList, 
                                 closingStockPriceList))
                
                
                tickerList \
                    .append \
                        (ticker)
                
                companyNameList \
                    .append \
                        (companyNameStringVariable)
                
                industryList \
                    .append \
                        (industryStringVariable)
                
                addressList \
                    .append \
                        (addressStringVariable)
                
                minimumMarketCapList \
                    .append \
                        (pd \
                            .Series \
                                (marketCapList) \
                            .min())
    
                maximumMarketCapList \
                    .append \
                        (pd \
                            .Series \
                                (marketCapList) \
                            .max())

                meanMarketCapList \
                    .append \
                        (pd \
                            .Series \
                                 (marketCapList) \
                            .mean())
    
                medianMarketCapList \
                    .append \
                        (pd \
                            .Series \
                                (marketCapList) \
                            .median())
            
            
                print \
                    (f'\nRetrieved information for {ticker} in the ' \
                     + f'{industryStringVariable} industry.\n\n')
        
        except:
        
            print \
                (f'This ticker, {ticker}, does not have the required information.'
                 + '  Skipping...\n')
        

    print \
        (f'\nThe retrievel of oil company information is complete.\n')
    
   
    companyDataFrame \
        = pd \
            .DataFrame \
                (list \
                    (zip \
                        (tickerList, 
                         companyNameList, 
                         industryList, 
                         addressList,
                         minimumMarketCapList, 
                         maximumMarketCapList, 
                         meanMarketCapList, 
                         medianMarketCapList)),
                         columns \
                            = ['Ticker', 
                               'Company Name', 
                               'Industry', 
                               'Address',
                               'Market Cap (Min)', 
                               'Market Cap (Max)', 
                               'Market Cap (Mean)', 
                               'Market Cap (Median)'])
    
    
    return \
        companyDataFrame


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFormattedAddressString
 #
 #  Function Description:
 #      This function receives a Yahoo Finance API object for a company, retrieves address
 #      information, and returns the formatted address as a String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          tickerListParameter
 #                          This parameter is a list of tickers from Yahoo Finance.
 #  Boolean
 #          marketCapFlagBooleanVariable
 #                          This parameter indicates whether the DataFrame includes
 #                          market capitalization data.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnFormattedAddressString \
        (yahooFinanceObjectParameter):
    
    try:
    
        streetAddressStringVariable \
            = yahooFinanceObjectParameter \
                .info \
                    ['address1']
        
        cityStringVariable \
            =  yahooFinanceObjectParameter \
                .info \
                    ['city']
        
        countryStringVariable \
            = yahooFinanceObjectParameter \
                .info \
                    ['country']
        
        
        if countryStringVariable == 'United States' \
           or countryStringVariable == 'Canada':
            
            stateStringVariable \
                = yahooFinanceObjectParameter \
                    .info \
                        ['state']
            
            zipCodeStringVariable \
                = yahooFinanceObjectParameter \
                    .info \
                        ['zip']
        
            addressStringVariable \
                = f'{streetAddressStringVariable}, ' \
                  + f'{cityStringVariable}, ' \
                  + f'{stateStringVariable}, ' \
                  + f'{zipCodeStringVariable}, ' \
                  + f'{countryStringVariable}'
          
        elif countryStringVariable == 'United Kingdom' \
             or countryStringVariable == 'Bermuda' \
             or countryStringVariable == 'Denmark':
            
            zipCodeStringVariable \
                = yahooFinanceObjectParameter \
                    .info \
                        ['zip']
            
            addressStringVariable \
                = f'{streetAddressStringVariable}, ' \
                  + f'{cityStringVariable}, ' \
                  + f'{zipCodeStringVariable}, ' \
                  + f'{countryStringVariable}'
            
        else:
 
            addressStringVariable \
                = f'{streetAddressStringVariable}, ' \
                  + f'{cityStringVariable}, ' \
                  + f'{countryStringVariable}'
        
        return \
            addressStringVariable
        
    except:
        
        print \
            ('The function, ReturnFormattedAddressString, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to retrieve and format a company '
             + 'address through the Yahoo Finance API.')
    
        return \
            None


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOilSectorMarketIndexSeries
 #
 #  Function Description:
 #      This function a list of tickers and index weights to calculate an index over time.
 #      The function returns to index to the caller as a Series.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Strings
 #          tickerListParameter
 #                          This parameter is a list of tickers from Yahoo Finance.
 #  List of Floats
 #          indexWeightListParameter
 #                          This parameter is a list of index weights corresponding
 #                          to the ticker list parameter.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnOilSectorMarketIndexSeries \
        (tickerListParameter,
         indexWeightListParameter):

    firstSeriesFlagBooleanValue = True
    
    
    if len(tickerListParameter) != len(indexWeightListParameter):
        
        print \
            (f'The number of elements in the two function parameters are not equal. Exiting...\n')
        
        return \
            None
    
    
    print \
        ('Begin calculating oil company stock index...\n')
    
    print()
    
    
    for index, ticker in enumerate(tickerListParameter):
    
        try:
            
            if ticker == None \
                or ticker == '':
                
                print \
                    ('\nThere was no ticker. Skipping...\n')
            
                continue
                
                
            stockYahooFinanceObject \
                = yf \
                    .Ticker \
                        (ticker)
    
    
            temporarySeries \
                = stockYahooFinanceObject \
                    .history \
                        (start \
                             = local_constant \
                                 .START_DATE, 
                         end \
                             = local_constant \
                                 .END_DATE) \
                            ['Close']

            
            if firstSeriesFlagBooleanValue == True:
                
                marketIndexSeries \
                    = temporarySeries * indexWeightListParameter[ index ]
                
                firstSeriesFlagBooleanValue \
                    = False
                    
            else:
                
                marketIndexSeries \
                    = marketIndexSeries \
                        + (temporarySeries * indexWeightListParameter[index])
            
            print \
                    (f"\nProcessed {ticker}'s contribution...\n")
            
            
        except:
        
            print \
                (f'\nThis ticker, {ticker}, did not have historical stock prices. ' \
                 + 'Skipping...\n')
            
            
    print \
        (f'\nThe calculation of the oil company stock index is complete.\n')
    
        
    return \
        marketIndexSeries

