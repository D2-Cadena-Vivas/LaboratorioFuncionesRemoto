a=1
cont=0
cont_p=0
cont_i=0
while a !=0:
    a=float(input("ingrese el numero que quiera elevar, para finalizar digite 0: "))
    b=int(input("ingrese el valor del exponente: "))
    if a==0:
        break
    else:
        cont=cont+1
        def a_power_b(a,b):
            result=1
            for number in range(b):
                result=result*a
                number+=1
            print(result)
            return result
        c=a_power_b(a,b)
        if c%2==0:
            cont_p=cont_p+1
        else:
            cont_i+=1
print("se calcularon",cont,"potencias")
print(cont_p,"potencias fueron pares")
print(cont_i, "potencias fueron impares")

