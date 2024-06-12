# knhts-hpt-uploader
Project to upload concepts to KNHTS - Original idea by Amos Laboso and improved by Newton Mugaya.

## Technology stack
Python - 3.10\
openpyxl==3.1.3\
requests==2.31.0


## Functionality
### Importation of
Maptypes - Medicine scheduling, Dosage form, Routes of admin, Shelf life and Storage conditions\
Pharmaceuticals\
Non-pharmaceuticals - Medical Supplies, Medical Equipment and Lab Diagnostics


### Note
Confirm the files in files/* columns have not been re-ordered comparing with main.py files\
Run the files in the order specified\
Use screen as this will take hours to complete.

## Installation

Edit common/settings.py with the correct Server URL and Token

cd maptypes\
python main.py

cd pharma\
python main.py

cd non_pharma\
If the concept_id for the subdomain (Medical Supplies, Medical Equipment and Lab Diagnostics) is existing put it in the main file before running to avoid duplicates

python main_devices.py to upload Medical Supplies\
python main_equipment.py to upload Medical Equipment\
python main_lab.py to upload Lab Diagnostics

