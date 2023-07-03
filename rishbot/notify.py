import requests
import os
import json 

# send slack message


def notify_slack(text=f':white_check_mark: All finished !!!'):
    requests.post(os.getenv('SLACK_URL'), data=json.dumps({'text': text}))