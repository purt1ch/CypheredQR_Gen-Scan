import qrcode
import base64
from crypto import encrypt
def main_gen(name =' HP ProBook 430', processor = 'Core i3-1115G4', display = '13.3 FHD', ram = 'AG 8GB DDR4', hdd ='256GB', power_supply = '45Wh LL'):
    data = name + '; ' + processor + '; ' + display + '; ' + ram + '; ' + hdd + '; ' + power_supply
    print('Входные данные: '+data)
    data = encrypt(data)
    print('Зашифрованные данные: '+data)
    # output file name
    filename = "qr.png"
    # generate qr code
    img = qrcode.make(data)
    # save img to a file
    img.save(filename)

if __name__ =='__main__':
    main_gen()