all: lint coverage

.PHONY: test
test:  ## Run tests
	cd backend && pytest

.PHONY: coverage
coverage:  ## Run tests with coverage
	cd backend && pytest --cov

.PHONY: flake
flake:  ## Run flake8
	cd backend && flake8 --statistics --count

.PHONY: eslint
eslint:  ## Run eslint
	cd frontend && npm run lint --no-fix

.PHONY: lint
lint: flake eslint  ## Run all linters

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
