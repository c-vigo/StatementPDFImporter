# -*- coding: utf-8 -*-
# Author: Carlos Vigo
# Contact: carviher1990@gmail.com

""" PDF parser for credit card statements.
It accepts statement from the following issuers:
 - Cembra (Cumulus MasterCard)
 - Swisscard Cashback (AMEX / VISA / MasterCard)
The data can be saved to a CSV file compatible with Wallet import feature.
"""

# Local imports
from . import __project__, pdf_importer

__all__ = [
    __project__.__author__,
    __project__.__copyright__,
    __project__.__short_version__,
    __project__.__version__,
    __project__.__project_name__,
    'pdf_importer',
]
