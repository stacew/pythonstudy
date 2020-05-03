from indeedW import get_jobs as get_indeedW_jobs
from soW import get_jobs as get_soW_jobs

searchWhat = 'python'

indeedW_jobs = get_indeedW_jobs(searchWhat)
soW_jobs = get_soW_jobs(searchWhat)
jobs = indeedW_jobs + soW_jobs
for job in jobs:
    print("title :", job['title'])
    print("company :", job['company'])
    print("location :", job['location'])
    print("link :", job['link'])
    print()
