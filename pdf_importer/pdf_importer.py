""" PDF parser for credit card statements.
It accepts statement from the following issuers:
 - Cembra (Cumulus MasterCard)
 - Swisscard Cashback (AMEX / VISA / MasterCard)
The data can be saved to a CSV file compatible with Wallet import feature.
"""

# Imports
import csv
from argparse import ArgumentParser

# Local packages
from .__project__ import (
    __documentation__ as docs_url,
    __module_name__ as module,
    __description__ as prog_desc,
)
from Importers import extract_cembra, extract_cashback


def pdf_importer():
    """The main routine. It parses the input argument and acts accordingly."""

    # The argument parser
    ap = ArgumentParser(
        prog=module,
        description=prog_desc,
        add_help=True,
        epilog='Check out the package documentation for more information:\n{}'.format(docs_url)
    )

    # Positional arguments:
    # 1. File name
    ap.add_argument(
        'filename',
        help='PDF file to parse',
        type=str,
    )

    # 2. Statement type
    ap.add_argument(
        'type',
        help='statement type',
        type=str,
        choices=['cembra', 'cashback']
    )

    # 3. Output file
    ap.add_argument(
        '--o',
        '-output',
        dest='output',
        help='output CSV file',
        type=str,
        default=None
    )

    # Parse the arguments
    args = ap.parse_args()

    # Extract data from PDF
    if args.type == 'cembra':
        print('Processing file {} as a Cembra PDF statement.'.format(args.filename))
        entries = extract_cembra(args.filename)
    elif args.type == 'cashback':
        entries = extract_cashback(args.filename)
    else:
        raise RuntimeError('Invalid statement type {}'.format(args.type))

    # Print to console
    total_value = 0.
    for entry in entries:
        print('{}  {:+7.2f}   {}'.format(entry[0], entry[1], entry[2]))
        total_value += entry[1]
    print('\nTotal: {:+7.2f}'.format(total_value))

    # Save to CSV file
    if args.output is not None:
        print('Saving data to {}.'.format(args.output))
        with open(args.output, mode='w') as f:
            writer = csv.writer(
                f,
                delimiter=';',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            for entry in entries:
                writer.writerow(entry)
