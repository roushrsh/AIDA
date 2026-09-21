# Input files

File formats must match the released application. The screenshots do not establish a complete schema, so the fields below need author confirmation.

| Input | Used by | Required documentation |
|---|---|---|
| Peptide list | Database Generator | **AUTHOR TODO:** extension, delimiter, header, sequence syntax, charge and protein columns |
| AIDA database | Main, Offline Search, Gradient Cal | **AUTHOR TODO:** version, column order, required predictions and missing-value rules |
| RAW | Offline Search, Post Run Script | **AUTHOR TODO:** supported formats and required scan metadata |
| Chopin CSV | Post Run Script | **AUTHOR TODO:** generator, identifiers and schema |
| MS3Signal CSV | Post Run Script | **AUTHOR TODO:** generator, scan matching and reporter-channel order |
| Calibration results | Gradient Cal | **AUTHOR TODO:** generator and order/time columns |
| Gradient table | Gradient Cal | **AUTHOR TODO:** time/%B/flow fields and interpretation |
| Adaptation runs | Transfer Learn | **AUTHOR TODO:** formats, number of runs and split rules |

## Schema template

Duplicate this table for each input:

| Column name/index | Meaning | Type/units | Required? | Valid example |
|---|---|---|---|---|
| AUTHOR TODO | AUTHOR TODO | AUTHOR TODO | AUTHOR TODO | AUTHOR TODO |

State whether indexing is zero-based or one-based. Include a validated short example and explain modification notation and missing values.
