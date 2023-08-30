The Jupyter Notebook, PyOilSectorAnalysis.ipynb, requires the following Python scripts 
with it in the same folder:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PyOilSectorAnalysisAPIFunctions.py

PyOilSectorAnalysisConfig.py

PyOilSectorAnalysisConstants.py

PyOilSectorAnalysisFunctions.py

PySubroutines.py

If the computer has Anaconda, JUpyter Notebook, and a recent version of Python, the 
Jupyter notebook already has the following dependencies installed: datetime, io, json, 
matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook needs the following to execute: 
yfinance, yahoo_fin, hvplot, panel.

Here are the requisite Terminal commands for installation of these peripheral modules:

python3 -m pip install yfinance

python3 -m pip install yahoo_fin

python3 -m pip install hvplot

python3 -m pip install panel

For the conda environment, these are the requisite Terminal commands:

conda install yfinance

conda install yahoo_fin

conda install hvplot

conda install panel

If the folders, Resources, Logs, and Images are not present, the Jupyter Notebook will 
create them.  If the CSV file, AllOilCompanies.csv, is not present in the Resources folder, 
the program will use APIs to generate the CSV file.  Without the CSV file, execution time 
is between 45 minutes to an hour; with it, execution time is approximately 1.5 minutes.

To place the Jupyter Notebook in log mode, debug mode,or image mode set the parameter for
the appropriate subroutine in cell #2 to True.  In debug mode, the program displays the 
debug information and writes it to a debug file in the Logs folder; the same is true in 
log mode for log information sent to a log file in the same folder.  If the program is in 
log mode but not debug mode, it displays no debug information, but writes that information 
to the log file. If the program is in image mode, it writes all the plots to png files in 
the Images folder.

WARNING: When an inexplicable Yahoo Finance API warning concerning delisted tickers appeared 
during the retrieval of oil tickers: xxx: No price data found, symbol may be delisted 
(1d 2020-01-03 -> 2022-10-16), I resolved the issue by upgrading the python version to 3.11.5, 
uninstalling the following modules: phantomJS, selenium, and holoviews, reinstalling yfinance, 
yahoo_fin, hvplot, and panel (in that order), and adding code for empty objects.  
