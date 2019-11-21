# import argparse
# from httplib2 import Http
import os.path

import requests
# from googleapiclient.discovery import build
# from oauth2client import file, client, tools
# from oauth2client.client import flow_from_clientsecrets, Storage

# BASE = os.path.dirname(os.path.abspath(__file__))

# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# SPREADSHEET_ID = '1thzF-svRUlIslOnCHdDcEoJ1e8a0S38sfqSPIGbSZYI'
# RANGE_NAME = 'B1:C'


# def main():
#     store = file.Storage('token.json')
#     creds = store.get()
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets(
#             os.path.join(BASE, 'credentials.json'), SCOPES
#         )
#         flags = tools.argparser.parse_args([])
#         # flags = parser.parse_args()
#         creds = tools.run_flow(flow, store, flags)
#     service = build('sheets', 'v4', http=creds.authorize(Http()))

#     # Call the Sheets API
#     result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
#                                                 range=RANGE_NAME).execute()
#     value = result.get('values', [])
#     print(value)
#     return value[-1][0]


from .models import Dustbin

def main():
    IP = "http://0.0.0.0:5/"
    r = requests.get(IP)
    res = r.json()
    d = Dustbin(dustbin_id='0', percentage=int(res))
    d.save()
    return res
