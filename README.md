# AIDA
AIDA
AI-Directed Acquisition (AIDA) is a software package that enables AI-orchestrated autonomous mass spectrometry-based data acquisition on Thermo Fisher Scientifc Tribrid mass spectrometers (Orbitrap Eclipse and Orbitrap Ascend)

## Running the Program:

A .rar file is provided. Upon extraction, the larger .exe application file with the AIDA icon has to be double-clicked for it to open to this image below (or see png attached above.)

<img width="1894" height="1203" alt="image" src="https://github.com/user-attachments/assets/d1904b06-2655-43d2-bb64-4db2acaebfa4" />


## Requirements

Windows 10; the application was tested on Windows 10 Pro, Version 21H2
A compatible Thermo Fisher Scientific Tribrid mass spectrometer including the Orbitrap Eclipse and the Orbitrap Ascend instruments (the application has been exclusively tested on an Orbitrap Eclipse)
Tune and Xcalibur Tribrid software (Tune 4.2.4310.9 and Xcalibur 4.7.69.37).  The correct version of the Tune software is crucial; previous and later versions may not be able to successfully run the application.
All required .dll files are included in the .rar file. This Comprise Thermo Fisher Scientific iapi modules.  API access must be approved by Thermo Fisher Scientifc and activated via the Tune software.

## Optional Requirements
AIDA can be operated using high-performance multi-core CPUs (Intel i9-13900K or Intel i9-14900K). For faster processing we recommend Nvidia GPUs with CUDA support (tested on NVIDIA RTX 4090 GPU.

## Databases
The Google Drive link includes target databases for using AIDA on cell line, blood plasma, and tumor samples. All databases are for samples of human origin. For plasma samples, two databases with the smaller version only including blood plasma protein peptides identified in our research group, while the larger database includes all possible peptides of the quantified proteins.

https://drive.google.com/drive/folders/1Sd0ZnZC7aPbky6W1ear_jACevGKypAf7?usp=sharing   



## File outputs

AIDA provides the following files as outputs:
(1) -filename-API-.csv
This file provides information on the scoring of every targeted peptide from the analysis.
For each peptide, the following information is provided in columns:
MS2 ID:  MS2 scan ID
cleanedEnds:  peptide sequence
Reference:  Uniprot database protein entry string including the location of the protein in the Swissprot (sp) or Trembl (tr) component, the Uniprot protein accession number, and the Uniprot protein name—all separated by vertical lines.
Charge:  peptide charge state
DBMass:  peptide mass (Da)
AdjustedMass:  corrected peptide ion mass deviation (ppm)
OriginalMass:  uncorrected peptide ion mass deviation (ppm)
currentOrder:  predicted peptide elution order adjusted in real-time
peptidesOrder:  predicted peptide elution order from database
PredScore:  peptide spectrum match score
MS1 ID:  MS1 scan ID
Time:  retention time (min)
Cosine:  peptide spectrum match cosine similarity score
Hit:  number of observed predicted fragment ions
NumberPossible:  total number of fragment ions predicted to be observable
CV:  FAIMS CV setting
Analyzer:  mass analyzer used for detection
Truth:  peptide annotation to forward or reversed (decoy) database component
TotalIntOffFrags: total Intensity of MS2 fragment ions annotated to the target peptide
MS2IntSum:  total MS2 signal intensity
dCn:  “Hit” difference between top and following best match

(2) MS2Called-filename-API-.csv
This file provides information on each acquired MS2 spectrum.
MS1 ID: MS1 scan ID
ScanPoint:  m/z center of MS2 isolation window
IT:  ion accumulation time
IsoSize:  size of isolation window (m/z)
Analyzer:  mass analyzer used for detection
MS1 Score:  score reflecting likelihood of identifying new protein from the selected isolation window
Resolution:  mass resolution used MS2 data acquisition


(3) MS3Signal-filename-API-.csv
This file provides information on each acquired MS3 spectrum.
MS1 ID:  MS1 scan ID
MS2 ID: MS2 scan ID
MS3 ID: MS3 scan ID
Peptide: peptide sequence
Protein:  Uniprot database protein entry string including the location of the protein in the Swissprot (sp) or Trembl (tr) component, the Uniprot protein accession number, and the Uniprot protein name—all separated by vertical lines.
126, 127n, 127c, 127d, 128n, 128nd, 128c, 128cd, 129n, 129nd, 129c, 129cd, 130n, 130nd, 130c, 130cd, 131n, 131nd, 131c, 131cd, 132n, 132nd, 132c, 132cd, 133n, 133nd, 133c, 133cd, 134n, 134nd, 134c, 134cd, 135n, 135nd, 135cd: signal intensity in TMT reporter ion channel (number of ions/millisecond)
MS3IonSum: sum of reporter ion signal (number of ions/millisecond)
MS3IIT: MS3 ion accumulation time (millisecond)
MS3TotalCurr: “MS3IonSum” x “MS3IIT”
massesChosen: MS2 fragment ions selected for MS3
Round: first MS3 for the peptide (1) or salvage scan (2)



## Parameters selection
AIDA requires a database to be selected (see above), and an output folder destination where it will output the results of its real-time acquisition.
The Run Number is just the unique number that will be assigned to each file to make it unique for the run. (in our case we match the row on Xcalibur).

The preset settings are tuned for a generic 3 hour TMT 18 sample, but can be altered as described below to maximize different gradients and samples. 

## Acquisition settings:

TMT :
This is the multiplexing used. Current databases are trained on TMT18 and TMT32 data, however we allow TMT11 to be used here as well. This changes the MS3 output files results, and which fragments the online AIDA search looks for in the MS3 to maximize signal to noise.

Run Time (min):
This is the length of your gradient. By default, AIDA does not scan in the first 2 minutes, and stops acquiring roughly 20 seconds before the run is over.

FAIMS CVs:
These are the 3 CV's always cycled in AIDA and can be varied, however our testing shows the optimal three to be roughly -40,-55 and -70.

MS2 Scans Per CV:
As different CV's cover different mass ranges, different cv's need fewer MS2s to cover the range. This goes hand in hand with shorter gradients being able to accomodate fewer MS2s before the elution peak dissapears.

Number of MSX Per MS1. As there is a processing requirement from when a MS1 is recieved, SIMS are generated, and MS2s are sent out, MSX discovery scans can be sent out to maximize acquisition per minute. These get sent out behind the SIM scan and therefore require no post MS1 processing time. Slower processors can take advantage by calling 1 or 2 MSX scans , whereas the fastest processors can have this set to 0.

## MS3 Settings:

Target ions:
We re-calculate SSN after the run finished, but in real-time use total ion signal to estimate if we have enough signal to match SSN. A SSN of 180 is roughly equivalent to 8 million 'ion' units of TMT fragments. Therefore, for TMT 18 we aim for 10 million ions to guarantee the great majority of peptides have enough signal. As noise is constant and doesn't scale with signal, less than double the signal is required for TMT32 samples. In our testing, 12.5 million ions for Target is usually enough.

MS3 Ions Round 2 SSN Cutoff:
When the peptide comes back, a salvage MS3 scan can be sent to get enough signal for the target peptide. We generally set this to a lower value, to give it a chance at actually getting enough signal.

Min MS3 Time (ms): 
This is the minimum time an MS3 will ever be sent for. Generally recommended to be 200 ms for an average sample, but can be as low as the 50k cycle time of 86ms if high enough concentrations are used for cell lines (ex 20 ug/ul per shot). 

Max MS3 Time (ms):
This is the maximum amount of time alotted to an MS3. If it will take longer, it will default to this value.

Max MS3 Time Second Round (ms):
This is for the salvage scan. Similar to the Max MS3 Time, this is the max alotted time for a second round.

MS3 Resolution:
This is the Orbitrap resolution used for MS3s. For TMT18 50k is all that is needed, but TMT32 requires 75k or 90k. 

Number of SPS if Original Fragments:
AIDA uses predicted energy fragments so this setting is not used unless the 'Use Original MS3 fragments' toggle is enabled, but if it is, it will instead looking at the MS2 spectra at the same energy and choose n(number of sps) fragments post clean up for MS3.

## Toggles

Use GPU:
This enables GPU use for AIDA's peak scoring. If enabled and no gpu, AIDA will throw an error.

Call Round 2 Scans:
This allows for salvage round 2 scans to be called. These only get called if the estimated time is below the max afforded time.

Minimum for Overs:
If a scan is going to take longer than the Max MS3 time, this check will force AIDA to call a scan at the minimum MS3 time instead of the maximum. This way, if the peptide is about to elute, we will see signal go up and the rest can be salvaged during the second round, and if it's not going to elute, time won't be wasted on the follow up scan.

Use Original MS3 Fragments:
As described above, this forces AIDA to choose fragments at the observed MS2 spectra + collision energy, over predicted ones.

Predicted MS3 Cycle times to Consider:
The AIDA MS3 accumulation model predicts an estimate time to achieve the designated signal based on observed MS2 fragment intensities (ex: aim for 10 million ions). However it also provides error estimates at 1 and 2 standard deviations. The longest accumulation time that falls below the max MS3 time is what is ultimately taken. To cover enough ground, most peptides don't require the slowest, ie longest amount of accumulation time, to reach the target SSN, buit if targets are rare, ex for plasma, this could be useful to maximize signal.

Force Analyzer Cycle time:
This forces all MS3s to perform their first scan at the analyzers cycle time (86 ms for 50k, and 131ms for TMT 32), the idea being that if needed, the second round scan will get the remaining required signal.
