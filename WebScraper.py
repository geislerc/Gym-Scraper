import requests as rq

req = rq.get("https://geislerc.github.io/")

print(req)

print(req.content)