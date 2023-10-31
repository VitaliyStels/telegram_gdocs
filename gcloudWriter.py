from __future__ import print_function
# import os.path
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json
from dotenv import load_dotenv
load_dotenv()


usersData = []

with open ('data/usersData.json', 'r') as file:
    usersData = json.load(file)




# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
RANGE_NAME = os.getenv('RANGE_NAME')

def writeValues(sheet):
    parsedData = {}
    for user_info in usersData:
        username = user_info["username"]
        user_id = user_info["id"]
        parsedData.add(username, user_id)

    try:
        result = sheet.values().update(
                spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
                valueInputOption="USER_ENTERED", body=parsedData).execute()
        return result
    
    except HttpError as error:
        print(f"Writing error: {error}")
        return error


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('data/token.json'):
        creds = Credentials.from_authorized_user_file('data/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'data/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('data/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, ID:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(f'{row[0]}, {row[1]}')
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
