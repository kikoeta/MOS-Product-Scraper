import pandas as pd

# --- Comment out line below if testing, else will recheck model ---
import WxWebScraperV3

# ---- GFS ----
# Header with station, model, and run
HEADER = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="B", header=1, nrows=0)
HEADER = HEADER.columns.values[0]
print(HEADER)

# Date
DATE = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="B", header=2, nrows=0)
DATE = DATE.columns.values[0]
print(DATE)

# Hour (UTC)
HR = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="B", header=3, nrows=0)
HR = HR.columns.values[0]
print(HR)

# Max/Min Temp
NX = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="B", header=4, nrows=0)
NX = NX.columns.values[0]
print(NX)

# Hourly Temp
TMP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="B", header=5, nrows=0)
TMP = TMP.columns.values[0]
print(TMP)

# Hourly Windspeed
WSP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="B", header=9, nrows=0)
WSP = WSP.columns.values[0]
print(WSP)

print("\n")

# ---- NAM ----
# Header with station, model, and run
HEADER = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="C", header=1, nrows=0)
HEADER = HEADER.columns.values[0]
print(HEADER)

# Date
DATE = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="C", header=2, nrows=0)
DATE = DATE.columns.values[0]
print(DATE)

# Hour (UTC)
HR = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="C", header=3, nrows=0)
HR = HR.columns.values[0]
print(HR)

# Max/Min Temp
NX = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="C", header=4, nrows=0)
NX = NX.columns.values[0]
print(NX)

# Hourly Temp
TMP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="C", header=5, nrows=0)
TMP = TMP.columns.values[0]
print(TMP)

# Hourly Windspeed
WSP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxWeb MOS Scraper.xlsx', index_col=None, usecols="C", header=9, nrows=0)
WSP = WSP.columns.values[0]
print(WSP)
#print("\n")
#TMP_Split = TMP.split() # Splits the unregulated text into readable bits
#TMP_Split.remove("TMP") # Removes letters from data
#NX_Split = NX.split()
#NX_Split.remove("X/N")
#if min(NX_Split) <= min(TMP_Split):
#    print("Min temp is: ", min(NX_Split))
#elif min(TMP_Split) <= min(NX_Split):
#    print("Min temp is: ", min(TMP_Split))
##if max(NX_Split) >= max(TMP_Split):
#    print("Max temp is: ", max(NX_Split))
#elif max(TMP_Split) >= max(NX_Split):
#    print("Max temp is: ", max(TMP_Split))
#
#print("NX min is:", min(NX_Split))
#print("NX max is:", max(NX_Split))
#print("TMP min is:", min(TMP_Split))
#print("TMP max is:", max(TMP_Split))