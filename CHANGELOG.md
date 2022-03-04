# Changelog

## [0.4.0]
### Changed
- Bump minimum required Python version to 3.7
- Update dependencies
  - discord-webhook ~=0.14 -> ~=0.15
  - mcstatus ~=6.5 -> ~=8.0

## [0.3.0]
### Added
- Add an option to select between ping and status

### Changed
- Remove unused default variable
- Clean up and rearrange webhook arguments
- Remove unused function for exiting on error
- Format exception messages better for logging
- More friendly error message when ping fails

### Fixed
- Include missing arguments in the initial debug log message

## [0.2.0]
### Added
- Add online and offline webhook thumbnail options
- Add default webhook thumbnails with option to disable them

### Changed
- Rename 'thumbnail' -> 'thumb' in arguments
- Use constants for default values

### Fixed
- Fix spelling in setup.cfg

## [0.1.0]
Initial release
