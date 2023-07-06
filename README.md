### *Checking the NPI Sample(Active/Deactive) using [NPI Registry API](https://npiregistry.cms.hhs.gov/search)*

***Using API we are checking sample(n=1000) NPI to identify Its status***

*`app.py`- Created to pull the data from API.

*`pull.py`- It will pick the sample NPIs from `NPI.csv` and hit the API, then result will be stored in 5 different Excel files (NPI_Output_{1,2,3.....})

*`NPI.csv` is the input file where we kept our NPI which the Python code will automatically pick.

*`NPI_Output` Excel file has two sheets, sheet one will have all the active NPI with the basic details, and sheet 2 have all the deactivate/Invalid NPIs.

***Note - It takes around 40-50 minutes to generate one sample file if we reduce the sample size it may reduce the run time.***
