import requests
import json

base_url = 'https://prportal.nidw.gov.bd/partner-service'
access_token = ''
refresh_token = ''
header_json = {'Content-type': 'application/json'}
header_bearer_access = {'Authorization': 'Bearer ' + access_token}
header_bearer_json = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
header_bearer_refresh = {'Authorization': 'Bearer ' + refresh_token}


# Authentication Related user: afis_api_user, pass: S3rAic3Us@r987
# user: test_sub, pass: 123456


def login():
    print("\n\nLogin API")
    login_url = base_url + '/rest/auth/login'
    data = {"username": "test_sub", "password": "123456"}

    response = requests.post(login_url, data=json.dumps(data), headers=header_json)

    if response.status_code == 200:
        data = response.json()
        global access_token, refresh_token, header_bearer_access, header_bearer_refresh, header_bearer_json
        access_token = data['success']['data']['access_token']
        refresh_token = data['success']['data']['refresh_token']
        header_bearer_access = {'Authorization': 'Bearer ' + access_token}
        header_bearer_refresh = {'Authorization': 'Bearer ' + refresh_token}
        header_bearer_json = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


def otp():
    print("\n\nGet OTP API")
    otp_url = base_url + '/rest/send-sms/otp'
    response = requests.post(otp_url, headers=header_bearer_access)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


def refresh():
    print("\n\nRefresh API")
    refresh_url = base_url + '/rest/auth/refresh'
    response = requests.post(refresh_url, headers=header_bearer_refresh)

    if response.status_code == 200:
        data = response.json()
        global access_token
        access_token = data['success']['data']['access_token']
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


def logout():
    print("\n\nLogout API")
    logout_url = base_url + '/rest/auth/logout'
    response = requests.post(logout_url, headers=header_bearer_access)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


# Voter Upload Controller

def num_of_prov_voter():
    print("\n\nNumber of provisional voter API")
    url = base_url + '/rest/prov-voter/total-count'
    data = {"applicationType": "NEW_VOTER"}

    response = requests.post(url, data=json.dumps(data), headers=header_bearer_json)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


def get_voter_list():
    print("\n\nGet Provisional Voter List API")
    url = base_url + '/rest/prov-voter/get-voter-ids'
    data = {"applicationType": "NEW_VOTER", "size": 500}

    response = requests.post(url, data=json.dumps(data), headers=header_bearer_json)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


# Voter Verification Controller

def get_verification_voter_details():
    print("\n\nGet Verification Voter Details API")
    url = base_url + '/rest/voter/details'
    data = {"nid10Digit": "4208576779", "dateOfBirth": "1992-07-23"}

    response = requests.post(url, data=json.dumps(data), headers=header_bearer_json)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


def verify_voter_details():
    print("\n\nVerify Voter Details API")
    url = base_url + '/rest/voter/details/verify'
    data = {"identify": {
                "nid10Digit": "4208576779"
                },
            "verify": {
                "dateOfBirth": "1992-07-23"
                }
            }

    response = requests.post(url, data=json.dumps(data), headers=header_bearer_json)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


# Wildcard Voter Search Controller

def wildcard_search():
    print("\n\nWildcard Voter Search API")
    url = base_url + '/rest/search-voter'
    data = {"gender": "jdhnjvhn", "name": "fd"}

    response = requests.post(url, data=json.dumps(data), headers=header_bearer_json)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


# Identification Afis Controller

def afis_identification():
    print("\n\nAfis Identification API")
    url = base_url + '/rest/afis/identification'
    data = ["RIGHT_THUMB"]

    response = requests.post(url, data=json.dumps(data), headers=header_bearer_json)

    if response.status_code == 200:
        data = response.json()
        json_formatted_str = json.dumps(data, indent=4)
        print(json_formatted_str)
    else:
        print('Request failed with status code:', response.status_code)


if __name__ == "__main__":
    login()
    # otp()
    # refresh()
    # logout()
    # num_of_prov_voter()
    # get_voter_list()
    # get_verification_voter_details()
    # verify_voter_details()
    # wildcard_search()
    afis_identification()
