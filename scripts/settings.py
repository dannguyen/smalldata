from copy import deepcopy
from csv import DictReader
from jinja2 import Template
from pathlib import Path

GSHEET_BASE_URL = 'https://docs.google.com/spreadsheets/d/{id}'
GSHEET_SHEET_HASH = '#gid={gid}'

GITHUB_BASE_REPO_URL = 'https://github.com/dannguyen/smalldata'
GITHUB_BASE_DATASET_URL = GITHUB_BASE_REPO_URL + '/blob/master/{localpath}'
GITHUB_BASE_DATASET_RAW_URL = 'https://raw.githubusercontent.com/dannguyen/smalldata/master/{localpath}'

DATASET_TEMPLATE = Template(Path('scripts', 'dataset_template.jinja.html').read_text())


# def get_dataset_local_filename(slug):
#     return Path('datasets', '%s.csv' % slug)

def make_dataset_anchortag(slug):
    return 'dataset-%s' % slug

def make_gsheet_url(id, gid=None):
    gurl = GSHEET_BASE_URL.format(id=id)
    if gid:
        gurl + GSHEET_SHEET_HASH.format(gid=gid)
    return gurl

def make_github_dataset_repo_url(localpath):
    return GITHUB_BASE_DATASET_URL.format(localpath=localpath)


def make_github_dataset_raw_url(localpath):
    return GITHUB_BASE_DATASET_RAW_URL.format(localpath=localpath)




def create_dataset_object(boilerplate):
    m = create_dataset_meta(boilerplate)
    return create_dataset_stats(m)


def create_dataset_meta(boilerplate):
    """
    meta is a dict read in from a standard YAML
    returns a dict
    i.e. this is a stupid person's class instance
    """
    b = boilerplate
    m = {}
    m['slug'] = b['slug']

    if b.get('local_filepath'):
        m['local_filepath'] = Path(b.get('local_filepath'))
    else:
        m['local_filepath'] = Path('datasets', '%s.csv' % m['slug'])

    m['filetype'] = 'workbook' if 'xls' in m['local_filepath'].suffix.lower() else 'csv'
    m['gsheet'] = b['gsheet']

    m['title'] = b['title']
    m['description'] = b['description']
    m['date_fetched'] = b['date_fetched']
    m['license_name'] = b['license']['name']
    m['license_url'] = b['license']['url']

    m['publisher_name'] = b['publisher']['name']
    m['publisher_url'] = b['publisher']['url']

    m['references'] = b.get('references')
    m['notes'] = b.get('notes')

    m['anchortag'] = make_dataset_anchortag(b['slug'])
    m['google_spreadsheet_url'] = make_gsheet_url(id=b['gsheet']['id'])
    m['github_dataset_url'] = make_github_dataset_repo_url(m['local_filepath'])
    m['github_dataset_raw_url'] = make_github_dataset_raw_url(m['local_filepath'])
    return m


def create_dataset_stats(meta):
    """
    meta ia  dict as returned from
    create_dataset_meta()

    returns a copy of the meta with stats attached
    """
    m = deepcopy(meta)
    datarows = get_dataset_rows(m)

    if m['filetype'] == 'csv':
        m['nrows'] = len(datarows)
        m['ncols'] = len(datarows[0].keys())
    elif m['filetype'] == 'workbook':
        m['ncols'] = sum(len(df[0].keys()) for df in datarows)
        m['nrows'] = sum(len(df) for df in datarows)
    else:
        raise TypeError("Unexpected filetype: %s" % m['filetype'])
    return m


def get_dataset_rows(meta):
    """

    if filename is a xlsx file, returns a list of list of dicts
    else: returns a list of dicts

    relies on get_dataset_local_filename() and meta['slug']

    right now wishing I had made this all OOP...
    """
    srcpath = meta['local_filepath']
    if meta['filetype'] == 'workbook':
        import pandas as pd
        sheetindices = list(range(len(meta['gsheet']['sheets'])))
        dfs = pd.read_excel(str(srcpath), sheetname=sheetindices)
        return [x.to_dict('records') for x in dfs.values()]
    else:
        # assume CSV
        return list(DictReader(srcpath.open('r')))


def dataset_template(datasetmeta):
    return DATASET_TEMPLATE.render(dataset=datasetmeta)
