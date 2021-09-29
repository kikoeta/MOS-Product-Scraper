import pandas as pd

# --- Comment out line below if testing, else will recheck model ---
import MOSWebScraper

# ---- GFS ----
# Header with station, model, and run
HEADER = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="B", header=1, nrows=0)
HEADER = HEADER.columns.values[0]
print(HEADER)

# Date
DATE = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="B", header=2, nrows=0)
DATE = DATE.columns.values[0]
print(DATE)

# Hour (UTC)
HR = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="B", header=3, nrows=0)
HR = HR.columns.values[0]
print(HR)

# Max/Min Temp
NX = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="B", header=4, nrows=0)
NX = NX.columns.values[0]
print(NX)

# Hourly Temp
TMP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="B", header=5, nrows=0)
TMP = TMP.columns.values[0]
print(TMP)

# Hourly Windspeed
WSP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="B", header=9, nrows=0)
WSP = WSP.columns.values[0]
print(WSP)

print("\n")

# ---- NAM ----
# Header with station, model, and run
HEADER = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="C", header=1, nrows=0)
HEADER = HEADER.columns.values[0]
print(HEADER)

# Date
DATE = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="C", header=2, nrows=0)
DATE = DATE.columns.values[0]
print(DATE)

# Hour (UTC)
HR = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="C", header=3, nrows=0)
HR = HR.columns.values[0]
print(HR)

# Max/Min Temp
NX = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="C", header=4, nrows=0)
NX = NX.columns.values[0]
print(NX)

# Hourly Temp
TMP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="C", header=5, nrows=0)
TMP = TMP.columns.values[0]
print(TMP)

# Hourly Windspeed
WSP = pd.read_excel (r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/MOSScraperData.xlsx', index_col=None, usecols="C", header=9, nrows=0)
WSP = WSP.columns.values[0]
print(WSP)