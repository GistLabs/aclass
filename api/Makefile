PYBIN=venv/bin

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. $(PYBIN)/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	. $(PYBIN)/activate; python -m unittest discover todo/unittests

integration-test: venv
	docker-compose up -d db
	sleep 8
	. $(PYBIN)/activate; python manage.py test todo/integrationtests
	docker-compose down

migrations: venv
	. $(PYBIN)/activate; python manage.py makemigrations todo

migrate: venv
	. $(PYBIN)/activate; python manage.py migrate

makesuperuser:
	. $(PYBIN)/activate; python manage.py createsuperuser 

oneclickbuild: 
	docker-compose up --build

db-up:
	docker-compose up db -d

shutdown:
	docker-compose down

lint: venv
	. $(PYBIN)/activate; autopep8 -ri backend todo

run: venv
	. $(PYBIN)/activate; python manage.py runserver

clean:
	rm -rf venv
	find . -iname "*.pyc" -delete

build-docker:
	docker build . --tag class/api

# CD
deploy: test integration-test build-docker
	kubectl delete pod -l app=api
	kubectl apply -f infrastructure/api.yml

# Localhost access
bind-api-locally:
	kubectl port-forward service/api 8000:8000

# Installation and set-up
install-kube-postgres:
	kubectl apply -f infrastructure/postgres.yml