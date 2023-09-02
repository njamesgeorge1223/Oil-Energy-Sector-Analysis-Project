The IPython notebook, PyOilSectorAnalysis.ipynb, requires the following Python scripts with it in the same folder:

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

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the IPython notebook needs the following to execute: yfinance, yahoo_fin, hvplot, panel, geoviews, and geopy.

Here are the requisite Terminal commands for installation of these peripheral modules (in this order):

python3 -m pip install yfinance

python3 -m pip install yahoo_fin

python3 -m pip install hvplot

python3 -m pip install panel

python3 -m pip install geoviews

python3 -m pip install geopy

For the conda environment, these are the requisite Terminal commands:

conda config --add channels conda-forge

conda config --set channel_priority strict


conda install yfinance

conda install yahoo_fin

conda install hvplot

conda install panel

conda install -c conda-forge geoviews

conda install -c conda-forge geopy

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  If the CSV file, AllOilCompanies.csv, is not present in the Resources folder, the program will use APIs to generate the CSV file.  Without the CSV file, execution time is an hour; with it, execution time is approximately 1.5 minutes.

To place the IPython notebook in log mode, debug mode, or image mode set the parameter for the appropriate subroutine in cell #2 to True.  In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in log mode for log information sent to a log file in the same folder.  If the program is in log mode but not debug mode, it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes all the plots to png files and all maps to html files in the Images folder.
