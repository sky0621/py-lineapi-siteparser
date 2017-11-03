from bs4 import BeautifulSoup
import requests
import requests_cache

requests_cache.install_cache('lineapi', backend='sqlite', expire_after=60)

BASE_URL = 'https://developers.line.me/ja/docs/messaging-api/reference/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_lineapi_soup():
    res = requests.get(BASE_URL+'#anchor-eab6741c0f596830bffc91eb993f5b3fcfc32b9a', headers=HEADERS)
    return BeautifulSoup(res.content, "lxml")

soup = get_lineapi_soup()
print(soup.find('a', {'class': 'md82ReferenceLangLink'}))
print("==============================================================================")

for i in soup.select('h2'):
    print(i.text)

print("==============================================================================")
statusCode = soup.select("h3#anchor-006a70a2021e9f35c762d309e9bd5f4e8aa94355 + p + table tbody tr td")
for j in statusCode:
    print(j)
