# 為「PCHome線上購物」建立一個的商品搜尋程式
import requests
import codecs
import json
import prettytable

key = input("關鍵字:")
p = 1
while True:
  req = requests.get(
      'https://ecshweb.pchome.com.tw/search/v3.3/all/results',
      headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
            "referer":"https://shopping.pchome.com.tw/",
            "cookie": "PHPSESSID=toonpqjnirk9gbh84elbnk39jg",
      },
      params={
          "q":key,
          "page":p,
          "sort":"sale/dc"
      },
      data={}
  )

  ret = json.loads(req.text)
  # for dd in ret["prods"]:
  #   print(dd["name"],dd["price"])

  p1 = prettytable.PrettyTable(["名稱","價格"], encoding="utf-8")
  p1.align["名稱"] = "l"
  for dd in ret["prods"]:
    p1.add_row([dd["name"],dd["price"]])

  print(p1)

  p = input("前往頁碼:")
  if p == "":
    print("輸入的不是數字！")
    break