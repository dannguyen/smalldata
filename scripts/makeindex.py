import argparse
from csv import DictReader
from jinja2 import Template
from pathlib import Path
import yaml
from sys import stdout, stderr



DATASET_TEMPLATE = Template("""
### {{dataset.title}}

- [Google Spreadsheet]({{dataset.urls.gdrive}})
- [Github](datasets/{{dataset.slug}}.csv)


| Last fetched | Columns | Rows |
|--------------|---------|------|
| {{dataset.date_fetched}} | {{ncols}} | {{nrows}} |


###### Original publisher

[{{dataset.publisher}}]({{dataset.urls.landing if dataset.urls.landing else dataset.urls.original}})

###### Description

{{dataset.description}}

""")




if __name__ == '__main__':
    parser = argparse.ArgumentParser("Print out a HTML version of datasets.yaml")
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()
    for dataset in yaml.load(args.infile.read()):
        datafilepath = Path('datasets', dataset['slug'] + '.csv')
        if not datafilepath.exists():
            stderr.write("Warning, %s does not exist; skipping\n" % datafilepath)
        else:
            data = list(DictReader(datafilepath.open('r')))
            stdout.write(DATASET_TEMPLATE.render(
                dataset=dataset,
                nrows=len(data),
                ncols=len(data[0].keys()),
            ))
    # print(datasets)

