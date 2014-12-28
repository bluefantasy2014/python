import pdb
from bs4 import BeautifulSoup
import requests
import urllib


index = "http://delhidistrictcourts.nic.in/case_status09.htm"
r = requests.get(index)
#pdb.set_trace()
soup = BeautifulSoup(r.content)

allLinks = soup.findAll('a')

JUDGE_SEARCH = "Judge Search"
for index,link in enumerate(allLinks):
  if index > 0 :
    continue
  print ("processing the {} link..........".format(index))
  print ("the link of the page is :{}".format(link.get('href')))
  print ("start to parse this page.....................................")
  r1 = requests.get(link.get('href'))
  pageSoup = BeautifulSoup(r1.content)

  allAs = pageSoup.findAll('a')
  for a in allAs:
#   print (a.contents)
    if len(a.contents) > 0 and a.contents[0] == JUDGE_SEARCH:
      judgeQueryURL = a.get('href')
      print (judgeQueryURL)
      judgeQueryPage = requests.get(judgeQueryURL)
      judgeQueryPageSoup = BeautifulSoup(judgeQueryPage.content)
      
      form = judgeQueryPageSoup.find(id='myForm')
      detailURL = form.get('action')
      print (detailURL)
      detailURL = judgeQueryURL[:judgeQueryURL.rfind('/')+1] + detailURL
      print (detailURL)
#judge=a&cyear=2014&Submit=Submit
      requestPara = {'judge':'a','cyear':'2014','Submit':'Submit'}
      data = urllib.parse.urlencode(requestPara)
      print (data)
      data=data.encode(encoding='UTF8')
      req = urllib.request.Request(detailURL,data)
      response = urllib.request.urlopen(req)
      detailPage = response.read()
    #  print (detailPage)
      datailPageSoup = BeautifulSoup(detailPage)
      print (datailPageSoup)
  








