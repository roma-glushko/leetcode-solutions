SOURCE ?= src scripts

help:
	@echo "============="
	@echo "Roma's LeetCode Solutions ✨"
	@echo "============="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint-check: ## Lint source code without modifying it
	@echo "🧹 Ruff"
	@uv run ruff format $(SOURCE) --diff
	@uv run ruff check $(SOURCE)
	@echo "🧽 MyPy"
	@uv run mypy --pretty $(SOURCE)

lint: ## Lint source code
	@echo "🧹 Ruff"
	@uv run ruff format $(SOURCE)
	@uv run ruff check --fix $(SOURCE)
	@echo "🧽 MyPy"
	@uv run mypy --pretty $(SOURCE)
