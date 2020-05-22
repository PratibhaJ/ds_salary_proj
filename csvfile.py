import pandas as pd
df = pd.read_csv("glassdoor_jobs.txt",delimiter=',')
df.to_csv('glassdoor_jobs.csv')
