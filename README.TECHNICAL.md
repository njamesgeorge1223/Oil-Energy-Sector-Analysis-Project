The Jupyter Notebook, PyOilSectorAnalysis.ipynb, requires the following Python scripts with it in the same folder:

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

If the computer has Anaconda and a recent version of Python, the Jupyter notebook already has the following dependencies 
installed: datetime, io, json, pandas, pathlib, os, pandas, requests.

In addition to these modules, the Jupyter Notebook will require the following: hvplot, numpy, matplotlib, requests_html,
yahoo_fin, yfinance.  

Here are the requisite Terminal commands:

pip install hvplot

pip install numpy

pip install matplotlib

pip install requests_html

pip install yahoo_fin

pip install yfinance

If the folders, Resources and Logs, are not present, the Jupyter Notebook will create them.  If the CSV file, 
AllOilCompanies.csv, is not present in the Resources folder, the program will use a variety of APIs to generate 
the CSV file.  Without the CSV file, execution time is between 45 minutes to an hour; with it, execution time 
is approximately 1.5 minutes.

To place the Jupyter Notebook in debug mode, set the variable in cell #2, log_constant.DEBUG_FLAG, equal to zero.  
In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; otherwise,  
the program only writes the information to the log file in the Logs folder.
