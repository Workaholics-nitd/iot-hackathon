import argparse
from httplib2 import Http
import os.path

from googleapiclient.discovery import build
from oauth2client import file, client, tools
from oauth2client.client import flow_from_clientsecrets, Storage

BASE = os.path.dirname(os.path.abspath(__file__))

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

SPREADSHEET_ID = '1jGZRuO_YLcH7-vkzgmwn-Z7SaIVyXjEYp3UcT9yMnVM'
RANGE_NAME = 'B7:B7'


def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(os.path.join(BASE, 'credentials.json'), SCOPES)
        flags = tools.argparser.parse_args([])
        # flags = parser.parse_args()
        creds = tools.run_flow(flow, store, flags)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    value = result.get('values', [])
    print(value)
    return value[0][0]
