# Makefile for base64c project

# Variables
PACKAGE_NAME = base64c
PYTHON = python
POETRY = poetry
BUILD_DIR = dist
SOURCE_FILES = $(wildcard $(PACKAGE_NAME)/*.c)

# Default target
.PHONY: all
all: build

# Build the package using poetry
.PHONY: build
build:
	@echo "Building the package..."
	$(POETRY) build

# Clean up build artifacts
.PHONY: clean
clean:
	@echo "Cleaning up build artifacts..."
	rm -rf $(BUILD_DIR) build *.egg-info

# Run tests using pytest
.PHONY: test
test:
	@echo "Running tests..."
	$(POETRY) run pytest --html=test_report.html

# Install the package locally
.PHONY: install
install:
	@echo "Installing the package locally..."
	$(POETRY) install

# Publish the package to PyPI using Poetry and PYPI_TOKEN
.PHONY: publish
publish: clean build
	@echo "Publishing the package to PyPI..."
	@if [ -z "$(PYPI_TOKEN)" ]; then \
		echo "Error: PYPI_TOKEN environment variable is not set"; \
		exit 1; \
	fi
	$(POETRY) config pypi-token.pypi $(PYPI_TOKEN)
	$(POETRY) publish

# Publish the package to Test PyPI using Poetry and TEST_PYPI_TOKEN
.PHONY: publish-test
publish-test: clean build
	@echo "Publishing the package to Test PyPI..."
	@if [ -z "$(TEST_PYPI_TOKEN)" ]; then \
		echo "Error: TEST_PYPI_TOKEN environment variable is not set"; \
		exit 1; \
	fi
	$(POETRY) config repositories.testpypi https://test.pypi.org/legacy/
	$(POETRY) config pypi-token.testpypi $(TEST_PYPI_TOKEN)
	$(POETRY) publish -r testpypi

# Show help message
.PHONY: help
help:
	@echo "Makefile for the $(PACKAGE_NAME) project"
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all              Build the package (default target)"
	@echo "  build            Build the package using Poetry"
	@echo "  clean            Clean up build artifacts"
	@echo "  test             Run tests"
	@echo "  install          Install the package locally"
	@echo "  publish          Publish the package to PyPI (requires PYPI_TOKEN env var)"
	@echo "  publish-test     Publish the package to Test PyPI (requires TEST_PYPI_TOKEN env var)"
	@echo "  help             Show this help message"