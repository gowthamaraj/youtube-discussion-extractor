import yaml
from googleapiclient.discovery import build

# getting the secret key secretly ;p
key = yaml.safe_load(open('api.yaml'))['key']
api_key = key

print(api_key)