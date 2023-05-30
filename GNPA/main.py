def gnpa(var):
    
    k = len(list(str(var)))

    print('Nous avons bel et bien k : ', k)

    number_gnpa = []

    b = var

    while(len(number_gnpa) < 12):

        b = b**2

        print('L\'elevation au carre donne ceci : ', b)

        c = list(str(b))


        while(len(c) < 4):
            c.insert(0, 0)


        print('On obtient par suite ce resultat : ', c)

        d = c[1:-1]

        print('Et la coupure nous donne ceci : ', d)

        v = ""

        for i in d:
            v += str(i)


        b = int(v)

        number_gnpa.append(d)

        print('B est cence donner ceci : ', b)

    return number_gnpa


numbers = gnpa(79)

print(numbers)


