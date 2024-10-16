""" 
Simulador de esforço cardíaco
Nas mulheres: FCM = 226 - idade.
Nos homens: FCM=  220 - idade
 """

sexo = input("\n\n\n\tIndique o Sexo(M/F): ")
idade = int(input("\n\n\tIndique a idade: "))

match sexo.upper():
    case "F":
        indiceFCM = 226- idade
    case "M":
        indiceFCM = 220- idade
    case _:
        print("Dados incorretos!")
print(f'\n\tFCM= {indiceFCM} bpm' )



