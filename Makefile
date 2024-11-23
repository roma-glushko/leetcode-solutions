SOURCE ?= src scripts

help:
	@echo "============="
	@echo "Roma's LeetCode Solutions ✨"
	@echo "============="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint-check: ## Lint source code without modifying it
	@echo "🧹 Ruff"
	@pdm run ruff format $(SOURCE) --diff
	@pdm run ruff check $(SOURCE)
	@pdm "🧽 MyPy"
	@poetry run mypy --pretty $(SOURCE)

lint: ## Lint source code
	@echo "🧹 Ruff"
	@pdm run ruff format $(SOURCE)
	@pdm run ruff check --fix $(SOURCE)
	@echo "🧽 MyPy"
	@pdm run mypy --pretty $(SOURCE)
