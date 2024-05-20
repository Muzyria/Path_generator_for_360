import requests
import json

from base.create_signature import SyncwiseAPI


# api = SyncwiseAPI("https://api2.syncwise360.com")


class SyncwiseClient:
    SECRET_KEY = None

    def __init__(self, host):
        self.host = host
        self.signature = SyncwiseAPI()

    # PUBLIC
    def user_account_login(self):
        """
        Login user and get secret key
        """
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_public()}"

        payload = json.dumps({
            "username": "igorperetssuperior",
            "password": "Qwerty01!"
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        print(response.text)
        self.SECRET_KEY = response_data['secretKey']


    # PRIVATE


    def pin_position_update(self, locations):
        """
        Change Pin Position
        """
        action = "PinPositionScheduleUpdate"
        url = f"{self.host}/rest/action/{self.signature.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_course": "KoyhA-zWt6os",
            "id": "KoyhA-zWt6os",
            "id_pinPositionSchedule": 286,
            "startPosition": 1,
            "numberPositions": 1,
            "startDate": "240518",
            "rotationSchedule": 127,
            "rotationDaysNumber": 0,
            "holes": [
                {
                    "holeNumber": 1,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": locations[0],
                            "longitude": locations[1],
                            "active": 1
                        }
                    ]
                },
                {
                    "holeNumber": 2,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.08185,
                            "longitude": 36.229671,
                            "active": 1,
                            "lat": 50.08185,
                            "lng": 36.229671
                        }
                    ]
                },
                {
                    "holeNumber": 3,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.08357,
                            "longitude": 36.232815,
                            "active": 1,
                            "lat": 50.08357,
                            "lng": 36.232815
                        }
                    ]
                },
                {
                    "holeNumber": 4,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.087444,
                            "longitude": 36.241216,
                            "active": 1,
                            "lat": 50.087444,
                            "lng": 36.241216
                        }
                    ]
                },
                {
                    "holeNumber": 5,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.090134,
                            "longitude": 36.240075,
                            "active": 1,
                            "lat": 50.090134,
                            "lng": 36.240075
                        }
                    ]
                },
                {
                    "holeNumber": 6,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.088139,
                            "longitude": 36.233498,
                            "active": 1,
                            "lat": 50.088139,
                            "lng": 36.233498
                        }
                    ]
                },
                {
                    "holeNumber": 7,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.086997,
                            "longitude": 36.233716,
                            "active": 1,
                            "lat": 50.086997,
                            "lng": 36.233716
                        }
                    ]
                },
                {
                    "holeNumber": 8,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.082783,
                            "longitude": 36.229297,
                            "active": 1,
                            "lat": 50.082783,
                            "lng": 36.229297
                        }
                    ]
                },
                {
                    "holeNumber": 9,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.078898,
                            "longitude": 36.229533,
                            "active": 1,
                            "lat": 50.078898,
                            "lng": 36.229533
                        }
                    ]
                },
                {
                    "holeNumber": 10,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.082433,
                            "longitude": 36.231746,
                            "active": 1,
                            "lat": 50.082433,
                            "lng": 36.231746
                        }
                    ]
                },
                {
                    "holeNumber": 11,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.082986,
                            "longitude": 36.232779,
                            "active": 1,
                            "lat": 50.082986,
                            "lng": 36.232779
                        }
                    ]
                },
                {
                    "holeNumber": 12,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.079895,
                            "longitude": 36.232236,
                            "active": 1,
                            "lat": 50.079895,
                            "lng": 36.232236
                        }
                    ]
                },
                {
                    "holeNumber": 13,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.083096,
                            "longitude": 36.233626,
                            "active": 1,
                            "lat": 50.083096,
                            "lng": 36.233626
                        }
                    ]
                },
                {
                    "holeNumber": 14,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.087842,
                            "longitude": 36.238869,
                            "active": 1,
                            "lat": 50.087842,
                            "lng": 36.238869
                        }
                    ]
                },
                {
                    "holeNumber": 15,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.089227,
                            "longitude": 36.239304,
                            "active": 1,
                            "lat": 50.089227,
                            "lng": 36.239304
                        }
                    ]
                },
                {
                    "holeNumber": 16,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.086314,
                            "longitude": 36.234389,
                            "active": 1,
                            "lat": 50.086314,
                            "lng": 36.234389
                        }
                    ]
                },
                {
                    "holeNumber": 17,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.080328,
                            "longitude": 36.235661,
                            "active": 1,
                            "lat": 50.080328,
                            "lng": 36.235661
                        }
                    ]
                },
                {
                    "holeNumber": 18,
                    "positions": [
                        {
                            "position": 1,
                            "latitude": 50.079174,
                            "longitude": 36.232691,
                            "active": 1,
                            "lat": 50.079174,
                            "lng": 36.232691
                        }
                    ]
                }
            ]
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'access-control-request-headers': 'content-type,x-access-token',
            'access-control-request-method': 'POST',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'content-type': 'application/json',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-access-token': 'HGf3LPVdKmzYvZNdJewrh_4PzTc4FcqWZy5-MPwKZfE0ANr9hsEGmMPn4icI'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)


# a = SyncwiseClient("https://api2.syncwise360.com")
# a.user_account_login()