#!/usr/bin/env python3
import datetime
import notify

def backup_action(action):
    now = datetime.datetime.now()
    message = now.isoformat()

    notify.publish_message(action, message)
