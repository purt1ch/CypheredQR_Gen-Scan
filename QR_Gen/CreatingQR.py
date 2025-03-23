import qrcode
def creatingQR(name =' HP ProBook 430', processor = 'Core i3-1115G4', display = '13.3 FHD', ram = 'AG 8GB DDR4', hdd ='256GB', power_supply = '45Wh LL'):
    code = f'<center> <table border="1" width="350" height="240"> <font size="+4">{name}</font></td><tr> <td align="centre"><h2>G8</td> <td><h2>{processor}</td> <td><h2>(1920x1080)</td> </tr> <tr> <td><h2>{display}</td> <td><h2>{ram}</td> <td><h2>{hdd}</td> </tr> <tr> <td><h2>SSD</td> <td><h2>{power_supply}</td> <td><h2>FPR</td></h2> </tr></table> </center>'
    print(code)

    # example data
    data = "data:text/html, " + code
    print(data)
    # output file name
    filename = "qr.png"
    # generate qr code
    img = qrcode.make(data)
    # save img to a file
    img.save(filename)

if __name__ =='__main__':
    creatingQR()