.PHONY: index lint search

index:
	python scripts/rebuild_index.py

lint:
	python scripts/lint_wiki.py

search:
	python scripts/search_wiki.py "$(Q)"
