import math
garums=float(input("Ievadi kvadrāta malas garumu lielāku par 5cm: "))
laukums1=garums*garums
laukums2=(garums+5)*(garums+5)
procenti=round(laukums2-laukums1/laukums2*100)
print(f"Jaunais kvadrāts ir par {procenti} procentiem lielāks.")
