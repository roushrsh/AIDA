
<h1 align="center">AIDA — AI-Driven Acquisition</h1>

<p align="center" > <img width="153" height="102" alt="image" src="https://github.com/user-attachments/assets/393bd92c-a366-411b-9dd3-d1b5ceadb0be" /></p>

AIDA is an automated, AI-driven mass spectrometry acquisition platform designed for deep, accurate, and high-throughput quantitative proteomics. AIDA autonomously controls and optimizes MS1, MS2, and MS3 acquisition in real time, maximizing proteome coverage while leveraging TMT multiplexing to analyze up to 35 samples simultaneously.

+ **Depth and sensitivity**: Adaptive MS1 tiling and intelligent MS2 isolation-window selection prioritize the detection of low-abundance peptides and previously unquantified proteins.

+ **Accurate quantification**: AI-optimized fragmentation and dynamic MS3 ion accumulation maximize TMT reporter-ion signal while minimizing interference and maintaining user-defined signal-to-noise thresholds.

+ **High throughput**: Combining multiplexed peptide identification with TMTpro 18-plex and 35-plex sample multiplexing enables deep proteome characterization of large sample cohorts.

+ **Robustness and adaptability**: Real-time retention-time alignment, mass-accuracy correction, and adaptive acquisition compensate for variations in chromatography and instrument performance.

+ **Flexibility and extensibility**: Custom target databases, adjustable acquisition parameters, and interchangeable prediction inputs lets users tailor AIDA to different sample types and experimental objectives.


AIDA is currently designed for TMT-multiplexed proteomics on compatible Thermo Scientific Orbitrap Tribrid mass spectrometers, using real-time instrument control through the Thermo Fisher Scientific iAPI (https://github.com/thermofisherlsms/iapi).

AIDA can be downloaded from this Github Directory as AIDAv1p0.exe

<h1>Table of Contents</h1>


* [Before you start](#before-you-start)
* [Main](#main)
* [Environment Check](#environment-check)
* [Post Run Script](#post-run-script)
* [Database Generator](#database-generator)
* [Offline search](#offline-search)
* [Gradient Cal](#gradient-cal)
* [Transfer Learn](#transfer-learn)
* [Run](#run)
* [Advanced](#advanced)


<h3>Before you start</h3>
AIDA is written for Windows and requires XCalibur 4.5 or higher, Tune 4.2.4310.9 and iAPI Access. AIDA has been tested on an Intel i9 14900K, results may differ on slower CPU's.\
We have provided sample Cell-line, Plasma and Breast-Tumor-Tissue databases, but users can generate their own using FASTA files or the recommended observed peptide libraries.  (see Database Generator).\
A valid Python executable for the Python-backed tools is needed along with the necessary libraries. (See the Environment Check module.)


<h3>Start the application</h3>
After downloading, launch `AIDAv1p0.exe`. Keep the executable together with its dependency files.


<h2>Main</h2>
The Main tab contains the minimum settings needed to start an acquisition.
<img width="1482" height="1326" alt="image" src="https://github.com/user-attachments/assets/ce845b2b-7aa0-4754-964e-a723b44b3468" />

Options are:
1. If the sample is TMT 18, or TMT 35. 
2. The Run time of the Gradient. 
3. Whether to use the more sensitive AIDA+.
4. The faster (light) or slower (Full) caller.

At the top the user chooses the database they would like to use for real-time acquisition, the output directory for AIDA, and the run number (Recommended to correspond to the XCalibur ID).

From there, the user queues the gradient (See 'SampleAIDAGradient.meth') in XCalibur with their chosen sample in the corresponding well position, and hit "Start" to begin acquisition. This currently has to be performed for each sample seperately.

<h2>Environment Check</h2>

Use this tab to check if all required installations are present. OfflineSearch.dll and search_methods.py come with the AIDA file here and dotnet has to be installed by the user. (https://dotnet.microsoft.com/en-us/download/dotnet/9.0 )
<img width="1075" height="674" alt="image" src="https://github.com/user-attachments/assets/3d6a922e-4d88-41fe-8de0-db62cfa79807" />

Select the Python executable installed which will be used by the AIDA tools.\
Click Check environment.\
If packages are missing, edit the package list if needed and click Install packages.
Installing packages modifies the selected Python environment. Confirm that its path is the intended environment before clicking Install.

<h2>Post Run Script</h2>
<img width="1073" height="671" alt="image" src="https://github.com/user-attachments/assets/a80308f9-1958-46a0-ac3e-dda1226f9339" />

This is the normal downstream step after an AIDA acquisition. It runs post-run protein sieving with mokapot and performs MS3 TMT quantification. \
After an AIDA run, Chopin CSV, MS3Signal CSV, and output-folder fields are automatically filled and it can be run. You will still need to choose the RAW file. 
Otherwise, provide the RAW file, Chopin CSV, MS3Signal CSV, and output folder. The latter three may already be populated after acquisition.\
Enable or disable Run Quantification (MS3 TMT). If quantification is enabled, select the TMT plex and SSN cutoff. Defaults are 180 for TMT18 and 350 for TMT35.\
Choose the Python executable directory location and click Run.\
With quantification disabled, the tab performs the sieving workflow without requiring RAW/MS3Signal input. The results panel reports peptides at 1%, sieved proteins, and proteins above SSN when quantification was run.


<h2>Database Generator</h2>
This tab produces the peptide database consumed by AIDA workflows.

<img width="1467" height="860" alt="image" src="https://github.com/user-attachments/assets/f60c490c-5523-4d84-84b9-260ab42ba8d5" />
<img width="402" height="722" alt="image" src="https://github.com/user-attachments/assets/6c9f734a-2bb9-4d64-84d3-284b4edbf9b0" />

Select peptide/protein text input or FASTA input, then select the TMT label profile. 

Choose:
Full build to generate all selected database-model columns. (recommended)\
Score one model to apply a single selected model/version. (generate single features, which the user will have to merge later)

Full build settings\
Set charge states, precursor mass range, reverse/decoy behavior, and optional methionine oxidation. It is recommended to leave all settings as is and provide only your peptide-protein list.

The model section lets you select:\
Order / retention-time model and its model file (This is provided if transfer learning has occurred).\
FAIMS CV model to predict with.\
Fragment-intensity model to predict with. \
Charge prediction. (not used by AIDA V1 in real time)\ 
Flyability prediction. (not used by AIDA V1 in real time)\ 
Note: FAIMS CV and Fragment intensity use V1 by default. V2-Beta is available as an experimental alternative. When Fragment intensity is V1, Charge prediction and Flyability appear directly below it. Selecting Fragment intensity V2-Beta expands the section to show Collision, Energy, Analyzer, and Collision-energy sweep controls.\
For V2-Beta Fragment intensity:\
Select CID or HCD and set the collision energy.\
Select IonTrap, Orbitrap, or Astral as analyzer. Astral forces HCD.\
Enable the energy sweep only when a collision-energy sweep is intended.\

Score one model settings:\
Choose FAIMS, Fragment, Order, Charge, or Fly, then choose the applicable version. The Collision/Energy controls appear only for Fragment V2-Beta scoring.

Choose an output database filename, select the Python executable, choose whether to use GPU, then click Generate database. The output panel reports peptide and database-entry counts, and the log records the invoked workflow.

<h2>Offline search</h2>
Offline search runs the supporting search workflow on a RAW file and reports peptide/protein counts. Note: this is only recommended if the real-time search files are lost, otherwise use the Post Run Script.
<img width="2870" height="1697" alt="image" src="https://github.com/user-attachments/assets/b19bcea7-b2eb-4e6b-8e07-c46ce59035fe" />

Choose the RAW file.\
Choose the database: either a CSV/TSV database or a packed database directory.\
Select a writable output root.\

Select the search mode:\
DDA for DDA search.\
DIA-Faster (beta) for the faster DIA mode.\
DIA (beta) for the broader DIA mode.\
For DIA, set Top MS1 peaks. `1` uses only the most intense precursor candidate per isolation window; higher values consider more candidates and take longer.\
Leave Tight MS2 ppm off for the default ±12 ppm search window; enable it for ±6 ppm.\
Optionally enable Attach MS3 quant, then provide the MS3Signal CSV, TMT plex, and SSN cutoff. Note, similar to other search engines, using the same database is paramount for obtaining reproducible PSM matching MS3 results.\
Select the Python location and click Run search.\
The result panel reports unique peptides, unique proteins, sieved proteins, and—when MS3 quantification is attached—proteins above the SSN cutoff. 


<h2>Gradient Cal</h2>
<img width="1179" height="673" alt="image" src="https://github.com/user-attachments/assets/a42def46-6c20-4502-8a69-f2a9d765a461" />

Gradient Cal proposes a revised `%B` program using a target database and a calibration run.\
Step 1 — Target database: select the database, set the retention-order column (default column 4), and click Read. The app reports unique peptide count and median order.\
Step 2 — Coverage target: select the desired order/coverage target. The interface shows the corresponding fraction of the database.\
Step 3 — Calibration run: select the calibration Chopin CSV and enter the gradient program used for that run as Time (min) / %B points.\
Click Optimize gradient.\
The result side displays fit quality (R²), coverage, CV, the calibration line, a proposed gradient table, and a chart comparing the original and proposed programs. Review the proposed program against instrument, column, and solvent constraints before populating the XCalibur .meth method with the new proposed gradient.

<h2>Transfer Learn</h2>
<img width="1185" height="672" alt="image" src="https://github.com/user-attachments/assets/39769ce6-50e0-4d9a-bc83-41a1890e434c" />

Transfer Learn adapts the retention-time model to your LC column using observations from multiple runs.\
Provide a runs CSV containing `peptide`, `time`, and `run_id`, with at least two runs.\
Select the base retention-time model.\
Choose an output folder.\
Choose the held-out run. `auto` selects the largest suitable run; the held-out run is the honest evaluation set.\
Set the number of epochs and minimum shared peptides.\
Select a Python environment with the required GPU/Torch dependencies and click Run adaptation.\
The output folder receives the adapted model and plots are generated. Use the old-vs-new comparison on the held-out run, rather than training loss alone, to decide whether the adaptation is beneficial.\

<h2>Run</h2>
<img width="1482" height="867" alt="image" src="https://github.com/user-attachments/assets/743787d7-516d-4fb0-a97c-2f8136df1e2c" />

The Run tab is the acquisition monitor. It displays startup output and then a concise set of live metrics, including current order, total proteins, and unique proteins with MS3 evidence. The full engine log is written to a timestamped file in the application log directory.\

<h3>**Recommended first workflow**</h3>
For a first test, we recommend preparing a TMTPro Zero labeled standard Hela sample as described in the AIDA Manuscript (PMID) and running with our cell line database using the default settings post gradient adjustment.
At completion, open Post Run Script.


<h2>Advanced</h2>
Advanced controls are initially locked to protect method defaults. Click an individual lock to edit a row, or use "Unlock all" when deliberately configuring a custom method.

<img width="1475" height="870" alt="image" src="https://github.com/user-attachments/assets/95958924-80d4-4792-9d37-35013c7b3a4a" />
<img width="725" height="72" alt="image" src="https://github.com/user-attachments/assets/069f509b-08f6-4935-98e2-32b3ceba858b" />

FAIMS CVs: the three compensation voltages used by the method. Defaults are `-40`, `-55`, and `-70`.\
MS2 scans per CV: scheduling budget for each FAIMS CV.\
MSX per MS1: number of MSX scans associated with each MS1 event.\
Use GPU: enables GPU use where supported. Default is off.\
Starting order (mid-run): starting elution-order position from `0` to `1`; normally leave at `0`.\
Target MS3 ions and MS3 ion cutoff: ion targets used for MS3 calling.\ 
MS3 SSN target: signal-to-noise criterion for MS3 calls.\
Min/Max MS3 time and round-2 max time: injection-time bounds in milliseconds. \
MS3 resolution: 50K, 75K, or 90K.\
SPS: number of synchronous precursor selection fragments when original fragments are used. \
Call round 2 scans: enables the second-round scan behavior. \
Minimum for overs: preserves the minimum-fill behavior for overs.\
Use original MS3 fragments: requests the real-time energy observed original MS3 fragment behavior.\
Force analyzer cycle time: applies a fixed analyzer-cycle-time behavior. \
Plasma mode: allows longer, approximately two-second MS3 injection behavior. \
Wide MS2 ppm: uses ±12 ppm rather than the ±6 ppm setting. \
Predicted cycle times: select which of Slowest, Slow, Normal, Fast, and Fastest predicted cycle times can be considered. Normal, Fast, and Fastest are enabled by default.


