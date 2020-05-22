
import glassdoor_scrap as gs
import pandas as pd
path = "/Users/apple/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000,False,path,15)
df.to_csv('glassdoor_jobsin.csv',index=False)
