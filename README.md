# README

[![PyPI Latest Version](https://badge.fury.io/py/pdf-importer.svg)](https://badge.fury.io/py/pdf-importer)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Statement PDF Importer

**pdf-importer** is a PDF parser for credit card statements.
It accepts statement from the following issuers:

 - [Cembra & Cumulus](https://www.cembra.ch/en/cards/cembra-mastercard/) MasterCard
 - [Swisscard Cashback](https://www.swisscard.ch/en/private-customers/products) (AMEX / VISA / MasterCard)

The data can be saved to a CSV file compatible with [Wallet by budgetbakers](https://budgetbakers.com/) import feature.

## Dependencies

 - [Python 3.6](https://www.python.org/downloads/release/python-360/) and [pip 10.0](https://pip.pypa.io/en/stable/).
 - [camelot-py](https://camelot-py.readthedocs.io/en/master/) and
   [opencv-python](https://github.com/opencv/opencv-python) for PDF parsing.
 - [python-dateutil](https://dateutil.readthedocs.io/en/stable/) for date format management.
 - [pandas](https://pandas.pydata.org/) for CSV export.

## Installation

You can install the package by cloning the [GitHub repository](https://github.com/c-vigo/StatementPDFImporter) or directly
using [pip](https://pip.pypa.io/en/stable/):

```
python -m pip install pdf-importer
```

## Usage

You can parse a PDF statement simply with

```
python -m pdf_importer [filename] [type] [-o csv_file]
```
where 

 - *filename* is the full path to the PDF file
 - *type* is either *cembra* or *cashback*
 - *csv_file* is the full path to the CSV file where the data is saved.

## Authors

* [**Carlos Vigo**](mailto:carviher1990@gmail.com?subject=[GitHub%-%pdf-importer]) - *Initial work* - 
[GitHub](https://github.com/c-vigo)

## Contributing

Please read our [contributing policy](CONTRIBUTING.md) for details on our code of
conduct, and the process for submitting pull requests to us.

## Versioning

We use [Git](https://git-scm.com/) for versioning. For the versions available, see the 
[tags on this repository](https://gitlab.ethz.ch/exotic-matter/cw-beam/pdf-importer).

## License

This project is licensed under the [GNU GPLv3 License](LICENSE.md)

## Built With

* [PyCharm Professional 2020](https://www.jetbrains.com/pycharm//) - The IDE used
* [Sphinx](https://www.sphinx-doc.org/en/master/index.html) - Documentation
