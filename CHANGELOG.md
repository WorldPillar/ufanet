# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-01-21

### Added

- README.md.

## [0.5.2] - 2024-01-21

### Added

- More unit tests.

## [0.5.1] - 2024-01-21

### Fixed

- Fix archiver function when bwt is active  
and the result is lexicographically the smallest string instead of shortest string.

## [0.5.0] - 2024-01-20

### Changed

- Archiver and unpacker functions now combine RLE and BWT.

## [0.4.0] - 2024-01-20

### Added

- Burrows-Wheeler transform (BWT).
- Unit tests for BWT.

## [0.3.1] - 2024-01-20

### Added

- More unit tests to verify that archiver and unpacker work correctly.
- Unit tests for TypeError checking

## [0.3.0] - 2024-01-19

### Added

- Escaping of digits and '/'.
- Unit tests with digits and '/'.

### Changed

- Archiver and Unpacker functions to support shielding.

## [0.2.0] - 2024-01-19

### Added

- Unpacker function for decompressing strings.
- Unit tests for mutual testing of functions.

## [0.1.0] - 2024-01-19

### Added

- Archiver function for compressing strings   
  using Run-Length Encoding (RLE).
- CHANGELOG file.