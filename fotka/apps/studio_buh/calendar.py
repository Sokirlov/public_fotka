from __future__ import print_function
import datetime
from datetime import timedelta
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from .models import Administrators


def creat_event_call(new_order):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    cal_id = None
    ciklorama = '' #cal_id_1
    objects = ''  #cal_id_2
    if str(new_order['service']) == 'Аренда Циклорамы':
        cal_id = ciklorama
    elif str(new_order['service']) == 'Аренда Темного зала':
        cal_id = objects
    else:
        cal_id = '' #cal_id_3

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    if new_order['who_admin']:
        admin_name = str(new_order['who_admin'])
        admin_object = Administrators.objects.get(name=admin_name)
        admin_mail = admin_object.email
        attendees = {'email': admin_mail}
    else:
        admin_name = ''
        admin_mail = ''
        attendees = None
    start_order = str(new_order['date_ordering'].strftime("%Y-%m-%dT%H:%M:%S+03:00"))
    raw_finish_order = new_order['date_ordering']+timedelta(hours=new_order['order'])
    finish_order = str(raw_finish_order.strftime("%Y-%m-%dT%H:%M:%S+03:00"))

    event_info = {
        'start': {
            'dateTime': start_order,
        },
        'end': {
            'dateTime': finish_order,
        },
        'attendees': [
           attendees,
        ],
        'title': 'Аренда',
        "summary": "Аренда  " + str(new_order['tel']),  # Title of the event.
        'description': "Клиент: "+str(new_order['tel']) +' грн\nПредоплата: '+ str(new_order['prepay'])+'\nАдминистратор: '+admin_name,
    }
    event_add = service.events().insert(calendarId=cal_id, body=event_info).execute()
    htmlLink = 'https://www.googleapis.com/calendar/v3/calendars/' + cal_id + '/events'
    print('Event created: %s' % (event_add.get('htmlLink')))