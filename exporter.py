import requests

php_session_id = "" # change this for your login

r = requests.get("https://www.codeabbey.com/index/user_profile", cookies={"PHPSESSID": php_session_id})

print(r.text)
