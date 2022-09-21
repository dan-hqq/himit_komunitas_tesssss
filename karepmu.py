bilangan = int(input("Masukkan bilangan: "))

i = 2

if bilangan < 2:
    print("Bukan prima")
elif bilangan == 2:
    print("Prima")
else:
    prima = True
    while i * i <= bilangan:
        if bilangan % i == 0:
            prima = False
            break
        i = i + 1
    if prima == True:
        print("Prima")
    else:
        print("Bukan Prima")