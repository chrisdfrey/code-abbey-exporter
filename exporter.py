import requests
import re

php_session_id = "" # change this for your login
cookies = {"PHPSESSID": php_session_id}

r = requests.get("https://www.codeabbey.com/index/user_profile", cookies=cookies)

solution_re = re.compile(r"\"/index/task_solution?([^\"]+)\"")
solutions = solution_re.findall(r.text)

code_re = re.compile(r"<code[^>]+>(.*?)</code>", re.DOTALL)

for solution in solutions:
    url = "https://www.codeabbey.com/index/task_solution" + solution
    r = requests.get(url, cookies=cookies)

    code = code_re.search(r.text).group(1)
    print(code)
