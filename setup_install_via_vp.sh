#! /bin/bash
# This installs the app forecast within the virtualenv

# Argument list
# $1: The virtual environment folder, defaults to vp

path=$(pwd)
virt=$1
usage=$'\nUsage: setup.sh <virtualenv path>'
echo ${usage}

# Check if virtualenv folder set
if [ -z ${virt} ]; then
	echo '------------->  Defaulting virtualenv folder to vp in the current directory'
	virt='vp'
fi

echo '------------->  Creating Virtualenv `vp` in current folder'
if [ ! -d "${virt}" ]; then
	virtualenv -p python3.5 ${virt}
	echo '------------->  virtualenv created'
else
    rm -r "${virt}"
    virtualenv -p python3.5 ${virt}
	echo '------------->  Virtualenv exists, removing, creating a new one'
fi


echo '------------->  checking if forecast app is in django_forecast_package'
if [ ! -d "${path}/django_forecast_package/forecast" ]; then
	echo '------------->  Package not found, moving it......'
	mv "${path}/forecast"  "${path}/django_forecast_package"

else
	echo '------------->  forecast app in correct location'
fi


cd "${path}/django_forecast_package"
python setup.py sdist
cd "${path}"


# activating env
echo '------------->  Activating environment'
source "${virt}/bin/activate"

# install requirements
echo "------------->  Installing requirement"
pip install django==2.0
pip install requests
pip install djangorestframework

pip install "${path}/django_forecast_package/dist/forecast_package-0.1.tar.gz"

#pip install -r "${path}/requirements.txt" # (receiving this error: pip._vendor.packaging.requirements.InvalidRequirement: Invalid requirement, parse error at "'install '")

## Running migrate command
echo "-------------> Running migrate command"
python manage.py migrate

# creating a django admin super user
echo "-------------> creating a django admin super user"
python manage.py createsuperuser

# updating the db with new weather records
echo "-------------> updating the db with new weather records"
python manage.py update_forecast


# The API can be accessed at http://127.0.0.1:8000/forecast/weather_records/
echo "-------------> The API can be accessed at http://127.0.0.1:8000/forecast/weather_records/"

# starting django web server
echo "-------------> starting django web server"
python manage.py runserver


