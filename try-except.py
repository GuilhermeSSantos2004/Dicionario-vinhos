'''lista = ['a','b','c']

while True:
    try:
        i = int(input("Diga um número: "))
        print(lista[i])
        #print("1"+1)

    except ValueError:
        print("Deve ser inteiro")
        #raise (serve para fazer biblioteca) serve para parar o código
    except IndexError:
        print(f"Alem de inteiro, deve ser entre 0 e {len(lista)-1}")
    except Exception as e:
        print(e)
    else:
        print("Operação realizada com sucesso!")
        break
    finally:
        print("N sirvo pra mta coisa")

'''

'''while True:

    try:
        a = int(input("diga o primeiro número : "))
        b = int(input("diga o segundo número : "))
        print(b/a)
    except ZeroDivisionError:
        print("O primeiro número não pode ser zero")
    except ValueError:
        print("Precisa ser um número")
        #print("Não posso dividir por zero")
    else:
        print("Operação realizada com sucesso!")
        break
'''

'''dic = {'são paulo': "campeão",
       'palmeiras': 'sem mundial',
       'corinthians' : 'putz kk',
       'santos' : 'idoso rebaixado'
       }
while True:

    try:
        time = input("Diga para que time torce: ")
        print(f"Você é {dic[time]}")
    except KeyError:
        print("Não sei o time")
    else:
        print("Operação realizada com sucesso")
        break
        
'''
'''
dic = {
    1:'um',
    2:'dois',
    3:'três'
}



while True:
    try:
        num = int(input("Diga o número que você quer ver por extenso: "))
        print(f"{dic[num]}")
    except ValueError:
        print(f"Deve ser um inteiro")
    except KeyError:
        print(f" Deve ser um entre {list{dic.keys()}}")
'''

dic = {
    1:['um','uno','one'],
    2:['dois','dos','two'],
    3:['três','tres','three']
    }

while True:
    escolha = int(input(f"Em qual ligua você quer traduzir entre {list(dic.keys())}"))
    print()


