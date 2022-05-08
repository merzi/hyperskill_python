import requests


def check_success(url):
    r = requests.get(url)
    succeed_status_code = 200
    return "Success" if r.status_code == succeed_status_code else "Fail"
