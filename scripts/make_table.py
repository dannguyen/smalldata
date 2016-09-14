import argparse
from csv import DictReader
from jinja2 import Template
from pathlib import Path
from sys import stdout, stderr
from settings import get_dataset_publishing_meta, \
                     get_dataset_local_filename, \
                     dataset_template
import yaml


ROW_TEMPLATE = Template("""
<tr>
    <td>
      <a href="#{{dataset.anchortag}}">
        {{dataset.title}}
      </a>
    </td>
    <td>
        <code>{{dataset.ncols}} x {{dataset.nrows}}</code>
    </td>
    <td><a href="{{dataset.google_spreadsheet_url}}">Spreadsheet</a></td>
    <td><a href="{{dataset.github_dataset_raw_url}}">Raw CSV</a></td>
</tr>
""")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Print out a HTML table from directory of YAMLs")
    parser.add_argument('metadir', type=str,
        help="The name of a directory of meta files")
    args = parser.parse_args()

    metadatafilenames = Path(args.metadir).glob('*.yaml')
    stdout.write("""<h2>Contents</h2><table><tbody>\n""")
    for mn in metadatafilenames:
        meta = yaml.load(mn.read_text())
        dn = get_dataset_local_filename(meta['slug'])

        stderr.write("Reading data from %s\n" % dn)

        data = list(DictReader(dn.open('r')))
        d = get_dataset_publishing_meta(data=data, meta=meta)
        stdout.write(ROW_TEMPLATE.render(dataset=d))

    stdout.write("""\n</tbody></table>\n""")
