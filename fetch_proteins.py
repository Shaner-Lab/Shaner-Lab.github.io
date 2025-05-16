import urllib.request
import json

# Fetch proteins authored by Shaner from the FPbase API using urllib
api_url = 'https://www.fpbase.org/api/proteins/?primary_reference__author__family__icontains=Shaner&format=json&page_size=200'
with urllib.request.urlopen(api_url) as response:
    data = json.load(response)

# Write results to local JSON file for static serving
with open('our-proteins/proteins.json', 'w') as f:
    json.dump(data, f, indent=2)
print(f"Wrote {len(data)} protein entries to our-proteins/proteins.json") 