texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''
texto = texto.lower()
texto = texto.replace('.', ' ',).replace(',', ' ').replace(':', ' ')
def listaPython(palavra):
  for letra in palavra:
    if letra in 'python':
      return True
  return False
resp = []
for i in texto.split():
  if listaPython(i) and len(i) > 4:
    resp.append(i)
print (resp)
print (len(resp))
