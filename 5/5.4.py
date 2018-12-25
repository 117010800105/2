def multi(*a): #发表示a可变
    if len(a) == 0:
        return 0
    t = 1
    for i in a:
        t = t * i
    return t

print( multi(1,2,3,4,5,6,7,8,9,10))

 10-1
import requests
from bs4 import BeautifulSoup
allUniv=[]
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    date=soup.find_all('tr')
    for tr in date:
        ltd=tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)

        allUniv.append(singleUniv)

def printUnivList(province):
    print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),"排名","学校名称","省市","总分","培养规模"))
    for u in allUniv:
        if province in u[2]:
            print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),u[0],u[1],u[2],u[3],u[4]))

def main(p):
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html=getHTMLText(url)
    soup=BeautifulSoup(html,'html.parser')
    fillUnivList(soup)
    printUnivList(p)

main('江西')

#把数量改为5个
def printUnivList(s,rank):
    c=0
    print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),"排名","学校名称","省市","总分","培养规模"))
    for u in allUniv:
        if s in u[1]:#u1指的是从第1组选取  学校名称
            print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(chr(12288),u[0],u[1],u[2],u[3],u[4]))
            c += 1
            if c == rank:
                break
def main(p,rank):
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html=getHTMLText(url)
    soup=BeautifulSoup(html,'html.parser')
    fillUnivList(soup)
    printUnivList(p,rank)

main('江西',5)
