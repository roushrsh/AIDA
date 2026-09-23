
<h1>AIDA — AI-Driven Acquisition

<img width="153" height="102" alt="image" src="https://github.com/user-attachments/assets/393bd92c-a366-411b-9dd3-d1b5ceadb0be" />

AIDA is an automated, AI-driven mass spectrometry acquisition platform designed for deep, accurate, and high-throughput quantitative proteomics. AIDA autonomously controls and optimizes MS1, MS2, and MS3 acquisition in real time, maximizing proteome coverage while leveraging TMT multiplexing to analyze up to 35 samples simultaneously.

**Depth and sensitivity**: Adaptive MS1 tiling and intelligent MS2 isolation-window selection prioritize the detection of low-abundance peptides and previously unquantified proteins.
**Accurate quantification**: AI-optimized fragmentation and dynamic MS3 ion accumulation maximize TMT reporter-ion signal while minimizing interference and maintaining user-defined signal-to-noise thresholds.
**High throughput**: Combining multiplexed peptide identification with TMTpro 18-plex and 35-plex sample multiplexing enables deep proteome characterization of large sample cohorts.
**Robustness and adaptability**: Real-time retention-time alignment, mass-accuracy correction, and adaptive acquisition compensate for variations in chromatography and instrument performance.
**Flexibility and extensibility**: Custom target databases, adjustable acquisition parameters, and interchangeable prediction inputs lets users tailor AIDA to different sample types and experimental objectives.


AIDA is currently designed for TMT-multiplexed proteomics on compatible Thermo Scientific Orbitrap Tribrid mass spectrometers, using real-time instrument control through the Thermo Fisher Scientific iAPI.

AIDA can be downloaded from this Github Directory as AIDAv1p0.exe

<h1>Table of Contents</h1>

Before you start
Recommended first workflow
Main
Advanced
Database generator
Offline search
Post Run Script
Gradient Cal
Transfer Learn
Run
Troubleshooting


<h3>**Before you start**</h3>
DIA-NN is written for Windows and requires XCalibur 4.5 or higher, Tune 4.2xxx and iAPI Access. AIDA has been tested on fast multithread CPU's, for our use case a i9 14900 was used.

We have provided a sample cell-line, plasma and breast-tissue databases. However 
What you need
A Windows computer with the instrument/API dependencies required by the acquisition installation.
A valid Python executable for the Python-backed tools. Use Environment Check to verify it.
A peptide/protein database for acquisition or search. The database generator accepts peptide/protein text input or FASTA input and writes the database used by AIDA workflows.
For acquisition: a writable output directory and the database to use.
For offline search: a Thermo `.raw` file, a CSV database or packed database directory, an output root, and the offline-search Python environment.

<h3>**Start the application**</h3>
For a development build, launch `AIDAv1p0.exe` . Release builds should be launched from their corresponding release directory. Keep the executable together with its dependency files.

<h3>**Recommended first workflow**</h3>
For a first test, use a small database and a short or representative RAW file.
Open Environment Check and point it to the Python interpreter used for AIDA tools. Click Check environment. Install only missing packages after confirming the selected Python path.
Use Database generator to create or refresh a database, or select an existing compatible database.
On Main, set the run number, database, output directory, TMT plex, run length, AIDA+ setting, and Smart Caller mode.
Review Advanced. Defaults are intended to preserve the configured method behavior; unlock a row only when you intend to override it.
Confirm instrument readiness, then click Start on Main. Monitor progress on Run.
At completion, open Post Run Script. AIDA pre-fills its Chopin/MS3Signal/output fields; choose the RAW file and run sieving, with optional MS3 TMT quantification.

<h2>Main</h2>
The Main tab contains the minimum settings needed to start an acquisition.

<img width="1477" height="867" alt="image" src="https://github.com/user-attachments/assets/ff7f2d69-ca38-4f8b-ba61-ab7a4535b0a8" />

Files and run
Control	Purpose
Run number	Identifier used in generated output names.
Database	Select the AIDA peptide database for the run.
Output	Select a writable folder for run outputs and logs.
Start	Validates the database and output folder, then begins acquisition.
Method tiles
Control	Meaning
TMT Plex	Select the 18- or 35-channel profile. Internally, the 35-channel selection is represented using the application’s 32-channel setting.
Run time	Maximum acquisition duration in minutes.
AIDA+	Higher-signal, faster-acquisition mode.
Smart Caller	Full uses the more complete decision logic; Light favors faster operation.
Use the defaults for the first run unless you have a reason to change them. The Main tab deliberately keeps method configuration compact; detailed settings are on Advanced.

<h2>Advanced</h2>
Advanced controls are initially locked to protect method defaults. Click an individual lock to edit a row, or use Unlock all when deliberately configuring a custom method.
<img width="1475" height="870" alt="image" src="https://github.com/user-attachments/assets/95958924-80d4-4792-9d37-35013c7b3a4a" />
<img width="725" height="72" alt="image" src="https://github.com/user-attachments/assets/069f509b-08f6-4935-98e2-32b3ceba858b" />

FAIMS and scan schedule
FAIMS CVs: the three compensation voltages used by the method. Defaults are `-40`, `-55`, and `-70`.
MS2 scans per CV: scheduling budget for each FAIMS CV.
MSX per MS1: number of MSX scans associated with each MS1 event.
Use GPU: enables GPU use where supported. Default is off.
Starting order (mid-run): starting elution-order position from `0` to `1`; normally leave at `0`.
MS3
Target MS3 ions and MS3 ion cutoff: ion targets used for MS3 calling.
MS3 SSN target: signal-to-noise criterion for MS3 calls.
Min/Max MS3 time and round-2 max time: injection-time bounds in milliseconds.
MS3 resolution: 50K, 75K, or 90K.
SPS: number of synchronous precursor selection fragments when original fragments are used.
Flags and cycle times
Call round 2 scans: enables the second-round scan behavior.
Minimum for overs: preserves the minimum-fill behavior for overs.
Use original MS3 fragments: requests the legacy/original MS3 fragment behavior.
Force analyzer cycle time: applies a fixed analyzer-cycle-time behavior.
Plasma mode: allows longer, approximately two-second MS3 injection behavior.
Wide MS2 ppm: uses ±12 ppm rather than the ±6 ppm setting.
Predicted cycle times: select which of Slowest, Slow, Normal, Fast, and Fastest predicted cycle times can be considered. Normal, Fast, and Fastest are enabled by default.

<h2>Environment Check</h2>
Use this tab before Database generator, Offline search, Post Run Script, or Transfer Learn.
<img width="1472" height="865" alt="image" src="https://github.com/user-attachments/assets/051a26a8-da46-429b-87aa-ecbd75bc0e75" />

Select the Python executable used by the AIDA tools.
Click Check environment.
Review checks for Python, pip, .NET, `OfflineSearch.dll`, `search_methods.py`, and the required Python packages.
If packages are missing, edit the package list if needed and click Install packages.
Installing packages modifies the selected Python environment. Confirm that its path is the intended environment before clicking Install.

<h2>Database generator</h2>
This tab produces the peptide database consumed by AIDA workflows.
<img width="1467" height="860" alt="image" src="https://github.com/user-attachments/assets/f60c490c-5523-4d84-84b9-260ab42ba8d5" />
<img width="402" height="722" alt="image" src="https://github.com/user-attachments/assets/6c9f734a-2bb9-4d64-84d3-284b4edbf9b0" />

Input and build mode
Select peptide/protein text input or FASTA input, then select the TMT label profile. Choose:
Full build to generate all selected database-model columns.
Score one model to apply a single selected model/version.
Full build settings
Set charge states, precursor mass range, reverse/decoy behavior, and optional methionine oxidation. The model section lets you select:
Order / retention-time model and its model file.
FAIMS CV model.
Fragment-intensity model.
Charge prediction.
Flyability prediction.
FAIMS CV and Fragment intensity use V1 by default. V2-Beta is available as an experimental alternative. When Fragment intensity is V1, Charge prediction and Flyability appear directly below it. Selecting Fragment intensity V2-Beta expands the section to show Collision, Energy, Analyzer, and Collision-energy sweep controls.
For V2-Beta Fragment intensity:
Select CID or HCD and set the collision energy.
Select IonTrap, Orbitrap, or Astral as analyzer. Astral forces HCD.
Enable the energy sweep only when a collision-energy sweep is intended.
Score one model
Choose FAIMS, Fragment, Order, Charge, or Fly, then choose the applicable version. The Collision/Energy controls appear only for Fragment V2-Beta scoring.
Generate
Choose an output database filename, select the Python executable, choose whether to use GPU, then click Generate database. The output panel reports peptide and database-entry counts, and the log records the invoked workflow.

<h2>Offline search</h2>
Offline search runs the supporting search workflow on a RAW file and reports peptide/protein counts.
<img width="1480" height="877" alt="image" src="https://github.com/user-attachments/assets/ac1fe3dc-6728-469c-91b4-396a35ff9136" />

Choose the RAW file.
Choose the database: either a CSV/TSV database or a packed database directory.
Select a writable output root.
Select the search mode:
DDA for DDA search.
DIA-Faster (beta) for the faster DIA mode.
DIA (beta) for the broader DIA mode.
For DIA, set Top MS1 peaks. `1` uses only the most intense precursor candidate per isolation window; higher values consider more candidates and take longer.
Leave Tight MS2 ppm off for the default ±12 ppm search window; enable it for ±6 ppm.
Optionally enable Attach MS3 quant, then provide the MS3Signal CSV, TMT plex, and SSN cutoff.
Select Python and click Run search.
The result panel reports unique peptides, unique proteins, sieved proteins, and—when MS3 quantification is attached—proteins above the SSN cutoff. Use Open output folder to inspect the run products.

<h2>Post Run Script</h2>
<img width="1480" height="872" alt="image" src="https://github.com/user-attachments/assets/efc6ff7a-f46e-45c0-9cfe-59a2ba948a19" />

This is the normal downstream step after an AIDA acquisition. It runs post-run protein sieving with mokapot and can run MS3 TMT quantification.
After an AIDA run, Chopin CSV, MS3Signal CSV, and output-folder fields are automatically filled. You normally only need to choose the RAW file.
Provide the RAW file, Chopin CSV, MS3Signal CSV, and output folder. The latter three may already be populated after acquisition.
Enable or disable Run Quantification (MS3 TMT).
If quantification is enabled, select the TMT plex and SSN cutoff. Defaults are 180 for TMT18 and 350 for TMT35.
Choose the Python executable and click Run.
With quantification disabled, the tab performs the sieving workflow without requiring RAW/MS3Signal input. The results panel reports peptides at 1%, sieved proteins, and proteins above SSN when quantification was run.

<h2>Gradient Cal</h2>
<img width="1475" height="870" alt="image" src="https://github.com/user-attachments/assets/1d727855-0525-42a3-a73f-88d1a15da6d1" />

Gradient Cal proposes a revised `%B` program using a target database and a calibration run.
Step 1 — Target database: select the database, set the retention-order column (default column 4), and click Read. The app reports unique peptide count and median order.
Step 2 — Coverage target: select the desired order/coverage target. The interface shows the corresponding fraction of the database.
Step 3 — Calibration run: select the calibration Chopin CSV and enter the gradient program used for that run as Time (min) / %B points.
Click Optimize gradient.
The result side displays fit quality (R²), coverage, CV, the calibration line, a proposed gradient table, and a chart comparing the original and proposed programs. Review the proposed program against instrument, column, and solvent constraints before using it.

<h2>Transfer Learn</h2>
<img width="1671" height="979" alt="image" src="https://github.com/user-attachments/assets/2bc40d32-de5e-4608-936d-6077009894eb" />

Transfer Learn adapts the retention-time model to your LC column using observations from multiple runs.
Provide a runs CSV containing `peptide`, `time`, and `run_id`, with at least two runs.
Select the base retention-time model.
Choose an output folder.
Choose the held-out run. `auto` selects the largest suitable run; the held-out run is the honest evaluation set.
Set the number of epochs and minimum shared peptides.
Select a Python environment with the required GPU/Torch dependencies and click Run adaptation.
The output folder receives the adapted model and plots. Use the old-vs-new comparison on the held-out run, rather than training loss alone, to decide whether the adaptation is beneficial.

<h2>Run</h2>
<img width="1482" height="867" alt="image" src="https://github.com/user-attachments/assets/743787d7-516d-4fb0-a97c-2f8136df1e2c" />

The Run tab is the acquisition monitor. It displays startup output and then a concise set of live metrics, including current order, total proteins, and unique proteins with MS3 evidence. The full engine log is written to a timestamped file in the application log directory.
Use Stop run — save && finish to end the acquisition gracefully. It requests cancellation, writes run outputs, and completes the normal shutdown path. Do not terminate the process externally unless the application is unresponsive and you accept the risk of incomplete output.

For each run, retain:
The input database and its generation settings.
Main and Advanced settings, including FAIMS CVs and MS3 parameters.
RAW data and resulting Chopin/MS3Signal files.
Python executable path and package environment used for database/search/post-run tools.
Output logs and post-run/offline-search result folders.
This structure follows the same documentation philosophy as projects such as DIA-NN: start with a short, reproducible workflow, then provide a settings reference and troubleshooting guidance.
