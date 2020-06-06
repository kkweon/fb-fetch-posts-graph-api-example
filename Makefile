include .env
export

format:
	pipenv run isort -y
	pipenv run black .

test:
	pipenv run python -m unittest discover -p "*_test.py"

run:
	pipenv run python main.py
