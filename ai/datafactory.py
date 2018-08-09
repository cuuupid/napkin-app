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
import csv

data = None
with open('jobs_dataset.csv') as f:
    def organize(d):
        d = list(d)
        try:
            return {
                'title': d[0].strip().lower(),
                'categories': [_.strip().lower() for _ in d[1:4]],
                'industries': [_.strip().lower() for _ in d[4:7]],
                'salary': {
                    'min': d[7].strip(), 'max': d[8].strip()
                },
                'experience': d[9].strip()
            }
        except Exception as e:
            console.error(e)  # in case data isnt correct just prune it
            exit()
    rows = list(csv.reader(f, delimiter=',', quotechar='"'))
    data = [organize(row)
            for row in rows[:30000]]
    test = [organize(row) for row in rows[30000:35000]]
    with open('features.json', 'w') as f2:
        json.dump(data, f2)
    with open('test.json', 'w') as f3:
        json.dump(test, f3)