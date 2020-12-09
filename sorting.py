import requests,bs4,os
students=[]
for i in range(61392,61757):
    page=requests.get('http://app2.helwan.edu.eg/HelwanNat/EngHelwan/TermAview.asp?StdCode=%i'%i)
    page.encoding='windows-1256'
    html = bs4.BeautifulSoup(page.text, features="html5lib")
    name = html.select('td[style="padding-left:0; padding-right:10px; padding-top:0; padding-bottom:0"] p[align="right"] b font[size="4"] span')
    n=''
    name=(name[0].next_sibling.string).replace('الب \n		:  ','').replace('\n\t\t ','')
    deg= html.select('td[width="40"] b')
    deg = [a.get_text() for a in deg]
    del(deg[0])
    del(deg[4:])
    deg = [a for a in deg if a!='']
    if len(deg)==0:
        deg=0
    else:
        deg=sum(list(map(int,deg)))
    students.append((name,deg))
students.sort(key= lambda x : x[1],reverse=True)
with open('Comm.txt','w',encoding="utf-8") as m:
    for i in range(len(students)):
        m.write('%s||%s||%s\n'%(students[i][0],students[i][1],i+1))
