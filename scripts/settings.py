from jinja2 import Template
from pathlib import Path


GSHEET_BASE_URL = 'https://docs.google.com/spreadsheets/d/{id}'
GSHEET_SHEET_HASH = '#gid={gid}'

GITHUB_BASE_REPO_URL = 'https://github.com/dannguyen/smalldata'
GITHUB_BASE_DATASET_URL = GITHUB_BASE_REPO_URL + '/blob/master/datasets/{slug}.csv'
GITHUB_BASE_DATASET_RAW_URL = 'https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/{slug}.csv'

DATASET_TEMPLATE = Template(Path('scripts', 'dataset_template.jinja.html').read_text())


def make_dataset_anchortag(slug):
    return 'dataset-%s' % slug

def make_gsheet_url(id, gid=None):
    gurl = GSHEET_BASE_URL.format(id=id)
    if gid:
        gurl + GSHEET_SHEET_HASH.format(gid=gid)
    return gurl

def make_github_dataset_repo_url(slug):
    return GITHUB_BASE_DATASET_URL.format(slug=slug)


def make_github_dataset_raw_url(slug):
    return GITHUB_BASE_DATASET_RAW_URL.format(slug=slug)


def get_dataset_publishing_meta(data, meta):
    m = {}
    m['slug'] = meta['slug']
    m['title'] = meta['title']
    m['description'] = meta['description']
    m['date_fetched'] = meta['date_fetched']


    m['license_name'] = meta['license']['name']
    m['license_url'] = meta['license']['url']

    m['publisher_name'] = meta['publisher']['name']
    m['publisher_url'] = meta['publisher']['url']

    m['references'] = meta.get('references')
    m['notes'] = meta.get('notes')

    m['anchortag'] = make_dataset_anchortag(meta['slug'])
    m['google_spreadsheet_url'] = make_gsheet_url(id=meta['gsheet']['id'])
    m['github_dataset_url'] = make_github_dataset_repo_url(slug=meta['slug'])
    m['github_dataset_raw_url'] = make_github_dataset_raw_url(slug=meta['slug'])
    m['nrows'] = len(data)
    m['ncols'] = len(data[0].keys())

    return m




def dataset_template(datasetmeta):
    return DATASET_TEMPLATE.render(dataset=datasetmeta)
