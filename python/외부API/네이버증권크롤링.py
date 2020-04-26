import requests #네트워크 연결
import bs4 #특정부분 추출 : Beautiful soup
import datetime

def crawl(codeValue):
    print('crawl start : ' + codeValue)
    url = 'https://finance.naver.com/item/main.nhn?code=' + codeValue

    result = requests.get(url) #네트워크로 url 연결
    doc = bs4.BeautifulSoup(result.content, 'html.parser')

    p_no_today = doc.find('p', {'class':'no_today'})
    today = p_no_today.find('span', {'class':'blind'})

    td_first = doc.find('td', {'class':'first'})
    start = td_first.find('span',{'class':'blind'})

    company = doc.find('a', {'onclick':"clickcr(this, 'sop.title', '', '', event);window.location.reload();"})

    div_desc = doc.find('div', {'class':'description'})
    code = div_desc.find('span',{'class':'code'})

    data = [today.text, start.text, company.text, code.text]
    print('file write : ' + codeValue)
    file_write(data)
    print('crawl end : ' + codeValue)

def file_write(comList):
    file = open('외부API/crawling/'+comList[2] + '.txt', 'w')
    for x in comList:
        file.write(x + '\n')
    file.close()


start = datetime.datetime.now()
print('crawling 시작' + str(start))

codelist = []


with open('외부API/file/codelist.txt','r') as readFile:
    while readFile.readable():
        line = readFile.readline()
        if line =='':
            break
        codelist.append(line)


for x in codelist:
    crawl(x)

print('crawling 종료' + str(datetime.datetime.now() - start))