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
 #      ReturnTradingPricesAsSeries
 #      ReturnCompleteTickerListFromYahooFinance
 #      ReturnAllCovidDataFromWHO
 #      ReturnOilEnergySectorCompanies
 #      ReturnFormattedAddressString
 #      ReturnOilSectorMarketIndexSeries
 #      ReturnGeographicDataFrame
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/22/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyFunctions as function
import PyLogSubRoutines as log_subroutine
import PyOilSectorAnalysisConstants as local_constant

import pandas as pd
import yahoo_fin
import yfinance as yf

import yahoo_fin.stock_info as stock_info

import datetime
import json
import requests

from io import StringIO
from PyOilSectorAnalysisConfig import geoapify_key


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
            
            log_subroutine \
                .PrintAndLogWriteText \
                    ('The function, ReturnHistoricalPricesSeries, '
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
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnTradingPricesAsSeries, '
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
        
        log_subroutine \
            .PrintAndLogWriteText \
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
                     None,
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
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnAllCovidDataFromWHO, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to retrieve COVID-19 Data '
                 + 'from the WHO.')
    
        return \
            None


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOilEnergySectorCompanies
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
    
    varianceMarketCapList \
        = []
    
    standardDeviationMarketCapList \
        = []
    
    standardErrorOfMeanList \
        = []
    
     
    log_subroutine \
        .PrintAndLogWriteText \
            (f'\nBegin retrieving oil company information...\n\n')

  

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
                
                log_subroutine \
                    .PrintAndLogWriteText \
                        (f'Trading for the ticker, {ticker}, begins ' \
                         + 'after the first day of the analysis period.\n')
                
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
        
                varianceMarketCapList \
                    .append \
                        (pd \
                            .Series \
                                (marketCapList) \
                            .var())
    
                standardDeviationMarketCapList \
                    .append \
                        (pd \
                            .Series \
                                (marketCapList) \
                            .std())
            
                standardErrorOfMeanList \
                    .append \
                        (pd \
                            .Series \
                                (marketCapList) \
                            .sem())
                
                
                log_subroutine \
                    .PrintAndLogWriteText \
                        (f'\nRetrieved information for {ticker} in the ' \
                         + f'{industryStringVariable} industry.\n\n')
        
        except:
        
            log_subroutine \
                .PrintAndLogWriteText \
                    (f'This ticker, {ticker}, does not have the required information.'
                     + '  Skipping...\n')
        

    log_subroutine \
        .PrintAndLogWriteText \
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
                         medianMarketCapList,
                         varianceMarketCapList,
                         standardDeviationMarketCapList,
                         standardErrorOfMeanList)),
                         columns \
                            = ['Ticker', 
                               'Company Name', 
                               'Industry', 
                               'Address',
                               'Market Cap (Min)', 
                               'Market Cap (Max)', 
                               'Market Cap (Mean)', 
                               'Market Cap (Median)',
                               'Market Cap (Var)',
                               'Market Cap (Stdev)',
                               'Market Cap (SEM)'])
    
    
    return \
        ReturnGeographicDataFrame \
            (companyDataFrame,
             'Address')


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
        
        log_subroutine \
            .PrintAndLogWriteText \
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
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The number of elements in the two function parameters are not equal. Exiting...\n')
        
        return \
            None
    
    
    log_subroutine \
        .PrintAndLogWriteText \
            ('Begin calculating oil company stock index...\n\n')

    
    for index, ticker in enumerate(tickerListParameter):
    
        try:
            
            if ticker == None \
                or ticker == '':
                
                log_subroutine \
                    .PrintAndLogWriteText \
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
            
            log_subroutine \
                .PrintAndLogWriteText \
                    (f"\nProcessed {ticker}'s contribution...\n")
            
            
        except:
        
            log_subroutine \
                .PrintAndLogWriteText \
                    (f'\nThis ticker, {ticker}, did not have historical stock prices. ' \
                     + 'Skipping...\n')
            
            
    log_subroutine \
        .PrintAndLogWriteText \
            (f'\nThe calculation of the oil company stock index is complete.\n')
    
        
    return \
        marketIndexSeries


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnGeographicDataFrame
 #
 #  Function Description:
 #      This function receives a input DataFrame, appends latitude and longitude onto
 #      a copy of the input DataFrame, and returns the copy to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is a input DataFrame.
 #  String
 #          addressFieldStringParameter
 #                          This parameter is the column name for the address information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnGeographicDataFrame \
        (inputDataFrameParameter,
         addressFieldStringParameter):

    inputDataFrame \
        = inputDataFrameParameter.copy()
    
    
    latitudeFloatList \
        = []
    
    longitudeFloatList \
        = []
    
    
    log_subroutine \
        .PrintAndLogWriteText \
            ('Retrieving latitudes and longitudes for addresses...\n')
    
    
    for index, company in inputDataFrame.iterrows():
        
        companyAddressStringVariable \
            = company[addressFieldStringParameter]

        urlStringVariable \
            = 'https://api.geoapify.com/v1/geocode/search?text=' \
              + f'{companyAddressStringVariable}&apiKey={geoapify_key}'

        try:

            geoResponse \
                = requests \
                    .get \
                        (urlStringVariable)

            geoResponse \
                .raise_for_status()

            informationDictionary \
                = geoResponse \
                    .json()

            
            latitudeFloatVariable \
                = informationDictionary \
                        ['features'] \
                            [0] \
                                ['properties'] \
                                    ['lat']

            longitudeFloatVariable \
                = informationDictionary \
                        ['features'] \
                            [0] \
                                ['properties'] \
                                    ['lon']
            
            log_subroutine \
                .PrintAndLogWriteText \
                    (f'\nIndex: {index}\n' \
                     + '\nCompany Information:\n'
                     + f'{company}\n\n' \
                     + f'Latitude: {latitudeFloatVariable}\n' \
                     + f'Longitude:  {longitudeFloatVariable}\n')
            
            
            latitudeFloatList \
                .append \
                    (latitudeFloatVariable)
            
            longitudeFloatList \
                .append \
                    (longitudeFloatVariable)

        except:
            
            log_subroutine \
                .PrintAndLogWriteText \
                    ('\nThe function, ReturnGeoDataFrame, ' \
                     + f'in file, {CONSTANT_LOCAL_FILE_NAME}, ' \
                     + f' for company:\n\n{company}\n\n' \
                     + 'did not find the requested address.  ' \
                     + 'Skipping...\n')
            
            
    tempDataFrame \
        = pd \
            .DataFrame \
                (list \
                    (zip \
                        (latitudeFloatList, 
                         longitudeFloatList)),
                         columns \
                            = ['Latitude', 
                               'Longitude'])
    
    return \
        pd \
            .concat \
                ([inputDataFrame, 
                  tempDataFrame], 
                 axis \
                     = 1)

