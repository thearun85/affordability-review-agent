.PHONY: test lint fmt typecheck check clean

test:
	poetry run pytest

lint:
	poetry run ruff check .

fmt:
	poetry run ruff format .

fix:
	poetry run ruff check . --fix

typecheck:
	poetry run mypy src tests

check: lint typecheck test

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -prune -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -prune -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -prune -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete
	find . -type f -name "*~" -delete
	
