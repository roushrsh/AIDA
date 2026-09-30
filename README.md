
<h1 align="center">AIDA — AI-Driven Acquisition</h1>

<p align="center" > <img width="153" height="102" alt="image" src="https://github.com/user-attachments/assets/393bd92c-a366-411b-9dd3-d1b5ceadb0be" /></p>

AIDA is an automated, AI-driven mass spectrometry acquisition platform designed for deep, accurate, and high-throughput quantitative proteomics. AIDA autonomously controls and optimizes MS1, MS2, and MS3 acquisition in real time, maximizing proteome coverage while leveraging TMT multiplexing to analyze up to 35 samples simultaneously.

+ **Depth and sensitivity**: Adaptive MS1 tiling and intelligent MS2 isolation-window selection prioritize the detection of low-abundance peptides and previously unquantified proteins.

+ **Accurate quantification**: AI-optimized fragmentation and dynamic MS3 ion accumulation maximize TMT reporter-ion signal while minimizing interference and maintaining user-defined signal-to-noise thresholds.

+ **High throughput**: Combining multiplexed peptide identification with TMTpro 18-plex and 35-plex sample multiplexing enables deep proteome characterization of large sample cohorts.

+ **Robustness and adaptability**: Real-time retention-time alignment, mass-accuracy correction, and adaptive acquisition compensate for variations in chromatography and instrument performance.

+ **Flexibility and extensibility**: Custom target databases, adjustable acquisition parameters, and interchangeable prediction inputs lets users tailor AIDA to different sample types and experimental objectives.

AIDA can be operated through its graphical user interface. In a standard workflow, the user provides a target peptide/protein database and defines the acquisition conditions. AIDA then performs real-time target prioritization, adaptive precursor isolation, peptide identification, and MS3-based quantitative acquisition.


## Obtaining AIDA

To request the most up-to-date available build of AIDA, please email [whaas@mgh.harvard.edu](mailto:whaas@mgh.harvard.edu) or [shajizadeh@mgh.harvard.edu](mailto:shajizadeh@mgh.harvard.edu) with the subject line **"AIDA Software"**.
Please include your institution (for example, MIT) and the mass spectrometer model on which AIDA will be used. A Recipient Agreement must be completed and signed before the software can be provided or used.
AIDA is currently designed for TMT-multiplexed proteomics on compatible Thermo Scientific Orbitrap Tribrid mass spectrometers, using real-time instrument control through the Thermo Fisher Scientific iAPI (https://github.com/thermofisherlsms/iapi).


<h1>Table of Contents</h1>


* [Before you start](#before-you-start)
* [Main](#main)
* [Environment Check](#environment-check)
* [Post Run Script](#post-run-script)
* [Database Generator](#database-generator)
* [Offline search](#offline-search)
* [Gradient Calibration](#gradient-calibration)
* [Transfer Learn](#transfer-learn)
* [Run](#run)
* [Advanced Options](#advanced-options)
* [Output Files](#output-files)
* [First AIDA Run: Workflow Overview](#first-aida-run-workflow-overview)
* [Running AIDA](#running-aida)
* [Target Databases](#target-databases)
* [Standardized AIDA Benchmark](#standardized-aida-benchmark)


<h3>Before you start</h3>

AIDA performs real-time instrument control and therefore requires a compatible mass spectrometer, instrument-control software, and sufficiently fast computational hardware.

### Instrument requirements

The current AIDA implementation supports Thermo Fisher Scientific Tribrid mass spectrometers capable of the required real-time MS3 acquisition workflow. AIDA has been developed and extensively evaluated using the Orbitrap Eclipse.

AIDA requires:

- Thermo Fisher Scientific iAPI for real-time instrument control
- Thermo Fisher Scientific Xcalibur
- Thermo Fisher Scientific Tune
- A compatible FAIMS interface when FAIMS-based acquisition is used
- A Windows workstation connected to the mass spectrometer

AIDA v1.0 was developed using Orbitrap Eclipse Tune Application **4.2.4310.9**. Use of substantially different instrument-control software versions should be validated before routine acquisition.

### Computational requirements

AIDA performs model inference and acquisition decisions while the mass spectrometer is operating. The real-time processing workflow is therefore sensitive to computational latency.

AIDA has been successfully tested using:

- Intel Core i9-13900K and i9-14900K CPUs
- NVIDIA RTX 3080 and RTX 4090 GPUs

GPU acceleration is supported but is not required for all AIDA acquisition modes. CPU-only operation is supported for the standard acquisition workflow.

The maximum acceptable real-time processing latency is approximately **100 ms**. Systems with substantially slower processing may reduce acquisition efficiency.

### Software environment

Some AIDA utilities use Python-based machine-learning packages. The exact Python, CUDA, PyTorch, and TensorFlow requirements depend on the AIDA build being used.

Before beginning an acquisition, use the **Environment Check** tab to verify that the required software dependencies and hardware interfaces are available.




<h2>Main</h2>
The **Main** tab contains the settings required for a standard AIDA acquisition.
<img width="1665" height="1367" alt="image" src="https://github.com/user-attachments/assets/a9358b7b-a37b-475a-a6bd-25f1412014c7" />


### Run Number

**Run Number** assigns a unique identifier to the acquisition and its associated output files. Use a different run number for each acquisition.

### Database

Select the AIDA target database to be used for the acquisition.

AIDA is a global targeted proteomics method. The database defines the peptide and protein targets that AIDA considers during real-time acquisition. The database can be generated using the **Database Generator** tab or obtained from the provided AIDA reference databases.

### Output

Select the folder in which AIDA acquisition files will be written.

We recommend using a separate output folder for each experiment or sample set.

### TMT Plex

Select the TMT multiplexing format used for the sample:

- **18**: TMT18
- **35**: TMT35

This setting controls acquisition parameters that depend on the reporter-ion multiplexing chemistry, including MS3 acquisition and resolving-power requirements.

### Run Time

**Run Time** defines the duration, in minutes, over which AIDA performs active real-time data acquisition.

This value should correspond to the analytical portion of the LC gradient during which peptide acquisition is desired.

### AIDA+

The **AIDA+** toggle enables the AIDA+ acquisition strategy.

AIDA+ optimizes MS2 fragment-ion selection to increase MS3 reporter-ion signal and thereby increase proteome coverage and quantitative sensitivity. Standard AIDA places greater emphasis on minimizing quantitative interference, whereas AIDA+ prioritizes reporter-ion signal and acquisition sensitivity.

The setting used should therefore be selected according to the goals of the experiment.

### Smart Caller: Full and Fast

The **Smart Caller** setting controls the algorithm used to select MS2 precursor isolation windows.

**Fast** uses a streamlined set of acquisition features to rapidly rank candidate MS2 windows.

**Full** performs additional feature extraction and evaluates candidate windows using the complete AIDA decision framework before dynamically selecting the highest-value non-overlapping windows.

Full is recommended for routine AIDA acquisition when sufficient computational performance is available. Fast provides a lower-computation alternative.

Changing advanced acquisition parameters is not required for a standard run. Additional controls are available under **Advanced Options**.




<h2>Environment Check</h2>

The **Environment Check** tab verifies that the software components required by AIDA are available before an acquisition is started.

<img width="2357" height="1747" alt="image" src="https://github.com/user-attachments/assets/f4fdc7e4-ab8a-4c88-b37d-0ebe0d0f7f88" />

Select the Python executable installed which will be used by the AIDA tools.

Click Check environment.

If packages are missing, edit the package list if needed and click Install packages.
Installing packages modifies the selected Python environment. Confirm that its path is the intended environment before clicking Install.

We recommend running Environment Check after:
- Installing AIDA for the first time
- Updating AIDA
- Updating Python or machine-learning packages
- Updating GPU drivers or CUDA
- Updating Xcalibur, Tune, or iAPI components
- Moving AIDA to a new acquisition computer

The check evaluates the local software environment and reports whether required components can be accessed.
A successful Environment Check indicates that the AIDA software environment is configured correctly. It does **not** independently verify LC performance, instrument calibration, or sample preparation.

The required AIDA `.dll` and `.py` files are provided with the AIDA software distribution.

.NET must be installed separately by the user. (https://dotnet.microsoft.com/en-us/download/dotnet/9.0 ) GPU-accelerated utilities additionally require compatible CUDA, cuDNN, PyTorch, and/or TensorFlow installations appropriate for the AIDA build being used.

For reference, our tested environments included Python 3.8.10 with PyTorch 2.4.1+cu124/CUDA 12.4 for PyTorch-based GPU workflows, and TensorFlow GPU 2.7.0 with CUDA 11.2/cuDNN 8.x for TensorFlow-based workflows.


<h2>Post Run Script</h2>
<img width="1073" height="671" alt="image" src="https://github.com/user-attachments/assets/a80308f9-1958-46a0-ac3e-dda1226f9339" />

This is the normal downstream step after an AIDA acquisition. It runs post-run protein sieving with mokapot and performs MS3 TMT quantification. 

The standard post-run workflow uses the acquisition files generated by AIDA, including:

- `AIDA*.csv` — real-time peptide identification and scoring information
- `MS3SignalAIDA*.csv` — quantitative MS3 reporter-ion measurements

After an AIDA-run, output-folder fields are automatically filled. Users are still required to select the new RAW file. 

Otherwise, provide the RAW file, AIDA.CSV, MS3SignalAIDA.CSV, and output folder. The latter three may already be populated after acquisition.

Enable or disable Run Quantification (MS3 TMT). If quantification is enabled, select the TMT plex and SSN cutoff. Defaults are 180 for TMT18 and 350 for TMT35.

Choose the Python executable directory location and click Run.

With quantification disabled, the tab performs the sieving workflow without requiring RAW/MS3Signal input. The results panel reports peptides at 1%, sieved proteins, and proteins above SSN when quantification was run.


The post-run workflow:

1. Filters peptide-spectrum assignments
2. Applies peptide-level confidence filtering
3. Associates identified peptides with quantitative MS3 spectra
4. Reprocesses MS3 reporter-ion information
5. Aggregates peptide measurements
6. Generates protein-level quantitative output

Protein-level filtering uses a target-decoy strategy and is performed using the picked-protein approach.

The Post Run Script generates three primary processed outputs:

#### `RunID_FinalProteinOutput.csv`

Contains protein-level identification and filtering information for the acquisition.

#### `RunID_PeptideQuant.csv`

Contains peptide-level quantitative measurements and associated peptide/protein annotations.

Use this file when peptide-level information or individual peptide behavior is required.

#### `RunID_ProteinQuant.csv`

Contains the final protein-level quantitative matrix generated from the peptide measurements.

**For most downstream biological analyses, `RunID_FinalProteinOutput.csv` is the recommended starting file.**




<h2>Database Generator</h2>

The Database Generator converts a peptide/protein search space into the target-database format required for AIDA acquisition.

<img width="2130" height="1762" alt="image" src="https://github.com/user-attachments/assets/4a78cb10-3a6d-40a5-9a8f-70dc43f48519" />

<img width="400" height="700" alt="image" src="https://github.com/user-attachments/assets/016fcd89-4dca-4fd3-a1a0-5315dfb4b4bd" />


Select peptide/protein text input or FASTA input, then select the TMT label profile. 

Choose:

+ Full build to generate all selected database-model columns. (recommended)

+ Score one model to apply a single selected model/version. (generate single features, which the user will have to merge later)

**Full build settings:**

Set charge states, precursor mass range, reverse/decoy behavior, and optional methionine oxidation. It is recommended to leave all settings as is and provide only your peptide-protein list.

The model section lets you select:

+ Order / retention-time model and its model file (This is provided if transfer learning has occurred).

+ FAIMS CV model to predict with.

+ Fragment-intensity model to predict with. 


Score one model settings:

Choose FAIMS, Fragment, or Order, then choose the applicable model version.

The Score one model workflow predicts and outputs a file containing the selected variable. The user can then append this feature to an existing AIDA database when developing a customized target database.

Choose an output database filename, select the Python executable, choose whether to use GPU, then click Generate database. The output panel reports peptide and database-entry counts, and the log records the invoked workflow.

The generated database contains the peptide properties and model predictions required by AIDA for real-time targeting, including peptide mass, predicted chromatographic behavior, ion-mobility information where applicable, and predicted fragment-ion information.
After generating a new database, perform **Gradient Calibration** before using it for routine acquisition.

<h2>Offline search</h2>
Offline search runs the supporting search workflow on a RAW file and reports peptide/protein counts. Note: this is only recommended if the real-time search files are lost, otherwise use the Post Run Script.
<img width="2870" height="1697" alt="image" src="https://github.com/user-attachments/assets/b19bcea7-b2eb-4e6b-8e07-c46ce59035fe" />

+ Choose the RAW file.

+ Choose the database: either a CSV/TSV database or a previously packed database's directory. AIDA generates a 'packed' or indexed version of each database the first time it used for offline searches. They can be re-used to save on packing time.

+ Select an output directory.

+ Select the search mode:

+ DDA for DDA search.

+ Leave Tight MS2 ppm off for the default ±12 ppm search window; enable it for ±6 ppm.

+ Optionally enable Attach MS3 quant, then provide the MS3Signal CSV, TMT plex, and SSN cutoff. Note, similar to other search engines, using the same database is paramount for obtaining reproducible PSM matching MS3 results.

+ Select the Python location and click Run search.

The result panel reports unique peptides, unique proteins, sieved proteins, and—when MS3 quantification is attached—proteins above the SSN cutoff. 

For routine analysis, use the real-time AIDA output followed by the **Post Run Script**. Offline Search should be considered a reanalysis and troubleshooting utility rather than a required step in the normal workflow.


<h2>Gradient Calibration</h2>

AIDA predicts peptide chromatographic behavior primarily as an elution order rather than relying on a fixed retention time. The **Gradient Calibration** tool maps these predictions onto the chromatography used on the local LC-MS system.

<img width="1782" height="1365" alt="image" src="https://github.com/user-attachments/assets/641c8fb5-b0c5-491b-9f80-c9c666c7815e" />

Gradient Cal proposes a revised `%B` program using a target database and a calibration run.

+ Step 1 — Target database: select the database, set the retention-order column (default column 4), and click Read. The app reports unique peptide count and the median predicted peptide order from the corresponding database.

+ Step 2 — Coverage target: select the desired order/coverage of target database. The interface shows the corresponding fraction of the database.

+ Step 3 — Calibration run: select the calibration AIDA*.CSV and enter the gradient program used for that run as Time (min) / %B points.

Click Optimize gradient.

The result side displays fit quality (R²), coverage, CV, the calibration line, a proposed gradient table, and a chart comparing the original and proposed programs. Review the proposed program against instrument, column, and solvent constraints before populating the XCalibur .meth method with the new proposed gradient.


Gradient calibration does not require retraining the underlying retention-time model. Instead, it uses the relationship between predicted peptide elution order and experimentally observed retention time to propose an LC `%B` program that better distributes the target peptide population across the analytical gradient.
Minor run-to-run retention-time deviations are handled automatically by AIDA during real-time acquisition and do not normally require recalibration.


<h2>Transfer Learn</h2>

The **Transfer Learn** tool adapts an AIDA prediction model to chromatographic conditions that differ substantially from those represented in the original training data.
Transfer learning is generally **not required** for routine differences in gradient length or small retention-time shifts. These differences are handled by Gradient Calibration and by AIDA's real-time retention-time adjustment.

<img width="1790" height="1367" alt="image" src="https://github.com/user-attachments/assets/dbbca53c-3840-41c5-baef-2932ca4cc0f0" />

Transfer Learn adapts the retention-time model to your LC column using observations from multiple runs.

Provide a runs CSV containing `peptide`, `time`, and `run_id`, with at least two runs.

Select the base retention-time model.

Choose an output folder.

Choose the held-out run. `auto` selects the largest suitable run; the held-out run is the honest evaluation set.\
Set the number of epochs and minimum shared peptides.

Select a Python environment with the required GPU/Torch dependencies and click Run adaptation.

The output folder receives the adapted model and plots are generated. Use the old-vs-new comparison on the held-out run, rather than training loss alone, to decide whether the adaptation is beneficial.

After transfer learning, use the adapted model when generating the corresponding AIDA target database, followed by Gradient Calibration for the final acquisition gradient.

<h2>Run</h2>
<img width="1500" height="1300" alt="image" src="https://github.com/user-attachments/assets/044e3a55-f910-4354-bc46-3008cc136c53" />

<img width="1500" height="1300" alt="image" src="https://github.com/user-attachments/assets/4332b817-42d6-47c9-8fcb-a615dd956715" />

The Run tab is the acquisition monitor. It displays startup output and then a concise set of live metrics, including current order, total proteins, and unique proteins with MS3 evidence. The full engine log is written to a timestamped file in the application log directory.


<h2>Advanced Options</h2>
The default AIDA settings are intended to provide robust performance for the sample types and acquisition configurations evaluated during development. Most users should begin with the defaults.
Advanced settings can be modified to optimize acquisition for different sample amounts, chromatographic gradients, TMT plexes, or sample dynamic ranges.
Advanced controls are initially locked to protect method defaults. Click an individual lock to edit a row, or use "Unlock all" when deliberately configuring a custom method.

<img width="1530" height="1670" alt="image" src="https://github.com/user-attachments/assets/5445dedb-c903-41a9-b2aa-f41975a522b9" />


+ FAIMS CVs:

Defines the FAIMS compensation voltages used during acquisition.
AIDA cycles through three CV settings. The standard workflows used in the accompanying study used:

`-40 V, -55 V, -70 V`

Alternative CV combinations can be used but should be validated for the sample type and FAIMS device being used.



+ MS2 scans per CV: Scheduling budget for each FAIMS CV.
Defines the number of MS2 acquisition events allocated to each FAIMS CV cycle.


+ MSX per MS1: Number of MSX scans associated with each MS1 event.
Defines the number of multiplexed MS2 discovery scans acquired during otherwise unused processing time between AIDA-controlled acquisition events.
On slower systems, up to two MSX scans can increase duty-cycle utilization.


+ Use GPU: enables GPU use where supported. Default is off.
Enables GPU acceleration for supported AIDA model inference and MS2 window-selection operations. GPU acceleration can reduce real-time processing latency but is not required.

+ Starting order (mid-run): starting elution-order position from `0` to `1`; normally leave at `0`. This is only if your sample for some reason was interrupted and you know the elution point to start the acquisition at. 

+ Target MS3 ions and MS3 ion cutoff: The minimum Ion targets used for MS3 calling.
Higher values increase quantitative signal but may increase acquisition time.

+ MS3 SSN target: Minimum Signal-to-noise criterion for MS3 calls.
Higher values increase quantitative signal but may increase acquisition time.

+ Min/Max MS3 time and round-2 max time: injection-time bounds in milliseconds.
Increasing these values can improve reporter-ion signal for low-abundance peptides at the cost of acquisition speed.

+ MS3 resolution: 50K, 75K, or 90K. Defines Orbitrap resolving power for MS3 reporter-ion acquisition.
The higher resolution used for TMT35 is required to resolve the smaller reporter-ion mass differences of the expanded plex.

+ SPS: number of synchronous precursor selection fragments when original fragments are used. 
Under normal AIDA operation, fragment selection is optimized dynamically and this setting is ignored.

+ Call round 2 scans: enables the second-round scan behavior. 
Enables secondary salvage MS3 acquisition for peptides that do not reach the required quantitative signal during the first MS3 event.

+ Minimum for overs: preserves the minimum-fill behavior for overs.
Adjusts the threshold used to determine whether a salvage MS3 scan should be triggered. This option is normally used together with **Call Round 2 Scans**.

+ Use original MS3 fragments: requests the real-time energy observed original MS3 fragment behavior.
Disables AIDA's optimized MS3 fragment-selection strategy and instead selects the most intense observed MS2 fragment ions.

+ Force analyzer cycle time: applies a fixed analyzer-cycle-time behavior. 
Forces the initial MS3 acquisition to use the analyzer-cycle timing rather than the complete AIDA-predicted accumulation time. 

+ Plasma mode: allows longer, approximately two-second MS3 injection behavior. This option should be selected when analyzing plasma proteomics samples.

+ Wide MS2 ppm: uses ±12 ppm rather than the ±6 ppm setting. Experimental setting for when an analyzer is not properly calibrated, not recommended.

+ Predicted cycle times: select which of Slowest, Slow, Normal, Fast, and Fastest predicted cycle times can be considered. Normal, Fast, and Fastest are enabled by default. These are calculated as the 1 or 2 standard deviations below or above the predicted ion injection time to achieve the target number of ions, where slowest is 2 SD above and Fastest is 2 SD below.


<h2>Output files</h2>
When MS3 quantification is enabled, the Post Run Script generates three primary processed output files:

1. RunID_FinalProteinOutput.csv
2. RunID_PeptideQuant.csv
3. RunID_ProteinQuant.csv

They share 40 columns in common (74 if TMT35)\
These are:

1. Protein - The Protein name (1)
2. SSNc - The Sum Signal To Noise For the Protein (1) 
3. 126 to 135n - The Intensity in the TMT Channels (18 or 35)
4. 126SN to 135nSN - The Signal To Noise in each TMT Channel (18 or 35)
5. MS3IonSum - Total cumulative TMT reporter-ion signal intensity (ions/ms) (1)
6. MS3TotalCurr - Total accumulated reporter-ion count, calculated as MS3IonSum × MS3IIT (1)

Exclusive to the PeptideQuant.csv are:

7. Peptide - The Peptide ID
8. MS1 ID - The Corresponding MS1 the Peptide was found
9. LinkedMS2 ID - The MS2 Scan the Peptide was found at
10. MS3 Master Scan - the ID from which the final MS3 was called from. (This is because round 2 MS3s scans are called from the previous MS3)
11. MS3 ID - The original MS3 ID for the first peptide
12. Round - Number of rounds of MS3 called on the Peptide
13. MS3IIT - Ion Injection Time for the MS3
14. massesChosen - Real time observed fragments which would have been chosen for MS3 if original fragments are set to true, otherwise fragments based on the database provided are used and this column can be ignored.
15. ifEnoughStatus - If AIDA determined it accumulated enough signal to pass SSN thresholds. 


<h2>First AIDA Run: Workflow Overview</h2>

For a new AIDA installation, we recommend completing the following workflow before analyzing experimental samples:

1. **Run Environment Check** to confirm that the required software, models, and instrument-control components are available.
2. **Select or generate an AIDA target database.**
3. Configure the acquisition in the **Main** tab.
4. Load the provided `SampleAIDAGradient.meth` method in Xcalibur.
5. Perform an initial AIDA calibration/benchmark run.
6. Process the run using the **Post Run Script**.
7. Use the resulting `AIDA*.CSV` with **Gradient Calibration** to optimize the LC `%B` program for the local chromatography.
8. Update the Xcalibur method with the proposed gradient.
9. Perform the standardized AIDA HeLa benchmark using the optimized gradient.
10. Inspect the resulting peptide- and protein-level outputs and confirm that system performance is within the expected range.

For routine use after the system has been validated, most acquisitions require only the **Main** and **Post Run Script** tabs.


<h2>Running AIDA</h2>

Before starting AIDA, confirm that:

1. Environment Check completes successfully.
2. The correct target database has been selected.
3. The correct output folder and Run Number have been entered.
4. TMT plex, acquisition time, and acquisition mode are correct.
5. The corresponding LC-MS method is queued in Xcalibur.

A sample AIDA instrument method, `SampleAIDAGradient.meth`, is provided with the repository as a starting point.

During AIDA acquisition, the instrument method itself performs only the minimal background acquisition required to maintain instrument operation. AIDA controls the analytical MS1, MS2, and MS3 scans through the Thermo Fisher Scientific iAPI.

For the methods used in the accompanying study, AIDA-controlled acquisition begins approximately **2 minutes after the LC-MS run begins**.

Start the LC-MS run in Xcalibur and then press **Start** in AIDA.

Once started, AIDA performs real-time acquisition autonomously. During the run, AIDA continuously updates peptide retention-time estimates, evaluates MS1 precursor signals, selects MS2 isolation windows, annotates peptide spectra, triggers quantitative MS3 acquisition, and removes sufficiently quantified proteins from further targeting.

Do not close AIDA or modify the active target database while an acquisition is running.

<h2>Target Databases</h2>

AIDA requires a peptide/protein target database for acquisition.

For the studies accompanying AIDA, global target databases were constructed by combining peptides and proteins previously identified during LC acquisitions of various samples.

The reference databases used in the study contained:

| Sample type | Peptides | Proteins |
|---|---:|---:|
| Human cell lines | 378,209 | 20,815 |
| Primary breast tumor tissue | 316,558 | 11,646 |
| Undepleted human blood plasma | 26,580 | 5,932 |

The corresponding reference databases are:

- `AIDACellLineDB.tsv`
- `AIDABreastTumorTissueDB.tsv`
- `AIDABloodPlasmaDB.tsv`

Users are not restricted to these databases. AIDA target databases for other sample types can be generated using the **Database Generator** tool described below.


<h2>Acquisition-Level Output Files</h2>


In addition to the final processed files described above, AIDA generates detailed acquisition-level output files.

These files are primarily intended for quality control and method development.
### `AIDA*.csv`

This file records real-time peptide assignment and scoring information.

Important fields include:

+ MS2 ID: MS2 scan identifier
+ cleanedEnds: Amino acid sequence of the peptide.
+ Reference: UniProt database entry string formatted as db|Accession|Name (separating Swiss-Prot sp or TrEMBL tr designations, UniProt accession number, and protein name via vertical bars).
+ Charge: Peptide ionization charge state.
+ DBMass: Theoretical mass of the peptide (Da).
+ AdjustedMass: Corrected mass deviation of the peptide ion (ppm).
+ OriginalMass: Uncorrected raw mass deviation of the peptide ion (ppm).
+ Order: Predicted peptide elution order, dynamically updated in real-time.
+ peptidesOrder: Baseline predicted peptide elution order derived from the database.
+ PredScore: Real-time scoring metric for the peptide-spectrum match.
+ MS1 ID: MS1 scan identifier.
+ Time: Retention time in minutes.
+ Cosine: Spectral cosine similarity score for the peptide-spectrum match.
+ Hit: Total number of predicted fragment ions observed in the MS2 spectrum.
+ NumberPossible: Theoretical total number of fragment ions predicted to be detectable.
+ CV: Active FAIMS Compensation Voltage setting.
+ Analyzer: Specific mass analyzer used for the scan acquisition.
+ Truth: Target-decoy annotation indicating a match to the forward or reversed database component.
+ TotalIntOffFrags: Cumulative signal intensity of all MS2 fragment ions assigned to the target peptide.
+ MS2IntSum: Total integrated signal intensity across the entire MS2 spectrum.
+ dCn: Delta score measuring the difference in "Hit" count between the top-scoring peptide match and the next best candidate.

MS2Called-AIDA*.csv

This file describes the MS2 isolation windows selected during acquisition.

Important fields include:

+ MS1 ID:  MS1 scan identifier.
+ ScanPoint: Center m/z of the MS2 isolation window.
+ IT : ion accumulation time
+ IsoSize : Width of the isolation window (m/z).
+ Analyzer: Specific mass analyzer used for detection.
+ MS1 Score : Predictive metric reflecting the statistical likelihood of identifying a novel protein from the selected isolation window.
+ Resolution:  Resolving power configuration used for MS2 data acquisition.

MS3SignalAIDA*.csv

This file contains quantitative information for acquired MS3 spectra.

Important fields include:

+ MS1 ID:  MS1 scan identifier.
+ MS2 ID:  MS2 scan identifier.
+ MS3 ID:  MS3 scan identifier.
+ Peptide:  Amino acid sequence of the peptide.
+ Protein:  UniProt database entry string formatted as db|Accession|Name (separating Swiss-Prot sp or TrEMBL tr designations, UniProt accession number, and protein name via vertical bars).
+ TMT reporter-ion intensities:  Signal intensity in the respective TMT reporter ion channel, measured in ions per millisecond (ions/ms).
+ MS3IonSum:  Total cumulative reporter ion signal intensity (ions/ms).MS3IIT — MS3 ion injection time
+ MS3IIT:  MS3 ion injection/accumulation time in milliseconds (ms).
+ MS3TotalCurr: Total accumulated ion count, calculated as MS3IonSum x MS3IIT.
+ massesChosen : Specific MS2 fragment ion mass-to-charge ratios ($m/z$) isolated for the MS3 event.
+ Round : Indicates acquisition priority tier: baseline initial MS3 scan (1) or secondary salvage MS3 scan (2).


These acquisition-level files should be retained together with the Thermo `.raw` file for reproducibility and future reanalysis.




<h2>Standardized AIDA Benchmark</h2>

Before analyzing experimental samples on a new AIDA installation, we recommend verifying system performance using the standardized AIDA HeLa benchmark.

The benchmark uses a commercially available HeLa protein digest standard:

**Pierce HeLa Protein Digest Standard, catalog 88328**

The digest is labeled using **TMTpro Zero** and analyzed using the standardized AIDA acquisition conditions provided with the reference dataset.

The benchmark is intended to verify that:

- AIDA communicates correctly with the mass spectrometer
- Real-time acquisition proceeds normally
- Peptide identification and MS3 acquisition are functioning
- Post-run processing completes successfully
- Proteome coverage and acquisition behavior are within the expected range

---

# Experimental and Beta Features

> **The features in this section are under active development and were not required for the AIDA workflows described in the accompanying manuscript. They are provided for testing and method-development purposes and may change between software builds.**

The stable AIDA workflow described above should be used for reproducing the experiments reported in the manuscript.

## Offline Search

AIDA includes experimental utilities for evaluating DIA-style offline search workflows.

DIA-Faster (beta) for the faster DIA mode.
DIA (beta) for the broader DIA mode.
For DIA, set Top MS1 peaks. `1` uses only the most intense precursor candidate per isolation window; higher values consider more candidates and take longer.

These functions are under active development and are not part of the validated AIDA acquisition and analysis workflow described in the accompanying manuscript.
Results generated using these modes should therefore be independently validated before biological interpretation.

## Database Generator

Charge prediction. (not used by AIDA V1 in real time)

Flyability prediction. (not used by AIDA V1 in real time)

Note: FAIMS CV and Fragment intensity use V1 by default. V2-Beta is available as an experimental alternative. When Fragment intensity is V1, Charge prediction and Flyability appear directly below it. Selecting Fragment intensity V2-Beta expands the section to show Collision Energy, Analyzer, and Collision-energy sweep controls.

For V2-Beta Fragment intensity:

Select CID or HCD and set the collision energy.
Select IonTrap, Orbitrap, or Astral as analyzer. Astral forces HCD.
Enable the energy sweep only when a collision-energy sweep is intended.

Fragment Prediction V2 is not required for the validated AIDA v1.0 workflow described in the accompanying manuscript.
The model architecture, inputs, and output format may change in future builds.
