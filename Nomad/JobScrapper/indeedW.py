import requests  # Request 요청
from bs4 import BeautifulSoup  # html 나열.. 해야되나?


def extract_job(html):
    strTitle = html.find("h2", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        strCompany = str(company_anchor.string)
    else:
        strCompany = str(company.string)
    strCompany = strCompany.strip()

    # strLocation = html.find("span", {"class": "location"}).string
    strLocation = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    strJobID = html["data-jk"]
    return {'title': strTitle,
            'company': strCompany,
            'location': strLocation,
            'link': f"https://www.indeed.com/viewjob?jk={strJobID}"
            }


def extract_jobs(BASE_URL, LIMIT, last_page):
    jobs = []

    for page in range(last_page):
        GET_PAGE_URL = f"{BASE_URL}&start={page*LIMIT}"
        result = requests.get(GET_PAGE_URL)

        print("Get URL :", GET_PAGE_URL)
        result = requests.get(GET_PAGE_URL)
        print("StatusCode :", result.status_code)

        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def extract_lastPage(BASE_URL):

    print("extract_lastPage() Get URL :", BASE_URL)
    result = requests.get(BASE_URL)
    print("status code :", result.status_code)

    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    pageCount = pages[-1]
    return pageCount


def get_jobs(searchWhat):
    LIMIT = 50
    BASE_URL = f'https://www.indeed.com/jobs?q={searchWhat}&limit={LIMIT}'

    lastPageNum = extract_lastPage(BASE_URL)
    print("extract_lastPage :", lastPageNum)

    lastPageNum = 1  # 1page만
    print("extract_lastPage :", lastPageNum)
    return extract_jobs(BASE_URL, LIMIT, lastPageNum)
