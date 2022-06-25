def salam():
    print('Selamat Pagi Semuanya')

salam()

# Menghitung luas persegi
def persegi(sisi1,sisi2):
    luas = sisi1*sisi2
    print('Luas persegi = %f' % luas)

persegi(5,5)

# Fungsi return value
def persegi(sisi1,sisi2):
    luas = sisi1*sisi2
    return luas

print('Luas persegi = %f ' % persegi(5,5))