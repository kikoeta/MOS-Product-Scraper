# MOS-Product-Scraper
A basic python web scraper to get and filter NWS MOS product data and display it in the terminal for the purposes of WxChallenge

Basically, the goal with this project was to simplify the very confusing and lengthy to process NWS MOS product text bulletins. I wanted to be able to get the lines I needed out of the table, which I would at some point, like to sort over a range.

You will need pandas, BeautifulSoup (bs4), selenium, openpyxl, and xlrd to make this work.
Download the requisite chrome web driver (for selenium) here: https://sites.google.com/chromium.org/driver/downloads

# Instructions
Check what version of Chrome you have installed on your computer, then download the webdriver from the above link and place it into the folder you will be using to house the files. After this, open the web scraper file and change things. You must alter all paths until I figure out how to make that happen, anything that is a path on my computer needs to be edited to match yours. The other things are the path to your chrome driver file, and the link to include the one (1) station you want to check. After this, run the data parser file and wait for it to output your data into the terminal.
