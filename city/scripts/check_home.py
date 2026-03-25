"""
Quick script to check that the root URL (/) returns 200 using Django test client.
Run from the workspace root: `cd city; python scripts/check_home.py`
"""
import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'city.settings')
django.setup()

client = Client()
resp = client.get('/')
print('Status code for GET / ->', resp.status_code)
if resp.status_code == 200:
    print('OK: Home page returned 200')
else:
    print('NOT OK: got status', resp.status_code)

# Print a snippet of response content to confirm template loaded
print('Response snippet:', resp.content.decode('utf-8')[:200])
