import json
import os
from lxml import html
import requests
import unicodedata
from console_logging.console import Console
console = Console()

job_data = None

with open('jobs.json') as f:
    job_data = json.load(f)
    console.info("Crawling %d career pages." % len(job_data))
    i = 0
    for job_entry in job_data:
        try:
            url = job_entry['link']
            page = requests.get(url)
            tree = html.fromstring(page.content)
            links = tree.xpath('//a')
            job_postings = []
            for link in links:
                job_title = link.text_content().strip().lstrip()
                if 'intern' in job_title: # only test if intern position
                    res = requests.post(
                        'http://127.0.0.1:8000/predict', json={'title': job_title})
                    prediction = res.text.strip().lstrip()
                    if prediction in ['IT/Software Development', 'Engineering']:
                        job_postings.append(job_title)
            job_entry['positions'] = job_postings
        except Exception as e:
            console.error(e)
        i = i + 1
        if i % 20 == 0:
            console.log("Processed %d pages." % i)
console.success("Finished crawling.")

with open('jobs.json', 'w') as f:
    json.dump(job_data, f)

console.success("Dumped data.")