import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')
#tasks:
# salary parsing
#Company name text only
# state field
#age of company
#parsing of job description(like keyword:Python)

df =df[df['Salary Estimate'] != -1]
