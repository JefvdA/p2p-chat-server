.DEFAULT_GOAL := help

run-dev: ## Run the dev environment of the API
	@flask run --debug

test: ## Run all tests and generate coverage report
	@coverage run -m unittest

coverage: ## Display the coverage report in the terminal
	@coverage report

coverage-html: ## Generate html to show coverage report
	@coverage html

.PHONY: help
help: ## Show this help menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
