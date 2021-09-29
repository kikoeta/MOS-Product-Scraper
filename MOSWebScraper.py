import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import openpyxl
import xlrd

# Web scraper to get data from GFS and NAM MOS bulletin forecast products and export into Excel file

# --- WEBDRIVER PATH ---
driver = webdriver.Chrome(executable_path='C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/chromedriver.exe')

# --- LINK ---
driver.get('https://www.weather.gov/mdl/mos_getbull?ele=mav,met&sta=kuil') # MAV and MET products for station ____, need to get for other times as well

results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

for element in soup.findAll('div', id='demo'):
    pre = element.find("pre")
    fullData = pre.find_next_siblings("pre", limit=3)
df = pd.DataFrame({'Lastest Data': fullData})
df.to_excel('WxDataHold.xlsx')

GFSRaw = pd.read_excel(r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxDataHold.xlsx', index_col=None, usecols="B", header=1, nrows=0)
GFSRaw = GFSRaw.columns.values[0]
GFSData = GFSRaw.splitlines()
NAMRaw = pd.read_excel(r'C:/Users/Jacob/PycharmProjects/Web Scraper for Met Data/WxDataHold.xlsx', index_col=None, usecols="B", header=3, nrows=0)
NAMRaw = NAMRaw.columns.values[0]
NAMData = NAMRaw.splitlines()
df = pd.DataFrame({'GFS': GFSData, 'NAM': NAMData})
df.to_excel('MOSScraperData.xlsx', "Data")