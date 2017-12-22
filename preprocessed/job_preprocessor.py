import os
import json

with open('raw_jobs.md') as f:
    job_table = f.readlines()
    jobs = []
    for job_entry in job_table:
        job, location = job_entry.split('|')[1:3]
        job = job.strip().lstrip()
        location = location.strip().lstrip()
        locations = [_.strip().lstrip() for _ in location.split(';')]
        company, link = job.split('](')
        company = company[1:]
        link = link[:-1]
        jobs.append({
            'company': company,
            'link': link,
            'locations': locations
        })
    with open('jobs.json','w') as f2:
        json.dump(jobs, f2)