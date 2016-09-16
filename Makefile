.PHONY: pre-commit
pre-commit:
	@tox -e pre-commit -- install -f --install-hooks

.PHONY: test
test: pre-commit
	@tox
