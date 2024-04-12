def kapital_verzinsung(jahre, kapital):
    if jahre == 0:
        return kapital
    ergebnis = kapital*1.05

    return kapital_verzinsung(jahre-1, ergebnis)

print(kapital_verzinsung(5, 1000))