flake:
	flake8 ./src

isort:
	isort ./src

black:
	black .

mypy:
	mypy ./src

lint:
	make isort && make black && make flake  && make mypy
