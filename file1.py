
import glassdoor_scrapper as gs
import pandas as pd
path = "/Users/apple/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15,False,path,15)
df
