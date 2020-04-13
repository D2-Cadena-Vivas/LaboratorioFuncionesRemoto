n = int(input("introduzca el numero a evaluar:"))
def perfect_number(n):
	suma = 0
	for i in range(1,n):
		if (n % i == 0):
			suma += i
	if n == suma:
		return True
	else:
		return False

if perfect_number(n):
	print("El número",n,"es perfecto")
else:
    print("El número",n,"no es perfecto")