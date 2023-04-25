import requests

res = requests.get("https://forms.googleapis.com/v1/forms/1Nfuk6r3GJliXVcJZqNxDPLaBqtzthRueDj8A6SHpYc8")

print(res)

print(res.text)

print(res.json())

print(res.status_code)