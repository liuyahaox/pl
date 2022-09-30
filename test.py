from fileinput import filename
from multiprocessing.resource_sharer import stop
import requests
import urllib.request
from lxml import etree

url = 'https://aclanthology.org/2022.acl-long.'
headers1={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
for i in range(1,600):
    thisurl = url+str(i)
    page = requests.get(thisurl,headers=headers1)
    downloadurl = thisurl+'.pdf'
    tree = etree.HTML(page.text)
    filename = str(tree.xpath('//*[@id="citeACL"]/a/text()'))[1:30]+'.pdf'
    filename=filename.replace(':','')
    print(filename)
    urllib.request.urlretrieve(downloadurl,filename,)
print('hello')