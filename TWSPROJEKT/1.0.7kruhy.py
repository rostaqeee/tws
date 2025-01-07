def plocha(odpolo,dopolo):
        if  odpolo<dopolo:
            print("Polomer(cm)   Obsah(cm2)   Spotreba(ml)")
            for i in range(odpolo,dopolo+1):
                print(i,end="             ")
                plocha=(i*i)*12.56
                print(f"{plocha:.2f}",end="             ")
                print(plocha*0.5)
            return ""
        else:
            return"Zadali ste nespravny rozsah"
print("Program na vypocet farby")
try:
    odpolo=int(input("Zadajte od : "))
    dopolo=int(input("Zadajte do : "))
    print(plocha(odpolo,dopolo))
except ValueError:
    print("Nespravne hodnoty na vstupe")
    