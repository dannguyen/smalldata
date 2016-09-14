pages:
	find 'meta' -name '*.yaml' | xargs -n 1 python scripts/make_html.py


table:
	python scripts/make_table.py meta
