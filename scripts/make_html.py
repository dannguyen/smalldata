import argparse
from csv import DictReader
from pathlib import Path
from sys import stdout, stderr
from settings import create_dataset_object,\
                     dataset_template
import yaml


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Print out a HTML version of dataset YAML file")
    parser.add_argument('infile', type=argparse.FileType('r'),
        help="The name of a dataset YAML file")
    args = parser.parse_args()
    metaname = args.infile
    stderr.write("Reading meta from %s\n" % metaname.name)
    d = create_dataset_object(yaml.load(metaname.read()))
    stdout.write(dataset_template(d))
