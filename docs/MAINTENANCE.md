# Maintenance

## Dependency updates

The project uses NumPy and Pandas. Review weekly Dependabot pull requests and run the full test suite before merging upgrades. Pin exact versions only when a reproducible course environment requires them.

## Workflow policy

Python CI checks compilation, tests, and non-interactive data-analysis examples. CodeQL scans Python code. Markdown lint checks documentation. README timestamp automation is manual-only to avoid unnecessary hourly commits.

## Generated files

Keep virtual environments, Python caches, temporary text files, CSV outputs, and editor configuration out of commits. Do not commit personal datasets or secrets.
