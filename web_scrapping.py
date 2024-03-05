from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.citizen.digital/news"
# url ="https://beautiful-soup-4.readthedocs.io/en/latest/#navigating-the-tree"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")



news = soup.select('.topstory-excerpt')


for i in news:
    
    print(i) 
    print("\n")
    print("\n")
    print("\n")
    # print(i.next_element)

# print(len(news))