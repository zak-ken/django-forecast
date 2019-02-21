# from forecast.forms import insertion_form
from forecast.models import save_weather_record
from django.core.management.base import BaseCommand
import requests
requests.packages.urllib3.disable_warnings()
import json
import ast



class Command(BaseCommand):
    args = ''
    help = 'Get data from the API and store it within the database'

    def handle(self, *args, **options):

        cityId = "77107"
        ashx_url = "http://weather.news24.com/ajaxpro/Weather.Code.Ajax,Weather.ashx"
        request_post = requests.post(ashx_url,
                                     headers={'X-AjaxPro-Method': 'GetForecast15DayExpanded',
                                              'Referer': 'http://weather.news24.com/sa/cape-town',
                                              'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/72.0.3626.96 Chrome/72.0.3626.96 Safari/537.36',
                                              'Origin': 'http://weather.news24.com',
                                              'Host': 'weather.news24.com',
                                              'Cookie': '__cfduid=de84c5b478da898a19eeab789a64f9c841547019841',
                                              'Content-Type': 'text/plain; charset=UTF-8',
                                              'Content-Length': '18',
                                              'Connection': 'keep-alive',
                                              'Accept-Language': 'en-US,en;q=0.9',
                                              'Accept-Encoding': 'gzip, deflate',
                                              'Accept': '*/*'
                                              },
                                     data=json.dumps({"cityId": cityId}))

        all_weather_records = request_post.content
        all_weather_records = str(all_weather_records).replace("b'", '').replace('false', 'False').replace('null', 'None').replace("\'", '')#.replace("new Date(Date.UTC(", "'").replace("))","'").strip(";/*'")
        all_weather_records = ast.literal_eval(all_weather_records)
        all_weather_records = all_weather_records.get('value', {})
        all_weather_records = all_weather_records.get('Forecasts', {})
        for weather_day in all_weather_records:
            data = {'weather_Date': weather_day['FormattedDate'], 'min_temp': int(weather_day['LowTemp']), 'max_temp': int(weather_day['HighTemp']),
                    'wind': int(weather_day['WindSpeed']), 'rain': weather_day['Rainfall']}
            save_weather_record(data)
        print('Complete...')
