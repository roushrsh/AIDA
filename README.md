# AIDA
AI Driven Acquisition


AIDA is a software method for real-time data acquisition of tribrid mass spectrometers.

## Running:

AIDA Can just be extracted from the rar (zipped) file in this github (in the future an installer will be included). The larger .exe application file with the AIDA icon has to be double clicked for it to open to this image below

<img width="3344" height="1971" alt="image" src="https://github.com/user-attachments/assets/de9e3159-1bc1-4439-9a71-a415b224ceca" />


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
