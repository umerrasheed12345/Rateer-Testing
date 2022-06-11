import json
import requests


def send_req_api(url, feature, scenario, given, when):
    print(
        "Feature: {}\n\
        Scenario: {}\n\
        Given: {}\n\
        When: {}\n".format(feature,scenario + ":" + url,given,when), end="")
    try:
        response = requests.get(url)
        print("\
        Then: {}\n\
        Response Status Code: {}\n\
        Response Data:\n\t{}\n".format(
        "Test Passed.",
        str(response.status_code),
        str(response.json())
        ))
    except Exception as e:
        print("\
        Then: {}\n\
        Response Status Code: {}\n".format(
        "Test Failed.",
        str(response.status_code),
        ))


BASE_URL = "https://rateer.pythonanywhere.com/"
API_ENDPOINT = "isadmin"

url = BASE_URL + API_ENDPOINT + "?" + "username=Clark_Kent"
send_req_api(url, "IsAdmin", "Testing API endpoint url", "valid username", "Sending requst to url")

url = BASE_URL + API_ENDPOINT + "?" + "username=asasdasddas"
send_req_api(url, "IsAdmin", "Testing API endpoint url", "invalid username", "Sending requst to url")

url = BASE_URL + API_ENDPOINT + "?" + "username="
send_req_api(url, "IsAdmin", "Testing API endpoint url", "empty username", "Sending requst to url")