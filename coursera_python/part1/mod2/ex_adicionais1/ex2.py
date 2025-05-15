segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_int = int(segundos_str)
dias = segundos_int // 86400
resto_dos_segundos = segundos_int % 86400
horas = resto_dos_segundos // 3600
resto_dos_segundos = resto_dos_segundos % 3600
minutos = resto_dos_segundos // 60
segundos = resto_dos_segundos % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")