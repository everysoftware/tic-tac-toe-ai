.PHONY: format
format:
	ruff format src tests

.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: run
run:
	python -m src
