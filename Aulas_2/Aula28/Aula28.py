animes=["Toradora","Erased","Death Note","Shingeki no Kioijin"]

itAnimes=iter(animes)

#print(next(itAnimes))

while itAnimes:
    try:
        print(next(itAnimes))
    except StopIteration:
        print("Fim lista!")
        break