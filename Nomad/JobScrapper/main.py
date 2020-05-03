from indeedW import get_jobs as get_indeedW_jobs
from soW import get_jobs as get_soW_jobs
from save import save_to_file

searchWhat = 'python'

indeedW_jobs = get_indeedW_jobs(searchWhat)
soW_jobs = get_soW_jobs(searchWhat)
jobs = indeedW_jobs + soW_jobs

save_to_file(jobs)
