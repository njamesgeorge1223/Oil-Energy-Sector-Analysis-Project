![maksym-kaharlytskyi-u13zBF4r56A-unsplash](https://github.com/SIWhang213/Project-1-group-4/assets/137141385/500f11cf-8bc1-478b-837d-383e914413e9)

## Project #1, Group #4: 

-----

# Did the COVID-19 Pandemic Affect the Oil Energy Sector?

-----
The Oil & Gas Energy Sector has always been a topic of interest to many due to the very nature of its business: a commodity that virtually everyone must frequently purchase, either directly or indirectly, to conduct the vagaries of daily life.  Thus, what factors affect, drive, or influence the oil industry is more than a mere topic of curiosity, as any unexpected disruptions can carry far reaching effects for individuals, groups, countries, or even the world.  For this project, we delve into this topic during the COVID-19 pandemic to answer these questions.

•	How strong is the relationship between the prices of oil company shares and the price of crude oil?

•	Is there a relationship between the number of daily COVID-19 cases or deaths and the prices of crude oil or oil company equities?

•	If there is no significant relationship between COVID-19 numbers and these prices, is there one among other economic metrics in this study?

To this end, we focused our efforts on assembling a sample space sufficient to produce valid results; but, throughout this undertaking, it contracted markedly.  Our initial analysis extended daily from January 1, 2020, to December 31, 2022, for 1,095 days.  Due to the New Year’s Day holiday precluding trading, the period shortened to 1,092 days ( January 2, 2020, to December 29, 2022).  A review of closing share price data through Yahoo Finance’s application programming interface (API) revealed that trading days do not include weekends, holidays, and other special days: this factor reduced the number of days to 755.  Moreover, an inspection of World Health Organization (WHO) API data disclosed that COVID-19 numbers did not begin until January 3, 2020, and daily numbers changed to weekly numbers after October 16, 2022. Understandably, these conditions reduced the number of samples to 702 ( January 3, 2020, to October 14, 2022).  Albeit difficult, these decisions were a trade-off between decreased validity from fewer sample points and increased integrity from compatible datasets.  We made the necessary choices to strike the best balance possible.

This inquiry continued with data collection.  The WHO’s API provided us with a full worldwide COVID-19 pandemic dataset, which we narrowed down to the appropriate country, categories, and dates.  This data complemented the Yahoo Finance API download of daily prices for crude oil, the S&P 500, gold, and U.S. Treasury 10-Year Bond Yields.  For all that, after completing these tasks, we were faced with a dilemma: how to construct a benchmark to best characterize Oil & Gas Energy Sector equities.  To this end, our fundamental question in this matter became, “What most accurately expresses a company’s value,” and we found our solution through the Efficient Market Hypothesis, which states that share prices reflect all information; therefore, market capitalization, the product of share price and number of company shares, should be the best way to establish a company’s value at any given time.

To find all publicly traded oil companies, a download of available tickers from Yahoo Finance ‘s API, over 11,000, began the process; a Python script then extracted only those tickers belonging to oil companies whose share trading began prior to the analysis period: the operation also included retrieving additional company information and calculating each company’s minimum, maximum, mean, median, variance, standard deviation, and standard error of the mean (SEM) market capitalization values.  

Side-by-side pie charts of the Oil & Gas Energy Sector breakdown by industry from number of companies, mean market capitalization, and median market capitalization imparted an insight.  Although the industry percentages were about the same for mean and median values, the industry, Oil & Gas Integrated, held the highest share for both while possessing the next to smallest number of companies.  Even though the mean and median market capitalizations appeared ostensibly similar from these diagrams, they still required further investigation.

Statistical analyses of the mean and median market capitalizations by industry exhibit the same situation: significant margins between mean and median values, small and consistent standard deviations except for one industry (Oil & Gas Integrated), numerous outliers, and heavily left-skewed distributions.  Most notably, the difference between means and medians determined the next course of action.  Under normal circumstances, the mean best represents central tendency, but is sensitive to skewed data and extreme values.  With these conditions, the median is the more suitable measure and better summarizes the dataset.  Even in a mitigated situation, the median is superior because data, in practice, tends to be more dynamic, and static observations may not be fully accurate.  As a result, we decided to use the median market capitalization in the construction of Oil & Gas Energy Sector indices.  

To depict the Oil & Gas Energy Sector in equity markets, we created indices from two portfolios, one with all the oil companies and one with only the top six oil companies; each top company has the highest median market capitalization in one of six oil industries: ConocoPhillips (Oil & Gas E&P), Enbridge Inc. (Oil & Gas Midstream), Marathon Petroleum Corporation (Oil & Gas Refining & Marketing), Precision Drilling Corporation (Oil & Gas Drilling), Shell plc (Oil & Gas Integrated), and Schlumberger Limited (Oil & Gas Equipment & Services).  For these indices, we calculate an index weight for each oil company equal to that company’s median market capitalization divided by the total median market capitalization for the portfolio: a daily index price is the sum of each company’s closing share price times its index weight.  When evaluating the two indices, the top company index is slightly less correlated with the S&P 500 (0.598) compared with the all-company index (0.631) making the top-company index preferable: for our purposes, slightly less systematic risk and, correspondingly, slightly more portfolio risk make for a better model.  Because of this discovery, the top company index’s appreciably reduced computational load, and the high linear correlation between the two indices (0.987), we chose to use the top company index, which we named the Oil Energy Sector (Top) Index.

In conclusion, this analysis provides nuanced answers to our questions.  From the price levels, the relationship between oil company shares and crude oil is very strong with a 0.926 linear correlation.  Remarkably, not only is there no relationship between COVID-19 numbers and the Oil Energy Sector, but also there is no relationship between COVID-19 numbers and any other point of reference in this study.  On top of that, Oil & Gas Energy Sector equities have a 0.738 quadratic correlation with the S&P 500 and a 0.923 quadratic correlation with 10-Year Bond Yields; the economic indicator that remains most insulated from any effects is gold.  Broadly speaking, these metrics, especially crude oil, suffered an immediate but temporary drop in prices at the pandemic’s onset in March 2020.  From the percent changes, there are no significant correlations between any metrics, but, by and large, all the economic benchmarks suffered a substantial increase in volatility at the pandemic’s onset followed by lower but increased volatility except for crude oil prices where normal volatility followed the sudden increase.  Altogether, the uncertainty created by the unexpected appearance of the COVID-19 pandemic caused a precipitous drop in prices and a sudden and substantial increase in volatility followed by lower but increased volatility and gradual price recovery, yet the levels and changes in COVID-19 numbers had no discernable effect on economic price levels.
