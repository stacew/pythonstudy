import csv


def save_to_file(jobs):
    # newline='' : writerow마다 한 줄 씩 띄우는 것 막음
    file = open('jobs.csv', mode="w", newline='')
    writer = csv.writer(file)

    writer.writerow(["title", "company", "location", "link"])

    # for job in jobs:
    #     writer.writerow([job["title"], job["company"],
    #                      job["location"], job["link"]])
    for job in jobs:
        writer.writerow(list(job.values()))

    print(file)
    return
