clean:
	rm -rf .pytest_cache/ .coverage

lint:
	flake8 app/

format:
	black app/ --line-length 79
