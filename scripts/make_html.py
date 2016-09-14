import argparse
from csv import DictReader
from pathlib import Path
from sys import stdout, stderr
from settings import get_dataset_publishing_meta,\
                     dataset_template,\
                     get_dataset_local_filename
import yaml


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Print out a HTML version of dataset YAML file")
    parser.add_argument('infile', type=argparse.FileType('r'),
        help="The name of a dataset YAML file")
    args = parser.parse_args()
    meta = yaml.load(args.infile.read())
    datafilepath = get_dataset_local_filename(meta['slug'])
    stderr.write("Reading data from %s\n" % datafilepath)
    # if not datafilepath.exists():
    #     stderr.write("Warning, %s does not exist; skipping\n" % datafilepath)
    # else:
    data = list(DictReader(datafilepath.open('r')))
    d = get_dataset_publishing_meta(data=data, meta=meta)
    stdout.write(dataset_template(d))
