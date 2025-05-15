dividainicial = float(input('Digite o valor da divida inicial: '))
juros = int(input('Digite o valor do juros: '))
valorpago = 0
valormensal = int(input('Quanto sera pago todo mes? '))
meses = 0
jurostotal = 0
divida = 0
while valorpago < dividainicial:
    divida = dividainicial * (1 + juros/100)
    jurostotal = jurostotal + (divida - dividainicial)
    dividainicial = divida - valormensal
    valorpago = valorpago + valormensal
    meses += 1

print(f"Meses: {meses}, Total pago: {valorpago}, Juros total: {jurostotal}")