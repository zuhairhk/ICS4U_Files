import pygsheets

gc = pygsheets.authorize() # This will create a link to authorize
# sh = gc.open('WARZONE Quick Stat Sheets') # open spreadsheet
# sh = gc.open_by_key('spreadsheet_key')
sh.open_by_link('https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQkSQpSMq7ARPy2jTjn4amWPe_mX39NVZRe9v3LHZC11wGEOHHnETP18pfSITU3thsGvFH6LRzFKEit/pubhtml')