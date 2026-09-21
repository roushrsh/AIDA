# Output files

Use this page to connect files between workflow steps. Exact names and schemas require confirmation.

| Producing step | Output filename | Contents | Next consumer |
|---|---|---|---|
| Database Generator | **AUTHOR TODO** | Peptide database and predictions | Main and relevant downstream steps |
| Main / Start | **AUTHOR TODO** | Generated acquisition artifacts | **AUTHOR TODO:** instrument import |
| Offline Search | **AUTHOR TODO** | Search results | **AUTHOR TODO:** post-run/calibration steps |
| Post Run Script | **AUTHOR TODO** | Post-run quantitative outputs | **AUTHOR TODO** |
| Gradient Cal | **AUTHOR TODO** | Exported gradient table | LC method configuration |
| Transfer Learn | **AUTHOR TODO** | Adapted models and evaluation | **AUTHOR TODO:** reuse procedure |
| Run | **AUTHOR TODO** | Execution log, if saved | Troubleshooting |

## Completion and reruns

**AUTHOR TODO:** Describe how to distinguish complete outputs from interrupted ones. State whether reruns overwrite, append, resume or create new files. Explain which artifacts should be retained for reproducibility.
