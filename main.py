a=1
while a !=0:
    a=float(input("ingrese el numero que quiera elevar: "))
    b=int(input("ingrese el valor del exponente: "))
    def a_power_b(a,b):
        result=1
        for number in range(0,b):
            result=result*a
            number=number+1
        print(result)
    a_power_b(a,b)