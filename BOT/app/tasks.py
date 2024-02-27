from celery import shared_task
import requests
from .models import *
from celery.schedules import crontab
from datetime import datetime, timedelta
import requests 
from pyrogram import Client
import time



api_id = 24855623
api_hash = '31e3bbaaf5669782c69236f615ab9c9b'




@shared_task()
def send_message_to_group():
    message = Advertising.objects.first().title
    groups = Groups.objects.values_list('groups', flat=True)
    client = Client(name = "my_client", api_id=api_id, api_hash=api_hash,)
    client.start()
    for group_id in groups:
        try:
            client.send_message(str(group_id), message)
        except Exception as e:
            print(e)
    client.stop()








