import argparse
from csv import DictReader
from jinja2 import Template
from pathlib import Path
from sys import stdout, stderr
from settings import create_dataset_object
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
    <td><a href="{{dataset.google_spreadsheet_url}}">Google Spreadsheet</a></td>
    <td><a href="{{dataset.github_dataset_raw_url}}">Raw {{dataset.filetype}}</a></td>
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
        stderr.write("\n[Info: Reading meta from %s]\n" % mn)
        d = create_dataset_object(yaml.load(mn.read_text()))
        stdout.write(ROW_TEMPLATE.render(dataset=d))

    stdout.write("""\n</tbody></table>\n""")
