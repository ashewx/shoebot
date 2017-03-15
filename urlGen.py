# Basic URL = http://www.adidas.com/us/BW0548.html?forceSelSize=BW0548_660
def urlGen(model, size):
    BaseSize = 580  # Base Size is for shoe 6.5
    ShoeSize = size - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
    return URL
Model = input('Model # ')
Size = input('Shoe Size: ')
URL = urlGen(Model, float(Size))

print(str(URL))
