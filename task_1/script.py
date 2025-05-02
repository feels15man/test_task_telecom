import requests
import logging
from sys import stdout

url = "https://httpstat.us/"

def init_log():
    handler = logging.StreamHandler(stdout)
    handler.setFormatter(logging.Formatter("[%(levelname)s]: %(message)s"))
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    

def main():
    for i in range(5):
        req = url + 'random/200-208,300-308,400-408,500-508?sleep=100'
        res = requests.get(req, allow_redirects=False)
        try:
            res.raise_for_status()
        # Можно также сделать это с помощью условия 
        # if (res.status_code >= 400):
        #     raise Exception("4xx or 5xx response code")
        except requests.RequestException as ex:
            logging.error(f"Bad response code {res.status_code};\tException: {ex}")
        else:
            logging.info(f"status code: {res.status_code};response body: {res.text}")

if __name__ == '__main__':
    init_log()
    main()