.PHONY: clean
clean:
	rm -rf __pycache__

.PHONY: develop
develop:
	pip install -r requirements.txt

.PHONY: clean-requirements
clean-requirements:
	rm -f requirements.txt

.PHONY: compile-requirements
compile-requirements:
	pip-compile -v --output-file requirements.txt requirements.in

.PHONY: pip-tools
pip-tools:
	pip install "pip-tools>=6.0, <7.0"

.PHONY: sync-requirements
sync-requirements:
	pip-sync requirements.txt

.PHONY: requirements
requirements: clean-requirements pip-tools compile-requirements sync-requirements