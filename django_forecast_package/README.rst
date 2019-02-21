=====
forecast
=====

forecast is a simple Django app to view weather info.


steps
-----------

1. 
* Add "rest_framework" and 'forecast.apps.ForecastConfig' to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
	'rest_framework',
	'forecast.apps.ForecastConfig',
    ]
* Add 
LOGIN_REDIRECT_URL = '/forecast/profile'


2. Include the following into URLconf in your project urls.py like this::
    
    url(r'^forecast/', include('forecast.urls')),
    url(r'^$', views.logged_out_redirect, name='logged_out_redirect'),
    url(r'^forecast/$', views.logged_out_redirect, name='logged_out_redirect'),

3. create a view in your project and add the following:
    from django.shortcuts import redirect
    def logged_out_redirect(request):
        return redirect('/forecast/logout')

4. Run `python manage.py migrate` to create the forecast models.

5. create a super user

6. Run `python manage.py update_forecast` to create the forecast models.

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

8. Visit http://127.0.0.1:8000/forecast/ to view the site.


9. # The API can be accessed at http://127.0.0.1:8000/forecast/weather_records/


Current_issues: Username login/register field to be named 'email' ....
