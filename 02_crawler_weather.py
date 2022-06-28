# 中央氣象局 建立一個可以查詢縣市溫度極值資料的程式
import requests
from bs4 import BeautifulSoup
import prettytable

req = requests.get('https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html',
      headers = {
          "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
          "referer":"https://www.cwb.gov.tw/V8/C/W/County_TempTop.html",
          "cookie": "_gid=GA1.3.446854056.1652631427; _ga_K6HENP0XVS=GS1.1.1652662884.2.1.1652664728.0; TS010c55bd=0107dddfefc46cc40d0547fbca1bf65c3fd432d05451df8def23de28add36883882eef53d27f0589bf01278c8a8ba08184a166f458; _ga=GA1.3.1885860613.1652631427; _gat_gtag_UA_126485471_1=1",
      },
      params = {
          "ID":"payload"
      },
    )
sp = BeautifulSoup(req.text,'html.parser')
# print(sp)

city = sp.find_all('th', {"scope":"row"})
temp = sp.find_all('span',{"class":"tem-C"})

p1 = prettytable.PrettyTable(["地區","氣溫"], encoding="utf-8")
p1.align["地區"] = "l"
for index in range(len(city)):
  p1.add_row([city[index].text,temp[index].text])

print(p1)