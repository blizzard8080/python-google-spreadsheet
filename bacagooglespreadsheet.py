# Python code Baca Google Spreadsheets
# By b4LtH4Z4R_ARMv8
# --------------------------------------------
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def veler():
    alamatURL = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    kredensial = ServiceAccountCredentials.from_json_keyfile_name('tms-telpro-e6e5cd3fe60d.json', alamatURL)
    client = gspread.authorize(kredensial)

    # Membaca Sheet1 Google Spreadsheets untuk file MASTERDATA:
    sheet = client.open('MASTERDATA').sheet1
    masterdata = sheet.get_all_records()

    # Konvert menjadi DataFrame
    df = pd.DataFrame(masterdata)

    # Seleksi columns label
    print(df[['NOPOL', 'NAMA KONTRAK', 'NOMOR RANGKA', 'NOMORMESIN', 'POOL AREA']])


veler()
