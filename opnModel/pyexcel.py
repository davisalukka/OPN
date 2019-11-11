import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('OPN-portal-a596a986eb98.json', scope)

gc = gspread.authorize(credentials)

#wks = gc.open("HB - SR&ED Monthly Time Project Tracking Report").sheet1
wks = gc.open("SupportersFUNDGP").sheet1


cell_list = wks.col_values(1)
print(cell_list)
