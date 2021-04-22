# Ganya kuch bhi karta hai
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from .models import Needy, Res_type, City, State, Resource
# from .forms import HelpForm, NeedForm
# import requests
# #from .forms import RequestForm
# # Create your views here.
# from django.utils import timezone

# # add source -- HelpForm -- helpingH
# # add need -- NeedForm -- request
# scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)

# client = gspread.authorize(creds)
# sheet = client.open("resources").sheet1

# col = sheet.col_values(2)
