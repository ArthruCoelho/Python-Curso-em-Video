alt = float(input("Diga a altura da parede "))
lgr = float(input("Diga a largura da parede "))
prm = alt * lgr
tinta = prm / 2
print('A parede tem um perimetro de {}m².\n E precisara de {}l de tinta para ela ser pintada.'.format(prm, tinta))
