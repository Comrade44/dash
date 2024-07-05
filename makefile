.PHONY: all install run

all: install run

install: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run: venv/bin
	./venv/bin/flask --app app/app run