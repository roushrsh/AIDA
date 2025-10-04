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


For peptide filtering, we recommend the use of mokapot (PMID: 33596079) using the following data inputs:  Charge, Cosine, Hit, order Difference, Length of peptide, PredScore, log2(fragment ints +1), Log2 (fragment ints/total ints +1), dCn, hits/Possible Ratio

For protein filtering, we recommend the use of the “picked” protein method (PMID: 25987413).

MS3 data are re-processed offline using the Thermo Fisher Scientific Raw Reader.


## Parameters selection

Running AIDA requires the selection of a database, and the setting of an output folder destination.. The Run Number is a unique number that will be assigned to each file.

The default settings are optimized for a regular generic 3-hour TMT18 sample analysis, but can be altered as described below to optimize the results for different gradients and samples.


## Acquisition settings:

TMT :  TMT reagents used for multiplexing (TMT18 or TMT35)

Run Time (min): The length of the LC gradient (data acquisition time) in minutes.

FAIMS CVs:  AIDA cycles through 3 FAIMS CV settings.  Our testing showed that the optimal settings to -40, -55 and -70 V.

MS2 Scans Per CV:  As different CV settings give signal distributions centered at different mass ranges, the number of MS2 to cover these m/z ranges also differs.

Number of MSX Per MS1:  As there is a processing time between the receiving of MS1 signals, the generation of SIM scans, and the calling of MS2 scans, multiplexed MS2 (MSX) discovery scans can be called to maximize data acquisition efficiency.  When using slower processors, calling 1 to 2 MSX scans will benefit the proteome coverage, whereas the number should be set to 0 when faster processors are used.


## MS3 Settings:

Target ions:  Recommended settings are 1x107 for TMT18 and 1.25x107 for TMT35.

Salvage MS3 scan signal-to-noise threshhold: Recommended settings are 8x106 for TMT18 and 1.15x107 for TMT35

Min MS3 Time (ms):  a setting of 200 milliseconds is our default recommendation, it can be lowered for samples with high overall protein concentrations (e.g., cell line samples)
.
Max MS3 Time (ms):  300 milliseconds for cell line and tumor samples, 1000 milliseconds for blood plasma samples.

Max MS3 Time Second Round (ms):  1000 milliseconds

MS3 Resolution:  5x104 for TMT18, 9x104 for TMT35.

Number of SPS if Original Fragments:  AIDA uses predicted energy fragments.  Therefore, this setting will not be considered unless the 'Use Original MS3 fragments' toggle is enabled.  If enabled, a setting of 5 is recommended.


## Toggles
Use GPU:  This enables GPU use for AIDA's peak scoring.

Call Round 2 Scans: This allows for salvage MS3 scans to be called.

Minimum for Overs:  Optimizes the time for the calling for salvage MS3 scan acquisitions.  We recommend using this toggle for efficient salvage MS3 scan use.

Use Original MS3 Fragments:  This will ignore our MS2 peptide intensity prediction when selecting MS2 fragment ions for MS3.  Its use is not recommended.

Predicted MS3 Cycle times to Consider:  Large sample amounts can be run with “Fastest” setting, for lower amounts “Slow” and “Normal” will be the optimal settings.  This setting influences the data acquisition speed and should be optimized for each sample type.

Force Analyzer Cycle time: This forces all MS3s to perform their first scan at the analyzer's cycle time (86 ms for 50k, and 131ms for TMT 35), so that the salvage MS3 scan will be optimized for reaching the target signal threshold.  Only recommended when analyzing large sample amounts.
