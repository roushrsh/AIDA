# AIDA
AI Driven Acquisition


AIDA is a software method for real-time data acquisition of tribrid mass spectrometers.

## Running:

AIDA Can just be extracted from the rar (zipped) file in this github (in the future an installer will be included). The larger .exe application file with the AIDA icon has to be double clicked for it to open to this image below

<img width="3344" height="1971" alt="image" src="https://github.com/user-attachments/assets/de9e3159-1bc1-4439-9a71-a415b224ceca" />

See png picture above.

## Requirements

A Computer with windows 10 installed. (Tested on Windows 10 Pro, Version 21H2)

A compatible Thermo Fisher Scientific Tribrid Mass Spectrometer (The current iteration of AIDA has only been tested on an Orbitrap Eclipse, however older builds did run on the Fusion.)

Tune and XCalibur Tribrid software. Specifically, Tune 4.2.4310.9 and Xcalibur 4.7.69.37. The Tune version is important, as previous and later variants may contain bugs for certain calls performed by AIDA.

All required .dll files are included in the zip, including thermo's API modules, however, API Access from thermo scientific is required for the API to access the instrument, which must be activated through Tune.

## Optional Requirements
A fast multi-core CPU that can handle the processing required for optimal results 
AIDA can run all of its code on the computers CPU, however for faster processing, an NVidia GPU with CUDA support can be used.
All of our most recent data was tested with a NVIDIA RTX 4090 GPU, and both Intel i9-13900K and Intel i9-14900K processors.


## Databases
Below is a google drive link to a Cellline, Plasma mini, Plasam Full, and Breast Tumor Databases to be downloaded for use with AIDA. Our models along with appropriate python scripts used to generate databases will be available in the future.

## File outputs
Current AIDA outputs 
Although one can already extract out the data and process themselves, In the future, generic moka pot processing plus protein picking scripts will be included.

## Parameters selection
AIDA requires a database to be selected (see above), and an output folder destination where it will output the results of its real-time acquisition.
The Run Number is just the unique number that will be assigned to each file to make it unique for the run. (in our case we match the row on Xcalibur).

The preset settings are tuned for a generic 3 hour TMT 18 sample, but can be altered as described below to maximize different gradients and samples. 

##Acquisition settings:

TMT :
This is the multiplexing used. Current databases are trained on TMT18 and TMT32 data, however we allow TMT11 to be used here as well. This changes the MS3 output files results, and which fragments the online AIDA search looks for in the MS3 to maximize signal to noise.

Run Time (min):
This is the length of your gradient. By default, AIDA does not scan in the first 2 minutes, and stops acquiring roughly 20 seconds before the run is over.

FAIMS CVs:
These are the 3 CV's always cycled in AIDA and can be varied, however our testing shows the optimal three to be roughly -40,-55 and -70.

MS2 Scans Per CV:
As different CV's cover different mass ranges, different cv's need fewer MS2s to cover the range. This goes hand in hand with shorter gradients being able to accomodate fewer MS2s before the elution peak dissapears.

Number of MSX Per MS1. As there is a processing requirement from when a MS1 is recieved, SIMS are generated, and MS2s are sent out, MSX discovery scans can be sent out to maximize acquisition per minute. These get sent out behind the SIM scan and therefore require no post MS1 processing time. Slower processors can take advantage by calling 1 or 2 MSX scans , whereas the fastest processors can have this set to 0.

##MS3 Settings:

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

##Toggles

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
