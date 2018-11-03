import os

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

AUTH_CREDS = os.path.join(os.path.expanduser('~'), ".nxdraftauth")
APP_CREDS = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".client_secrets")
SCOPES = "https://www.googleapis.com/auth/gmail.compose"


def auth():
    """
    authorises the application using saved credentials
    :return: service: authenticated and built gmail API service client
    """
    store = file.Storage(AUTH_CREDS)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(APP_CREDS, SCOPES)
        creds = tools.run_flow(flow, store)
    gmail_service = build('gmail', 'v1', http=creds.authorize(Http()))
    return gmail_service


def get_draft_list(service):
    """
    prints the list of drafts present in user's draft box

    :param service: authenticated and built gmail API service client
    :return: list containing iD and subject of drafts
    """
    draft_list = service.users().drafts().list(userId='me').execute()
    beautiful_draft_list = []

    for draft in draft_list.get("drafts", []):
        # print(draft)
        draft_body = service.users().drafts().get(userId='me', id=draft["id"], format="metadata").execute()
        # print(draft_body)
        beautiful_draft_list.append([
            draft["id"],
            draft_body["message"]["snippet"]
        ])
    return beautiful_draft_list


def make_copies(service, draft_id, n):
    """
    make copies of the draft
    :param service: authenticated gmail service
    :param draft_id: GMail draft ID
    :param n: number of copies
    :return: True if successful, False otherwise
    """
    draft_response = service.users().drafts().get(userId="me", id=draft_id, format="raw").execute()
    raw_response = {'raw': draft_response["message"]["raw"]}
    message = {'message': raw_response}
    try:
        for x in range(int(n)):
            draft = service.users().drafts().create(userId="me", body=message).execute()
            print("draft number "+str(x+1)+" created")
        return True
    except Exception as err:
        print(err)
        return False


if __name__ == "__main__":
    gm_serv = auth()
    print("Draft ID\t\tDraft Snippet")
    draft_list = get_draft_list(gm_serv)
    for beautified_draft in draft_list:
        print(beautified_draft[0]+"\t\t"+beautified_draft[1])
    draft_id = input("Enter the draft ID to be NxEd: ")
    while draft_id not in [x[0] for x in draft_list]:
        print("Wrong Draft ID!!!")
        draft_id = input("Enter the draft ID to be NxEd: ")
    n = input("Enter the number of copies to be made: ")
    if make_copies(gm_serv, draft_id, n):
        print("Done!")
    else:
        print("Failed")
