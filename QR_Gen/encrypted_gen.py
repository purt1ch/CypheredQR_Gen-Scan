import qrcode
from crypto import encrypt
def main_gen(name =' HP ProBook 430', processor = 'Core i3-1115G4', display = '13.3 FHD', ram = 'AG 8GB DDR4', hdd ='256GB', power_supply = '45Wh LL'):
    # Organizing data for future decryption in Android app
    data = name + '; ' + processor + '; ' + display + '; ' + ram + '; ' + hdd + '; ' + power_supply
    encrypted_data = encrypt(data)
    # output file name
    filename = "qr.png"
    # generate qr code
    img = qrcode.make(encrypted_data)
    # save img to a file
    img.save(filename)
    return data, encrypted_data
if __name__ =='__main__':
    main_gen()
    print('Data: ' + main_gen()[0])
    print('Encrypted data: ' + main_gen()[1])