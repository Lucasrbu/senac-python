# and, or, not(not é igual a ! no c#, negando um if/elif), 

soma = 6 + 5
multiplicacao = 10 ** 4299

if soma > 10 and multiplicacao > 10:
    print("a soma e multiplicacao sao maiores que 10")
else:
    print("a soma ou multiplicação não são maior que 10")

if soma > 11 or multiplicacao > 11:
    print("a soma ou multiplicacao sao maiores que 11")
else:
    print("nem a soma nem a multiplicacao sao maiores que 11")

if not soma > 10:
    print("A soma nao é maior que 10")

print(multiplicacao)