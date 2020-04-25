import requests #네트워크 연결
import bs4 #특정부분 추출 : Beautiful soup

def crawl(codeValue):
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
    file_write(data)

def file_write(comList):
    file = open(comList[2] + '.txt', 'w')
    for x in comList:
        file.write(x + '\n')
    file.close()


codeList = ['039610', '002460', '013520']
for x in codeList:
    crawl(x)

#readFile = open('codelist.txt','r')
#while readFile.readable():
#    codeValue = readFile.readline()
#    crawl(codeValue)
#readFile.close()