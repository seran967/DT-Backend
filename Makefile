all:	build down up

build:
		docker-compose build

push:
		docker push ${IMAGE_APP}

pull:
		docker pull ${IMAGE_APP}

up:
		docker-compose up

down:
		docker-compose down

web:
		makemigrations migrate web

bot:
		makemigrations migrate bot

run:
		python src/manage.py runserver

migrate:
		python src/manage.py migrate $(if $m, api $m,)

makemigrations:
		python src/manage.py makemigrations
		sudo chown -R ${USER} src/app/migrations/

createsuperuser:
		python src/manage.py createsuperuser

collectstatic:
		python src/manage.py collectstatic --no-input

dev:
		python src/manage.py runserver localhost:8000

command:
		python src/manage.py ${c}

shell:
		python src/manage.py shell

debug:
		python src/manage.py debug

piplock:
		pipenv install
		sudo chown -R ${USER} Pipfile.lock

lint:
		isort .
		flake8 --config setup.cfg
		black --config pyproject.toml .

check_lint:
		isort --check --diff .
		flake8 --config setup.cfg
		black --check --config pyproject.toml .

docker_check_lint:
		docker run --rm ${IMAGE_APP}
		docker-compose run web isort --check --diff .
		docker-compose run web flake8 --config setup.cfg
		docker-compose run web black --check --config pyproject.toml













