# Main

Select the database and output location, then configure the experiment before starting method generation.

```{note}
Author draft. Fields marked **AUTHOR TODO** need confirmation against the released AIDA software. Screenshots show the supplied interface; they do not establish universal recommended settings.
```


![AIDA Main tab](images/main.png)

## Step-by-step procedure

1. Have a suitable AIDA database available. See [Database Generator](database-generator.md) if you need to create one.
2. Enter the **Run number**.
3. Use **Browse** beside **Database** to choose the database.
4. Use **Browse** beside **Output** to select the destination.
5. Select the **TMT Plex** and **Run time** that match the intended experiment.
6. Choose the **AIDA+** switch state and **Smart Caller** option.
7. Review the settings and click **Start**.
8. Inspect the execution output and confirm the expected files before using the method.

## Buttons and settings

| Control | Description | Details to complete |
|---|---|---|
| **Run number** | Run identifier. | **AUTHOR TODO:** Define valid values and its effect on filenames or processing. |
| **Database / Browse** | Select the AIDA database. | **AUTHOR TODO:** Document extension, schema and compatibility checks. |
| **Output / Browse** | Select the output location. | **AUTHOR TODO:** Confirm whether this is a folder and explain overwrite behavior. |
| **TMT Plex** | The screenshot offers 18 and 35. | **AUTHOR TODO:** Confirm supported plexes and what each selection changes. |
| **Run time** | The screenshot labels this as maximum acquisition length in minutes. | **AUTHOR TODO:** Define the time origin and treatment of loading, washing and equilibration. |
| **AIDA+** | The interface describes a higher-signal, fuller acquisition mode. | **AUTHOR TODO:** Describe the algorithmic change and when to enable it. |
| **Smart Caller: Full / Light** | Select one of two calling modes. | **AUTHOR TODO:** Explain differences, recommended use and interaction with AIDA+. |
| **Start** | Starts the configured operation. | **AUTHOR TODO:** Confirm precisely what is generated and the success message. |

## Expected output

**AUTHOR TODO:** List method/schedule/log filenames, their destinations and any instrument import step.

## Worked example

**AUTHOR TODO:** Add one real input filename, the settings used, an expected result and a screenshot of successful completion.

## Troubleshooting

**AUTHOR TODO:** Add a verified error message, its cause and recovery steps. See also [Troubleshooting](troubleshooting.md).
