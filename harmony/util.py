import sys

from harmony import auth
from harmony import client as harmony_client

def get_client(harmony_ip, harmony_port, email, password):
    token = auth.login(email, password)
    if not token:
        sys.exit('Could not get token from Logitech server.')

    session_token = auth.swap_auth_token(
        harmony_ip, harmony_port, token)
    if not session_token:
        sys.exit('Could not swap login token for session token.')
    client = harmony_client.create_and_connect_client(
        harmony_ip, harmony_port, token)
    return client
