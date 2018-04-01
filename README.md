# predicting-billionaires-status
Statistics project to predict billionaire networth (using dataset found at: https://piie.com/publications/working-papers/origins-superrich-billionaire-characteristics-database?ResearchID=2917).

# About the Project
This project is a statistics project for SDS 291: Multiple Regression (taken Spring 2018 of my sophomore year). It mainly consists of code written in R and write ups in R Markdown (and HTML).

## sourceofwealth.py
sourceofwealth.py is a python program written to edit the original dataset (included as "oldBillionaires.csv") to contain a column titled "numsourceofwealth", which is the number of sources of wealth for the billionaire. Originally, we had planned to use the variable `sourceofwealth` to determine if the billionaire's source of wealth has an effect on the billionaire's networth. However, upon discovering that the variable has over 600 levels, we decided to determine the number of sources of wealth instead. To do this, I wrote a python programming that determines the billionaire's number of sources of wealth (basically by determining how many commas are in the source of wealth column), and writes a new csv file including this comma.
