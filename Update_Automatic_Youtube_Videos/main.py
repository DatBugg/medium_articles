import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow



SCOPES = ["https://www.googleapis.com/auth/youtube"]





def generateToken():

    sdir = os.path.dirname(__file__)
    # We load the credentials
    credentials = os.path.join("credentials/desktopYT.json")

    # We generate the token
    flow = InstalledAppFlow.from_client_secrets_file(credentials, SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(os.path.join(sdir, './credentials/tokenYT.json'), 'w') as token:
        token.write(creds.to_json())

    return "Token generated"






def updateVideo():
    
    # With the google function "Credentials" we import the Json downloaded from GCP to authenticate ourselves
    creds = Credentials.from_authorized_user_file('./tokenYT.json', SCOPES)
    
   
    youtube = build("youtube", "v3", credentials=creds)

    # We introduce the parameters to modify in the video
    update = youtube.videos().update(
        part="snippet",
        body={
          "id": "ID_VIDEO",
          "snippet": {
            "description": f'Video Description',
            "title": f'Title Video',
            "categoryId": "24"
          }
        }
    )

    # We make the API call
    update.execute()


    return "Video updated"