import requests
from bs4 import BeautifulSoup


def extract_job(html):
    strTitle = html.find("h2").find("a")["title"]

    # strCompany = html.find("h3").find("span").text
    # strLocation = html.find("h3").find("span", {"fc-black-500"}).text
    strCompany,  strLocation = html.find(
        "h3").find_all("span", recursive=False)
    strCompany = strCompany.text
    strLocation = strLocation.text

    strJobID = html["data-jobid"]
    return {'title': strTitle,
            'company': strCompany.strip(),
            'location': strLocation.strip("-").strip("\r").strip("\n"),
            'link': f"https://stackoverflow.com/jobs/{strJobID}"
            }


def extract_jobs(BASE_URL, last_page):
    jobs = []
    for page in range(last_page):
        GET_PAGE_URL = f"{BASE_URL}&pg={page + 1}"
        result = requests.get(GET_PAGE_URL)

        print("Get URL :", GET_PAGE_URL)
        result = requests.get(GET_PAGE_URL)
        print("StatusCode :", result.status_code)

        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

        return jobs


def extract_lastPage(BASE_URL):
    print("extract_lastPage() Get URL :", BASE_URL)
    result = requests.get(BASE_URL)
    print("status code :", result.status_code)

    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def get_jobs(searchWhat):
    BASE_URL = f"https://stackoverflow.com/jobs?q={searchWhat}&sort=i"

    lastPageNum = extract_lastPage(BASE_URL)
    print("extract_lastPage :", lastPageNum)

    lastPageNum = 1  # 1page만
    print("extract_lastPage :", lastPageNum)

    return extract_jobs(BASE_URL, lastPageNum)
