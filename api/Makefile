PYBIN=venv/bin

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. $(PYBIN)/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	. $(PYBIN)/activate; python -m unittest discover todo/unittests

integration-test: venv
	. $(PYBIN)/activate; python manage.py test todo/integrationtests

migrations: venv
	. $(PYBIN)/activate; python manage.py makemigrations todo

migrate: venv
	. $(PYBIN)/activate; python manage.py migrate

makesuperuser:
	. $(PYBIN)/activate; python manage.py createsuperuser 

oneclickbuild: 
	docker-compose up --build

db-only:
	docker-compose up db

shutdown:
	docker-compose down

lint: venv
	. $(PYBIN)/activate; autopep8 -ri backend todo

run: venv
	. $(PYBIN)/activate; python manage.py runserver

clean:
	rm -rf venv
	find . -iname "*.pyc" -delete