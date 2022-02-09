# Covid_HelpDesk
A collection of COVID-19 relief resources and support for user-input resources and requests. After 6 months of support and help, with improvement in the pandemic situation, website is currently inactive.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ cd Covid_HelpDesk/
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```

If you face problems, change Debug = True in /Covid_HelpDesk/Covid_HelpDesk/settings.py

