#This is sample Makefile that covers a number of day to day commands in Django. I have added comments on the usage of the commands
serve:
	python manage.py runserver
	# Usage: make serve
superuser:
	python manage.py createsuperuser --username $(name)
	# Usage: make superuser name=<the name of the superuser>
migrate:
	python manage.py migrate
	# Usage: make migrate
app:
	django-admin startapp $(name)
	# Usage: make app name=<name of your app>
migrations:
	python manage.py makemigrations $(app)
	# Usage: make migrations or make migrations app=<name of your app>
check:
	python manage.py check
	# Usage: make check
collectstatic:
	python manage.py collectstatic
	#Usage: make collectstatic