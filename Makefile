# Makefile for base64c project

PYTHON ?= python3
PIP ?= pip3
PYTEST ?= pytest

ifeq ($(OS),Windows_NT)
    RM = del /Q
    SEP = \\
else
    RM = rm -f
    SEP = /
endif

.PHONY: all clean build install test dist publish

all: build

build:
	$(PYTHON) setup.py build_ext --inplace

clean:
	$(RM) -r build dist *.egg-info
	find . -type d -name "__pycache__" -exec $(RM) -r {} +
	find . -type f -name "*.so" -o -name "*.pyd" -exec $(RM) {} +

install: build
	$(PIP) install -e .

test:
	$(PYTEST) -v

dist: clean
	$(PYTHON) setup.py sdist bdist_wheel

publish: dist
	@if [ -z "$(PYPI_TOKEN)" ]; then \
		echo "Error: PYPI_TOKEN environment variable is not set"; \
		exit 1; \
	fi
	twine upload dist/* -u __token__ -p $(PYPI_TOKEN)

# Add platform-specific targets if needed
ifeq ($(OS),Windows_NT)
windows_build:
	# Add Windows-specific build commands here
else
unix_build:
	# Add Unix-specific build commands here
endif