texto = ("""The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.""")
lista = []
texto = texto.lower()
texto = texto.replace('.', ' ',).replace(',', ' ').replace(':', ' ')
texto = texto.split()
for i in texto:
    if i[0] in 'python' or i[-1] in 'python':
        lista.append(i)
print(lista)


