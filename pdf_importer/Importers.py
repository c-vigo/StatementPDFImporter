""" Collection of importers.
"""

# Imports

# Third party
import camelot
from dateutil.parser import parse
from pandas import concat


def extract_cembra(filename):
    entries = []

    # noinspection PyUnresolvedReferences
    tables = camelot.read_pdf(filename, pages='2-end', flavor='stream', table_areas=['60,670,600,100'])
    df = tables[0].df
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header

    for _, row in df.iterrows():
        try:
            date = parse(row[1].strip(), dayfirst=True).date()
            date2 = parse(row[0].strip(), dayfirst=True).date()
            text = row[2]
            credit = row[3]
            debit = row[4]
            amount = -float(debit) if debit else float(credit)
            entries.append([date, amount, text])
        except ValueError:
            pass

    return entries


def extract_cashback(filename):
    entries = []

    # noinspection PyUnresolvedReferences
    table1 = camelot.read_pdf(
        filename,
        pages='1',
        flavor='stream',
        table_areas=['50,320,560,50'],
        columns=['120,530']
    )
    table2 = camelot.read_pdf(
        filename,
        pages='2-end',
        flavor='stream',
        table_areas=['50,800,560,50'],
        columns=['120,530']
    )

    df = concat([table1[0].df, table2[0].df])

    for index, row in df.iterrows():
        try:
            date = parse(row[0].strip(), dayfirst=True).date()
            text = row[1]
            amount = -float(row[2])

            entries.append([date, amount, text])
        except ValueError:
            pass

    return entries
