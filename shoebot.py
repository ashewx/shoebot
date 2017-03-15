import requests
import bs4
import random
import lxml
import webbrowser

# Basic URL = http://www.adidas.com/us/BW0548.html?forceSelSize=BW0548_660
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def urlGen(model, size):
    BaseSize = 580  # Base Size is for shoe 6.5
    ShoeSize = float(size) - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
    return URL

def CheckSizes(url, model):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    RawHTML = requests.get(url, headers=headers)
    page = bs4.BeautifulSoup(RawHTML.text,"lxml")
    ListOfRawSizes = page.select('.size-dropdown-block')
    Sizes = str(ListOfSizesRaw[0].getText()).replace('\t', '')
    Sizes = Sizes.replace('\n\n', ' ')
    Sizes = Sizes.split()
    Sizes.remove('Select')
    Sizes.remove('size')
    for size in Sizes:
        print(str(model) + ' Sizes: ' + str(size) + ' Available')
