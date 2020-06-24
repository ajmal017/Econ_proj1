import pandas_ta as ta  # !pip install pandas_ta
import numpy as np  # array,matrix,random numbers
import pandas as pd  # for DataFrames, dataframe for time series data
# import statsmodels  # timeseries analysis , regression models
import math
import sys
# import backtrader as bt
import yfinance as yf  # !pip install yfinance
# import seaborn as sns
# import pyfolio as pf
from io import StringIO  # before pandas_datareader
from pandas_datareader import data as pdr
from pandas_datareader import data, wb
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from matplotlib import rc
from matplotlib import interactive
import datetime as dt
from datetime import timedelta, datetime, date, time
import time
import pathlib
from pathlib import Path  # to read/write files
import os
from os import path
import ast
import re
import requests  # scraping the web
from urllib.request import urlopen
# from bs4 import BeautifulSoup
#import scipy
# from sklearn.preprocessing import StandardScaler
#import scipy.stats
#from scipy.stats.mstats import gmean
#from scipy.stats import norm
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display
# import chart_studio.plotly as py
# import plotly.tools as tls
# from sqlalchemy import create_engine
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
import fredapi
from fredapi import Fred

InteractiveShell.ast_node_interactivity = "all"
register_matplotlib_converters()
pd.core.common.is_list_like = pd.api.types.is_list_like
