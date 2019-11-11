import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('OPN-portal-a596a986eb98.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("SupportersFUNDGP").sheet1

cell_list = wks.range('A1:AP1')


demarc = 42

companyName = "testcompanyalpha"

worksheet2 = gc.create(companyName)

worksheet2.share("davis.ja@hardbootinc.com", perm_type="user", role="writer")

wks2 = gc.open(companyName).sheet1

cell_list2 = wks2.range('A1:AP1')


for i in range(len(cell_list)):
    cell_list2[i].value = cell_list[i].value

wks2.update_cells(cell_list2)









