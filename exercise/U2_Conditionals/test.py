'''
# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import thread
import time
import json


class Spider_Model:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def GetPage(self, page):
        myUrl = "https: // www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref = zg_bs_toys-and-games_home_all?pf_rd_p = 089b8285-7691-4849-a7f5-b2fca56bf24a & pf_rd_s = center-1 & pf_rd_t = 2101 & pf_rd_i = home & pf_rd_m = ATVPDKIKX0DER & pf_rd_r = 444ERCAB5AYQ4QYVJH4R & pf_rd_r = 444ERCAB5AYQ4QYVJH4R & pf_rd_p = 089b8285-7691-4849-a7f5-b2fca56bf24a" + page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(myUrl, headers=headers)
        myResponse = urllib2.urlopen(req)
        for divs in myResponse.read('//div[@class="zg_itemlmmersion"]'):
            myPage = myResponse.read('//div[@class="zg_itemlmmersion"]')
            doc = etr.Html(myResponse)
        divs = doc.read("//div[@id='zg_centerListWrapper']")

        print myPage
        unicodePage = myPage.decode("utf-8")
        myItems = re.findall(
            '<div.*?class="p13n-sc-price">\n\n+<span>(.*?)</span>\n\n+</div>', unicodePage, re.S)
        items = []
        print myItems
        print str(myItems).decode('string_escape')
        print json.dumps(myItems, encoding="UTF-8", ensure_ascii=False)
        for item in myItems:
            items.append([item[0].replace("\n", ""),
                            item[1].replace("\n", "")])
        print myItems
        print str(myItems).decode('string_escape')
        print str(myItems).encode("UTF-8")
        print myItems[0]
        return myItems

    def LoadPage(self):
        while self.enable:
            print len(self.pages)
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print '无法链接！'
            else:
                time.sleep(5)

    def ShowPage(self, nowPage, page):
        print u'第%d页' % page, json.dumps(nowPage, encoding="UTF-8", ensure_ascii=False)

    def ShowPage(self, nowPage, page):
        i = 0
        print len(nowPage)
        for i in range(0, len(nowPage)):
            if i < len(nowPage):
                oneStory = "\n\n" + \
                    nowPage[i].replace("\n\n", "").replace(
                        "<br/>", "\n")+"\n\n"
                print u'第%d页,第%d个文件' % (page, i), oneStory
                i += 1
            else:
                break

        myInput = str(raw_input(u'回车键看下一页,按quit退出：\n'))
        if myInput == "quit":
            self.enable = False

    def Start(self):
        self.enable = True
        page = self.page
        print u'正在加载中请稍候......'
        thread.start_new_thread(self.LoadPage, ())
        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1
i = 1
b = 0
if i == 1:
    b = b + 1
elif i == 1:
    b = b + 1

print(b)
'''
i = 0

def b(i):
    if i == 10:
        return break

while i < 100:
    i = i + 1
    print(i)