install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	python -m pytest -vv --cov=mylib test_*.py
build:
	docker build -t deploy-fastapi .
run:
	docker run -p 127.0.0.1:8080:8080 f7a5c6a839ce
deploy:
	#deploy
all: install lint test deploy