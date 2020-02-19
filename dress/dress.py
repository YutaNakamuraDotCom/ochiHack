import urllib3
from bs4 import BeautifulSoup
import certifi



# アクセスするURL
url = "https://tenki.jp/indexes/dress/6/30/6200/"

# httpsの証明書検証を実行している
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
r = http.request('GET', url)

soup = BeautifulSoup(r.data, 'html.parser')
# print(soup)
# print(type(soup))
today=soup.select('.indexes-telop-1')
print(today[0])

# print(hukusou)