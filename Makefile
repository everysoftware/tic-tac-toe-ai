.PHONY: format
format:
	ruff format src tests

.PHONY: freeze
freeze:
	pip freeze > requirements.txt