import requests
import os


class RegionAll():

    @staticmethod 
    def get_region_all():
        """ Get configuration map """
        url = "https://restcountries-v1.p.rapidapi.com/all"
        data = []
        headers = {
            'x-rapidapi-host': 'restcountries-v1.p.rapidapi.com',
            'x-rapidapi-key': os.environ['KEY_RAPID']
        }
        response = requests.request("GET", url, headers=headers)
        return response