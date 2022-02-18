import json
from ast import literal_eval

import requests
import logging

from datetime import datetime
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from env_data import env_run


# logger_custom = logging.getLogger(__name__)
# logger_custom.propagate = False
# logger_custom.setLevel(logging.DEBUG)
# now = datetime.now()
# # if not logger_custom.handlers:
# #     log_path = os.path.join('logs')
# #     os.makedirs(log_path, exist_ok=True)
# #     f_handler = logging.FileHandler(os.path.join(log_path, f"{str(now.strftime('%d-%b-%Y'))}_logsfile.log"))
# #     f_handler.setLevel(logging.DEBUG)
# #     logger_custom.addHandler(f_handler)
# s_handler = logging.StreamHandler()
# s_format = logging.Formatter('[%(levelname)s] - %(message)s')
# s_handler.setFormatter(s_format)
# logger_custom.addHandler(s_handler)

main_url_api = env_run()

# https://jsonplaceholder.typicode.com/

def logging_request(url, response, data=None, request_json=None):
    request_body = ""
    response_body = ""
    if data:
        request_body = json.dumps(data.dict(), indent=4)
    elif request_json:
        request_body = json.dumps(request_json, indent=4)
    elif data == None and request_json == {}:
        pass
    if len(response.json())>0:
        response_body = json.dumps(response.json(), indent=4)
    logging.info(f"Request: "
         f"\n url= {url} "
         f"\n header= {response.request.headers} "
         f"\n body=\n{request_body}")
    logging.info(f"Response: \n status={response.status_code} "
         f"\n url={response.url}"
         f"\n header={response.headers} "
         f"\n body=\n{response_body}")


def auth_to_service(username, password):
    client_id="autotests_client"
    client_secret="test_temp_secret"
    logging.info(f"Get cookies user: *{username}*")
    oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
    token = oauth.fetch_token(token_url='https://accounts.ghost-network.boberneprotiv.com/connect/token', username=username,
                              password=password, client_id=client_id, client_secret=client_secret)
    return (token['access_token'])


def get_method(url, user_cookies, headers=None, params=None, session=None):
    url_request = main_url_api+url
    logging.info(f'Make a GET request to {url_request}')
    if headers is None:
        headers = {}
    headers['Authorization'] = f"Bearer {user_cookies}"
    if session is None:
        response = requests.get(url=url_request, headers=headers, params=params)
    else:
        response = session.get(url=url_request, headers=headers, params=params)
    logging_request(url_request, response)
    return response


def post_method(url, user_cookies=None, headers=None, data=None, session=None):
    url_request = main_url_api + url
    logging.info(f'Make a POST request to {url_request}')
    if headers is None:
        headers = {}
    if user_cookies != None:
        headers['Authorization'] = f"Bearer {user_cookies}"
    if session is None:
        response = requests.post(url=url_request, headers=headers, data=data.dict())
    else:
        response = session.post(url=url_request, headers=headers, data=data.dict())
    logging_request(url_request, response, data=data)
    return response


def put_method(url, user_cookies, headers=None, data=None, verify_ssl_cert=True, json=None):
    url_request = main_url_api + url
    logging.info(f'Make a PUT request to {url_request}')
    if headers is None:
        headers = {}
    headers['Authorization'] = f"Bearer {user_cookies}"
    response = requests.get(url=url_request, headers=headers, verify=verify_ssl_cert)
    logging_request(url_request, response, data=data)
    return response


def delete_method(url, user_cookies, headers=None, data=None, verify_ssl_cert=True):
    url_request = main_url_api + url
    logging.info(f'Make a DELETE request to {url_request}')
    if headers is None:
        headers = {}
    headers['Authorization'] = f"Bearer {user_cookies}"
    logging.info('Make a DELETE request to {}'.format(url))
    response = requests.get(url=url_request, headers=headers, verify=verify_ssl_cert)
    logging_request(url_request, response, data=data)
    return response
