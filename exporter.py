import requests
import re
import os
import html

php_session_id = "" # change this for your login
cookies = {"PHPSESSID": php_session_id}

solution_re = re.compile(r"\"/index/task_solution?([^\"]+)\"")
code_re = re.compile(r"<code[^>]+>(.*?)</code>", re.DOTALL)
task_re = re.compile("task=([^&]+)")

r = requests.get("https://www.codeabbey.com/index/user_profile", cookies=cookies)
solutions = solution_re.findall(r.text)

output_folder = "C:\\codeabbey\\output\\"

if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

for solution in solutions:
    url = "https://www.codeabbey.com/index/task_solution" + solution
    r = requests.get(url, cookies=cookies)

    code_match = code_re.search(r.text)
    if code_match is None:
        continue

    code = code_match.group(1)
    code = html.unescape(code)
    code = code.replace("\r", "")

    task = task_re.search(solution).group(1)

    output_path = os.path.join(output_folder, task + ".py")
    f = open(output_path,'w')
    f.write(code)
    f.close()
