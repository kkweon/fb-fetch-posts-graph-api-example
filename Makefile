include .env
export

format:
	pipenv run isort -y
	pipenv run black .

run:
	pipenv run python main.py
