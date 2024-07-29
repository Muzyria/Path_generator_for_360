import requests
import json
from base.create_signature import SyncwiseAPI


class GeofenceADVEdit:
    SECRET_KEY = None

    def __init__(self, secret_key):
        self.SECRET_KEY = secret_key
        self.host = "https://api2.syncwise360.com"
        self.action = "CourseGeofenceUpdate"
        self.signature = SyncwiseAPI()

    def get_course_geofence_list(self):
        action = "CourseGeofenceList"
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = json.dumps({
            "active": 1,
            "id_company": 4442
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-access-token': 'schFugByhm6v0V_rT2KgUPotgfAtonQF2bSruFM_Ys0dcZDOXJY7-KVd-lIt'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # print(response.text)
        data = response.json()["resultList"]
        # print(data)
        return data

    def change_name(self, id_geofence, name):
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(self.action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "status": 1,
            "visible": 1,
            "id_company": 4442,
            "id_geofenceType": 17,
            "active": 1,
            "name": name,
            "disabilityBypass": 0,
            "marshallBypass": 0
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-access-token': 'schFugByhm6v0V_rT2KgUPotgfAtonQF2bSruFM_Ys0dcZDOXJY7-KVd-lIt'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def change_on_off(self, id_geofence, status):
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(self.action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "status": status
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-access-token': 'schFugByhm6v0V_rT2KgUPotgfAtonQF2bSruFM_Ys0dcZDOXJY7-KVd-lIt'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def change_visibility(self, id_geofence, visible):
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(self.action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "visible": visible
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-access-token': 'schFugByhm6v0V_rT2KgUPotgfAtonQF2bSruFM_Ys0dcZDOXJY7-KVd-lIt'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def change_coordinate(self, id_geofence, coordinate: list):
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(self.action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "status": 1,
            "visible": 1,
            "id_company": 4442,
            "id_geofenceType": 17,
            "points": coordinate,
            "active": 1,
            "name": "6",
            "disabilityBypass": 0,
            "marshallBypass": 0
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-access-token': 'schFugByhm6v0V_rT2KgUPotgfAtonQF2bSruFM_Ys0dcZDOXJY7-KVd-lIt'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def change_image(self, id_geofence, file_name):
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(self.action, self.SECRET_KEY)}"

        payload = {'request': json.dumps({
            "id_geofence": id_geofence,
            "status": 1,
            "visible": 1,
            "id_company": 4442,
            "id_geofenceType": 17,
            "active": 1,
            "name": "7"
        })}

        files = [('file', ('file', open(f'tests/images/{file_name}', 'rb'), 'application/octet-stream'))]
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)