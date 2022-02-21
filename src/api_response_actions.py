import json
import logging
import os

import allure
import jsonpath_rw
from pydantic import ValidationError


class ResponseActions(object):
    # https://jsonpath.com
    # https://goessner.net/articles/JsonPath/
    # https://jsonpath-rw.readthedocs.io/


    @allure.step
    def status_code_check(self, response, expected_code=200):
        logging.info(f"Check status is code: {expected_code}")
        if response.status_code == expected_code:
            pass
        else:
            logging.error(f"Incorrect status code. \nExpected value: 200,\nActual value: {response.status_code}")
            raise AssertionError(f"Incorrect status code. \nExpected value: 200,\nActual value: {response.status_code}")

    @allure.step
    def check_value_by_path(self, response, json_path, check_value):
        logging.info(f"Check value: *{check_value}* in key: {json_path}")
        try:
            logging.info("Key by path: *{}* has value: {}".format(json_path, check_value))
            json = response.json()
            value = jsonpath_rw.parse(json_path).find(json)[0].value
            assert value == check_value
        except KeyError:
            logging.error("\nResponse body doesn't have *{}* field".format(json_path))
            assert Exception, "\nResponse body doesn't have *{}* field".format(json_path)
        except AssertionError:
            logging.error(f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value}'")
            assert False, f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value}'"


    @allure.step
    def check_value_more_null(self, response, json_path):
        try:
            logging.info("Key {} has value than 0".format(json_path))
            json = response.json()
            value = jsonpath_rw.parse(json_path).find(json)[0].value
            assert value > 0
        except KeyError:
            logging.error("\nResponse body doesn't have *{}* field".format(json_path))
            assert Exception, "\nResponse body doesn't have *{}* field".format(json_path)
        except AssertionError:
            logging.error(f"Value in key {json_path} is null")
            assert False, f"Value in key {json_path} is null"


    @allure.step
    def json_body_check_full(self, response_body, check_json):
        try:
            logging.info(f"Check value in response body")
            json = response_body.json()
            assert json == check_json
        except AssertionError:
            logging.error(f"Jsons aren't qual\nResponse json:\n{json}\nChecking json:\n{check_json}")
            assert False, f"Jsons aren't qual\nResponse json:\n{json}\nChecking json:\n{check_json}"


    @allure.step
    def value_in_body_from_list_by_path(self, response, check_value, json_path):
        logging.info(f"Check value in key: {json_path}")
        try:
            logging.info("Make list from values by path: {}".format(json_path))
            json = response.json()
            value_list = [d for d in jsonpath_rw.parse(json_path).find(json)[0].value]
            assert check_value in value_list
        except KeyError:
            logging.info("\nResponse body doesn't have *{}* field".format(json_path))
            assert Exception, "\nResponse body doesn't have *{}* field".format(json_path)
        except AssertionError:
            logging.error(f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value_list}'")
            assert False, f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value_list}'"

    # @allure.step
    # def validate_json_body(self, response_json, file_name_schema):
    #     path_file = os.path.join((ROOT_DIR + file_name_schema))
    #     with open(path_file) as f:
    #         validate(instance=response_json.json(), schema=json.loads(f.read()))

    @allure.step("Validate schema")
    def schema_validate(self, response, schema):
        try:
            # schema(**response.json())
            schema.parse_obj(response.json())
        except ValidationError as exc:
            logging.error(f"Json validation: {exc}")

