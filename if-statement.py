# If statement
i = 10

if(i == 10):
     print('Ini angka 10') #jika TRUE


# If... Else
if(i == 10):
     print('Ini angka 10') #jika TRUE
else:
    print('Ini bukan angka 10')

# If..Elif..Else
if(i == 10):
     print('Ini angka 10') #jika TRUE
elif(i<=10):
    print('Angka lebih kecil dari 10')
else:
    print('Angka lebih besar dari 10')


# Nested IF
if(i == 10):
     print('Ini angka 10') #jika TRUE
     if(i<10):
         print('Nilainya mlebih kecil dari 10')
     else:
         print('Mantap')