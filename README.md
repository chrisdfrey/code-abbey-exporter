# code-abbey-exporter

Exports solutions to problems you have solved on [Code Abbey](https://www.codeabbey.com/).

By default puts files in "C:\codeabbey\output" (see the `output_folder` variable).

Requires you to provide the value of your "PHPSESSID" cookie when you are logged into Code Abbey (set via the `php_session_id` variable).

Requires the [requests](https://pypi.org/project/requests/) library to be installed.
