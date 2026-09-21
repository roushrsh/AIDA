# AIDA documentation

AIDA supports AI-driven acquisition for TMT-based proteomics on Thermo Tribrid instruments. Its interface brings together database preparation, acquisition configuration and tools for processing calibration runs, adjusting gradients and adapting predictions.

This guide explains the interface tab by tab and provides a starting point for a reproducible tutorial. Begin with [Installation](installation.md), then follow [Quick start](quick-start.md). Use the tab reference when you need to look up an individual control.

```{note}
Author draft. Fields marked **AUTHOR TODO** need confirmation against the released AIDA software. Screenshots show the supplied interface; they do not establish universal recommended settings.
```


## Two starting points

- **You already have a suitable database:** use the [Main tab](main.md) to configure method generation.
- **You need a new database:** begin with [Database Generator](database-generator.md), then return to Main.

Calibration and adaptation use experimental information. See [Gradient Cal](gradient-cal.md) and [Transfer Learn](transfer-learn.md) for their inputs and review steps.

## Scope

**AUTHOR TODO:** Add supported instrument models, tested operating systems, the software release number, download link, and a precise explanation of AIDA versus AIDA+ and Full versus Light calling. Do not equate these controls without confirming their relationship.

```{toctree}
:maxdepth: 2
:caption: Getting started

installation
quick-start
input-files
```

```{toctree}
:maxdepth: 2
:caption: Interface tabs

main
advanced
environment-check
database-generator
offline-search
post-run-script
gradient-cal
transfer-learn
run
```

```{toctree}
:maxdepth: 2
:caption: Reference

outputs
paper-workflow
troubleshooting
citation
editing-guide
```
