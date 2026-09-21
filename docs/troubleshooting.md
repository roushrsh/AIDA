# Troubleshooting

The checks below are diagnostic starting points. Add confirmed application-specific error messages as they become available.

## Environment check fails

Check the selected Python path and the failed component. Separate a missing Python package from a missing .NET or application component. Follow [Environment Check](environment-check.md).

## Input cannot be read

Check that the path exists and that the extension, delimiter and columns match the documented input schema. **AUTHOR TODO:** Add the exact validation messages and supported formats.

## A task stops or produces no expected output

Record the error and surrounding log text. Check input paths and whether the output folder is writable. **AUTHOR TODO:** Document each known failure and whether restarting preserves or replaces partial output.

## Quantification output is empty

Check that the supplied files belong to the intended run. **AUTHOR TODO:** Explain the identifiers used for spectrum matching and how to check channel/scan compatibility.

## Gradient or adaptation results look wrong

Review input units, calibration provenance and the held-out evaluation. **AUTHOR TODO:** Add diagnostic plots and quantitative acceptance criteria for each workflow.

## Reporting a problem

Include the AIDA version, selected tab, operating system, relevant settings, error text and a minimal shareable example. Remove private sample names or paths if necessary.

**AUTHOR TODO:** Add the official support or issue-tracker URL.
