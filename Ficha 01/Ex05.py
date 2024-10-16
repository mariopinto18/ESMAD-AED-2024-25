"""
Conversor  de  segundos em horas, muinutos e segundos
"""
tempoTotal= int(input("Indique o tempo em segundos:"))

horas= int(tempoTotal/3600)   # converte em horas
tempoTotal-= horas*3600       # subtrai as horas ao tempo inicial

minutos = int(tempoTotal/60)  # converte em minutos
segundos= tempoTotal- minutos*60       # subtrai os minutos ao tempo disponível, sobrando os segundos


print("\n{:n} horas, {:n} minutos, {:n} segundos" .format(horas, minutos, segundos) )
