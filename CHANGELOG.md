# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5] - 2021-12-26

- Fix [issue #6](https://github.com/c-vigo/StatementPDFImporter/issues/6): statements were silently skipped if the
amount contains an apostrophe

- Fix [issue #4](https://github.com/c-vigo/StatementPDFImporter/issues/4): last transactions got omitted in long
statements (over two pages)

## [0.4] - 2021-03-27

- Fix bug: amounts above 1000 with coma-separated thousands

## [0.3] - 2021-02-24

- Fix [issue #2](https://github.com/c-vigo/StatementPDFImporter/issues/2): newline in transaction description messing with CSV output

## [0.2] - 2021-02-07

- Hotfix

## [0.1] - 2021-02-03

- First version of the package
- Supported statements:
  - [Cembra & Cumulus](https://www.cembra.ch/en/cards/cembra-mastercard/) MasterCard
  - [SwissCard Cashback](https://www.swisscard.ch/en/private-customers/products) (AMEX / VISA / MasterCard)

[Unreleased]: https://github.com/c-vigo/StatementPDFImporter/compare/v0.2...HEAD
[0.5]: https://github.com/c-vigo/StatementPDFImporter/tree/v0.5
[0.4]: https://github.com/c-vigo/StatementPDFImporter/tree/v0.4
[0.3]: https://github.com/c-vigo/StatementPDFImporter/tree/v0.3
[0.2]: https://github.com/c-vigo/StatementPDFImporter/tree/v0.2
[0.1]: https://github.com/c-vigo/StatementPDFImporter/tree/v0.1
