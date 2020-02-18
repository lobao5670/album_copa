n = int(input())

#Verificar se o input da quantidade de figurinhas no álbum está de acordo
while n<0 or n>100:
    n = int(input())

m = int(input())

#Verificar se o input da quantidade de figurinhas compradas está de acordo
while m<0 or m>300:
    m = int(input())

figurinhas_compradas = []

#Iteração para ler o número das figurinhas
for _ in range(m):
    comprada = int(input())
    # Verificar se o input do número da figurinha comprada está de acordo
    while comprada<0 or comprada>n:
        comprada = int(input())
    #Se a figurinha já foi comprada, não adicionar à lista
    if figurinhas_compradas.count(comprada) == 0:
        figurinhas_compradas.append(comprada)

#Imprime a quantidade de figurinhas que faltam fazendo o número de figurinhas menos o número de obtidas
print(n-len(figurinhas_compradas))
