default:
	find 'meta' -name '*.yaml' | xargs -n 1 python scripts/make_html.py
