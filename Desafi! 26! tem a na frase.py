frase = str(input('Digite uma fase: ')).strip().lower()
frasi = frase.count("a")
print("""Aparece {} "A" na frase\nO primeiro "A" aparece na posição {}\nO ultimo "A" aparece na posição {}"""
      .format(frasi, frase.find('a'), frase.rfind('a')))
