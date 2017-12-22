# Headers:
'''
0 TITLE
1 CATEGORY_1
2 CATEGORY_2
3 CATEGORY_3
4 INDUSTRY_1
5 INDUSTRY_2
6 INDUSTRY_3
7 SALARY_MIN
8 SALARY_MAX
9 EXPERIENCE
'''
import os
from console_logging.console import Console
console = Console()
import json

data = None
with open('jobs_dataset.csv') as f:
    def organize(d):
        try:
            return {
                'title': d[0].strip(),
                'categories': [_.strip() for _ in d[1:4]],
                'industries': [_.strip() for _ in d[4:7]],
                'salary': {
                    'min': d[7].strip(), 'max': d[8].strip()
                },
                'experience': d[9].strip()
            }
        except Exception as e:
            console.error(e) # in case data isnt correct just prune it
            exit()
    ls = f.readlines()[:10000] # realistically we don't even need 10,000 rows
    data = [organize(l.strip().split(',')) for l in ls[1:]]
    with open('data.json','w') as f2:
        json.dump(data, f2)