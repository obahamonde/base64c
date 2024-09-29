# Makefile for base64c project

# Variables
PACKAGE_NAME = base64c
PYTHON = python
BUILD_DIR = dist
SOURCE_DIR = src/base64c
SOURCE_FILES = $(wildcard $(SOURCE_DIR)/*.c)

# Default target
.PHONY: all
all: build

# Build the package using setuptools
.PHONY: build
build:
	$(PYTHON) setup.py build_ext --inplace

# Clean up build artifacts
.PHONY: clean
clean:
	@echo "Cleaning up build artifacts..."
	rm -rf $(BUILD_DIR) build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.so" -delete

# Run tests using pytest
.PHONY: test
test:
	@echo "Running tests..."
	pytest --html=test_report.html

# Install the package locally
.PHONY: install
install:
	@echo "Installing the package locally..."
	pip install -e .

# Build source distribution
.PHONY: dist
dist: clean
	@echo "Building source distribution..."
	$(PYTHON) setup.py sdist

# Publish the package to PyPI
.PHONY: publish
publish: dist
	@echo "Publishing the package to PyPI..."
	@if [ -z "$(PYPI_TOKEN)" ]; then \
		echo "Error: PYPI_TOKEN environment variable is not set"; \
		exit 1; \
	fi
	twine upload dist/* -u __token__ -p $(PYPI_TOKEN)

# Show help message
.PHONY: help
help:
	@echo "Makefile for the $(PACKAGE_NAME) project"
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all              Build the package (default target)"
	@echo "  build            Build the package using setuptools"
	@echo "  clean            Clean up build artifacts"
	@echo "  test             Run tests"
	@echo "  install          Install the package locally"
	@echo "  dist             Build source distribution"
	@echo "  publish          Publish the package to PyPI (requires PYPI_TOKEN env var)"
	@echo "  help             Show this help message"