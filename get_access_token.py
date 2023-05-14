import requests
import config

REDDIT_USERNAME = config.REDDIT_USERNAME
REDDIT_PASSWORD = config.REDDIT_PASSWORD
APP_ID = config.APP_ID
APP_SECRET = config.APP_SECRET
APP_NAME = config.APP_NAME

base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': REDDIT_USERNAME, 'password': REDDIT_PASSWORD}
auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': f'{APP_NAME} by {REDDIT_USERNAME}'}, auth=auth)
d = r.json()

print(d)