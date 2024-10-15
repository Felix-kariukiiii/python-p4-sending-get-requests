import requests
import json

# urlText = "https://learn-co-curriculum.github.io/json-site-example/"
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

# responseText= requests.get(urlText)
response = requests.get(url)

# print(responseText.text)
json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))
print(json.dumps(json_content, indent=4, sort_keys=True))