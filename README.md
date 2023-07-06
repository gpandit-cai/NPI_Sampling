### *Checking the NPI Sample(Active/Deactive) using [NPI Registry API](https://npiregistry.cms.hhs.gov/search)*

***Using API we are checking sample(n=1000) NPI to identify Its status***

*`app.py`- Created to pull the data from API.

*`pull.py`- It will pick sample and hit the API and store the output into 5 different excel files (NPI_Output_{1,2,3.....})

*`NPI.csv` is the input file where we kept our NPI which will be automatically picked by the python code.

*`NPI_Output` Excel file has two sheets, sheet one will have all the active NPI with the basic details and Sheet2 has all the deactive/Invalid NPIs.

