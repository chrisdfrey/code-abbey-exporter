import http.client

conn = http.client.HTTPConnection("www.codeabbey.com")
conn.request("GET", "/index/user_profile")

r = conn.getresponse().read()
print(r)
