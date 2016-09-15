# Small data for small data exploration

This is a collection of public datasets that can fit in a single spreadsheet table and be operated on without too much lag so that you can practice spreadsheet and pivot table functions.

Each dataset comes with a Google Spreadsheet and plaintext CSV URL, along with links back to the original publisher.

See the [meta/](meta/) folder in this repo to see the metadata for each dataset.


<!-- begin makeindex -->

python scripts/make_table.py meta
<h2>Contents</h2><table><tbody>

<tr>
    <td>
      <a href="#dataset-berkeley-jail-bookings">
        Berkeley Police Department Jail Bookings
      </a>
    </td>
    <td>
        <code>18 x 239</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1lH2P_0Bb6aZdldjLZXmUnp-zoocXmCGFMojM59kkLns">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/berkeley-jail-bookings.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-buffer-open-salaries">
        Buffer Open Salaries
      </a>
    </td>
    <td>
        <code>3 x 81</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/14OFXkKWKGQhKmDBgCGdZiByPZ9iU7CE7nzdU8TltGkc">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/buffer-open-salaries.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-census-2000-surnames">
        U.S. Census 2000, Top 10,000 Surnames
      </a>
    </td>
    <td>
        <code>11 x 10002</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/15G0cLi9MEnWjllaFA8T_FGCNj_rlSXlxFSZBpYCtavs">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/census-2000-surnames.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-denver-marijuana-gross-sales">
        Denver Marijuana Gross Sales
      </a>
    </td>
    <td>
        <code>4 x 66</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1MxgnMXRJjjZkX82I1gdPlyfnqMzo6AX5R0s6vRICfiw">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/denver-marijuana-gross-sales.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-palo-altos-salaries">
        Palo Alto and East Palo Alto City Employee Salaries
      </a>
    </td>
    <td>
        <code>28 x 11933</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1nTdSBLcUxrm29jZ1Tn6tZ8fYYNHPv_h79m0JVK_5RFI">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/palo-altos-salaries.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-ssa-babynames-1985-vs-2015">
        U.S. Baby Names 1985 vs. 2015
      </a>
    </td>
    <td>
        <code>4 x 53028</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/17dDrhGrKV68USZT55LVFMOyhD-JnBFW7jg-S3DQprZ0">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/ssa-babynames-1985-vs-2015.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-us-congressmembers">
        U.S. Congressmembers
      </a>
    </td>
    <td>
        <code>29 x 898</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1mfETOUsi2h18m4ETqLFwLYNCE0wOKcZhKYwVjz53pAk">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/us-congressmembers.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-us-federal-judges-biographies">
        U.S. Federal Judges Biographical Directory
      </a>
    </td>
    <td>
        <code>202 x 3580</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1EhWjKUF9OrWiPr_EzE_3kupTqf98Kdnr7co6hg4sb5I">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/us-federal-judges-biographies.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-us-presidential-election-county-results-2004-vs-2008">
        U.S. Presidential Election County-Level Results, 2004 and 2008
      </a>
    </td>
    <td>
        <code>15 x 6308</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1v6zqutv__4TiO0nahVJOyfs-NlD_IB7KUULRiicSO9s">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/us-presidential-election-county-results-2004-vs-2008.csv">Raw CSV</a></td>
</tr>
<tr>
    <td>
      <a href="#dataset-usgs-m4-earthquakes-contiguous-united-states">
        M4.0+ Earthquakes in the Contiguous United States
      </a>
    </td>
    <td>
        <code>22 x 6610</code>
    </td>
    <td><a href="https://docs.google.com/spreadsheets/d/1DXcqRnuxfoDNHi6c_5TTXYa8smeif-moSWI5G14IDR4">Spreadsheet</a></td>
    <td><a href="https://raw.githubusercontent.com/dannguyen/smalldata/master/datasets/usgs-m4-earthquakes-contiguous-united-states.csv">Raw CSV</a></td>
</tr>
</tbody></table>
find 'meta' -name '*.yaml' | xargs -n 1 python scripts/make_html.py

-------------

<a id="dataset-berkeley-jail-bookings"></a>


## Berkeley Police Department Jail Bookings

Adults booked into the Berkeley Police Department Jail over the past 30 days.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [City of Berkeley](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Log-Jail-Bookings/7ykt-c32j/about) |  2016-09-14 | 18 | 239 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1lH2P_0Bb6aZdldjLZXmUnp-zoocXmCGFMojM59kkLns)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/berkeley-jail-bookings.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)


Note: The "Subject" field, which contained the name of each inmate, has been removed.



#### References


- [Direct source download (CSV)](https://data.cityofberkeley.info/api/views/7ykt-c32j/rows.csv?accessType=DOWNLOAD)

-------------

<a id="dataset-buffer-open-salaries"></a>


## Buffer Open Salaries

An example of a real-world salary spreadsheet.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [Buffer](https://open.buffer.com/transparent-salaries/) |  2016-08-26 | 3 | 81 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/14OFXkKWKGQhKmDBgCGdZiByPZ9iU7CE7nzdU8TltGkc)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/buffer-open-salaries.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License](https://creativecommons.org/licenses/by-nc-sa/4.0/)


The original Buffer spreadsheet has a first line that reads "Buffer is hiring" instead of headers. The headers are on the second line. This facet is left in the Google spreadsheet and the CSV file for the user to deal with manually.



#### References


- [Source spreadsheet](https://docs.google.com/spreadsheets/d/1l3bXAv8JE5RB9siMq36-Ogngks2MT6yQ5gt8YXhUyAg/edit#gid=1533208969&vpid=G2)
- [Buffer + Transparency Overview](https://buffer.com/transparency)
- [Buffer's tweet approving of our inclusion of their spreadsheet as an example.](https://twitter.com/buffer/status/776129045897568256)
- [Buffer Diversity Dashboard](https://diversity.buffer.com/)

-------------

<a id="dataset-census-2000-surnames"></a>


## U.S. Census 2000, Top 10,000 Surnames

The top 10,000 most popular surnames as recorded by the U.S. 2000 Census. Includes demographic breakdown of each name.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [U.S. Census](http://www.census.gov/topics/population/genealogy/data/2000_surnames.html) |  2016-08-01 | 11 | 10002 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/15G0cLi9MEnWjllaFA8T_FGCNj_rlSXlxFSZBpYCtavs)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/census-2000-surnames.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)





#### References


- [Direct source download (zip)](http://www2.census.gov/topics/genealogy/2000surnames/names.zip)

-------------

<a id="dataset-denver-marijuana-gross-sales"></a>


## Denver Marijuana Gross Sales

This data set summarizes the total dollar value of medical and retail marijuana sold within the City and County of Denver.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [City and County of Denver Office of Marijuana Policy](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-marijuana-gross-sales) |  2016-09-14 | 4 | 66 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1MxgnMXRJjjZkX82I1gdPlyfnqMzo6AX5R0s6vRICfiw)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/denver-marijuana-gross-sales.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [Creative Commons Attribution 3.0](https://www.denvergov.org/opendata/termsofuse)





#### References


- [Direct source download (CSV)](http://data.denvergov.org/download/gis/marijuana_gross_sales/csv/marijuana_gross_sales.csv)

-------------

<a id="dataset-palo-altos-salaries"></a>


## Palo Alto and East Palo Alto City Employee Salaries

Salary data from 2009 through 2015 for Palo Alto and East Palo Alto


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [California State Controller](http://publicpay.ca.gov/) |  2016-09-14 | 28 | 11933 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1nTdSBLcUxrm29jZ1Tn6tZ8fYYNHPv_h79m0JVK_5RFI)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/palo-altos-salaries.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)



Here's the shell code I used to build the data (requires installing csvkit):

~~~
  curl -O http://publicpay.ca.gov/RawExport/[2009-2015]_City.zip

  unzip '*.csv'

  sed -n 5p  2009_City.csv > all.csv find . -name '*_City.csv' \
    | while read -r fname; do
        tail -n +6 "$fname" \
         >> all-cities.csv
      done

  csvgrep -c 'Entity Name' -m 'Palo Alto' \
      -e latin1 \
      all-cities.csv > palo-altos-salaries.csv
~~~



#### References


- [Source list of zipped data files](http://publicpay.ca.gov/Reports/RawExport.aspx)

-------------

<a id="dataset-ssa-babynames-1985-vs-2015"></a>


## U.S. Baby Names 1985 vs. 2015

Nationwide counts of baby names by sex, according to Social Security Number applications in the years 1985 and 2015.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html) |  2016-09-14 | 4 | 53028 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/17dDrhGrKV68USZT55LVFMOyhD-JnBFW7jg-S3DQprZ0)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/ssa-babynames-1985-vs-2015.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)





#### References


- [Direct source download (zip)](https://www.ssa.gov/oact/babynames/names.zip)

-------------

<a id="dataset-us-congressmembers"></a>


## U.S. Congressmembers

A listing of current and former notable Congressmembers, including biographical information and identifiers into other databases.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [Sunlight Foundation and the unitedstates project](https://sunlightlabs.github.io/congress/#legislator-spreadsheet) |  2016-09-14 | 29 | 898 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1mfETOUsi2h18m4ETqLFwLYNCE0wOKcZhKYwVjz53pAk)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/us-congressmembers.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)





#### References


- [Direct source download (CSV)](http://unitedstates.sunlightfoundation.com/legislators/legislators.csv)
- [unitedstates/congress-legislators repo](https://github.com/unitedstates/congress-legislators)

-------------

<a id="dataset-us-federal-judges-biographies"></a>


## U.S. Federal Judges Biographical Directory

Biographical and political information about U.S. federal judges, from 1789 to the present.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [Federal Judicial Center](http://www.fjc.gov/history/home.nsf/page/export.html) |  2016-09-14 | 202 | 3580 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1EhWjKUF9OrWiPr_EzE_3kupTqf98Kdnr7co6hg4sb5I)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/us-federal-judges-biographies.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)





#### References


- [Direct source download (csv)](http://www.fjc.gov/history/export/jb.txt)

-------------

<a id="dataset-us-presidential-election-county-results-2004-vs-2008"></a>


## U.S. Presidential Election County-Level Results, 2004 and 2008

County-level results for the U.S. general elections in 2004 and 2008.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [USGS National Atlas](https://catalog.data.gov/dataset/2008-presidential-general-election-county-results-direct-download) |  2016-08-01 | 15 | 6308 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1v6zqutv__4TiO0nahVJOyfs-NlD_IB7KUULRiicSO9s)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/us-presidential-election-county-results-2004-vs-2008.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)


This data actually comes from the wrangled version as created by the [Hello World Data project](https://github.com/helloworlddata/us-presidential-election-county-results).

The 2012 data is [not currently available](https://gist.github.com/dannguyen/2de0fcd2ba3100b4698cd5af6ae61754).



#### References


- [Data.gov landing page for 2004 Presidential General Election, County Results](http://catalog.data.gov/dataset/2004-presidential-general-election-county-results-direct-download)
- [Data.gov landing page for 2008 Presidential General Election, County Results](https://catalog.data.gov/dataset/2008-presidential-general-election-county-results-direct-download)

-------------

<a id="dataset-usgs-m4-earthquakes-contiguous-united-states"></a>


## M4.0+ Earthquakes in the Contiguous United States

All 4.0+ magnitude earthquakes as recorded by the USGS for the lower 48 United States.


| Publisher   | Last fetched | Columns | Rows |
|-------------|----|---------|------|
| [United States Geological Survey](http://earthquake.usgs.gov/earthquakes/search/) |  2016-09-14 | 22 | 6610 |

- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1DXcqRnuxfoDNHi6c_5TTXYa8smeif-moSWI5G14IDR4)
- [Github](https://github.com/dannguyen/smalldata/blob/master/datasets/usgs-m4-earthquakes-contiguous-united-states.csv)
- [CSV direct download](dataset.github_dataset_raw_url)

License: [MIT](https://opensource.org/licenses/MIT)





#### References


- [Direct source download (CSV)](http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=1900-01-01%2000:00:00&endtime=2016-12-31%2023:59:59&maxlatitude=50&minlatitude=24.6&maxlongitude=-65&minlongitude=-125&minmagnitude=4&orderby=time-asc)
- [Glossary](http://earthquake.usgs.gov/earthquakes/feed/v1.0/glossary.php)

