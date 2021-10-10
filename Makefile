.PHONY: list clean build install uninstall
SHELL := /bin/bash

PKG = adbloater

list:
	@cat Makefile

clean:
	rm -rf *.egg-info dist
	find . -regex '^.*\(__pycache__\|\.py[co]\)$$' -delete

build: clean
	python setup.py sdist

install:
	pip install -e .

uninstall:
	# note scripts from /.local/bin don't get removed when installed with -e.
	pip uninstall $(PKG)

test:
	cd tests && pytest -s

format:
	black $(PKG)

venv:
	python3 -m venv venv \
	&& source venv/bin/activate \
	&& pip install -r requirements_dev.txt


