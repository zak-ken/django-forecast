# django-forecast
This Django-Forecast project is based on a assignment I did with regards to scraping data from a weather site and displaying it in a
table.

Weather App Assignment:
----------------------
The main goal of the assignment is to test your skills in learning new technologies and gauge code quality. You
will be required to use the Django framework to develop a simple application. You need to setup a virtualenv
for the app and install Django. Read through the django documentation and proceed with the development of
the assignment. Django: http://www.djangoproject.com

Basic Requirements:
* Homepage - Logged-out landing page with links to login/register
* Registration and Login:
    Users should be able to register themselves by filling in a form with 3 fields:
    email, password, password_repeat
    Basic validation should be done on the email address and the two password boxes should match up.
    After registering the user should be able to login.
* Logged in landing page:
    After logging in the user should be shown the latest weather forecasts retrieved from the database.
    data should be paginated to show 3 records per page.
* Admin section:
    There should be a basic admin section to edit User and Weather records
* API (REST):
    the weather data should be exposed in a simple json format.
    Clients authenticate using basic HTTP auth.
* Use latest django and python 2.7 or 3.4 - You may use any extension libraries you see fit.
* extra points for tests, packaging, documentation.
* The delivered code needs to run (obvious - but we have seen some funny results)
    - assignments with major bugs will be disqualified.

Forecast data:
--------------
The forecast data should be retrieved from http://weather.news24.com/sa/cape-town. The page makes use of
an API to populate weather data, you will have to find the API and use it to store the relevant weather data in
your database(Note: the JSON string returned from this API will need to be fixed before it can be parsed). In
the db you should store the date, min temp, max temp, wind, rain. Ideally the retrieval of the forecast data
would be run as a Django management command via cron.
