from __future__ import print_function
import argparse
import logging
import json
import sys

from pyharmony import auth
from pyharmony import client as harmony_client

import code

def login_to_logitech(email, password, harmony_ip='HarmonyHub', harmony_port=5222):
    """Logs in to the Logitech service.

    Args:
      email: Email address to login to Logitech
      password: Password to login to Logitech
      harmony_ip: IP address of Harmony Hub
      harmony_port: port of Harmony Hub (default: 5222)

    Returns:
      Session token that can be used to log in to the Harmony device.
    """
    token = auth.login(email, password)
    if not token:
        sys.exit('Could not get token from Logitech server.')

    session_token = auth.swap_auth_token(
        harmony_ip, harmony_port, token)
    if not session_token:
        sys.exit('Could not swap login token for session token.')

    return session_token

def pprint(obj):
    """Pretty JSON dump of an object."""
    print(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))

def get_client(email, password, harmony_ip='HarmonyHub', harmony_port=5222):
    """Gets a client object used to interact with Logitech

    Args:
      email: Email address to login to Logitech
      password: Password to login to Logitech
      harmony_ip: IP address of Harmony Hub
      harmony_port: port of Harmony Hub (default: 5222)

    Returns:
      Client object used to control the Harmony device.
    """

    token = login_to_logitech(email, password, harmony_ip, harmony_port)
    client = harmony_client.create_and_connect_client(
        harmony_ip, harmony_port, token)
    return client

def show_config(args):
    """Connects to the Harmony and prints its configuration."""
    client = get_client(args)
    pprint(client.get_config())
    client.disconnect(send_close=True)
    return 0

def show_current_activity(args):
    """Connects to the Harmony and prints the current activity block
    from the config."""
    client = get_client(args)
    config = client.get_config()
    current_activity_id = client.get_current_activity()

    activity = [x for x in config['activity'] if int(x['id']) == current_activity_id][0]

    pprint(activity)

    client.disconnect(send_close=True)
    return 0

def power_off(args):
    """Connects to the Harmony and syncs it.
    """
    client = get_client(args)
    client.power_off()
    client.disconnect(send_close=True)
    return 0

def sync(args):
    """Connects to the Harmony and syncs it.
    """
    client = get_client(args)
    client.sync()
    client.disconnect(send_close=True)
    return 0

def start_activity(args):
    """Connects to the Harmony and starts an activity"""
    client = get_client(args)
    config = client.get_config()
    activities = config['activity']
    labels_and_ids = dict([(a['label'], a['id']) for a in activities])
    matching = [label for label in list(labels_and_ids.keys())
                if args.activity.lower() in label.lower()]
    if len(matching) == 1:
        activity = matching[0]
        print("Found activity named %s (id %s)" % (activity,
                                                   labels_and_ids[activity]))
        client.start_activity(labels_and_ids[activity])
    else:
        print("found too many! %s" % (" ".join(matching)))
    client.disconnect(send_close=True)
    return 0

def send_command(args):
    """Connects to the Harmony and send a simple command."""
    client = get_client(args)

    client.send_command(args.device_id, args.command)

    client.disconnect(send_close=True)
    return 0
