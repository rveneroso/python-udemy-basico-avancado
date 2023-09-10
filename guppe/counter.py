'''
Collections Counter opera sobre qualquer iterável
'''

from collections import Counter

# Utilizando lista mas poderia ser qualquer iterável
lista = [1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9 ,12, 25, 27, 32, 32, 99]

# O Counter irá armazenar cada valor distinto presente no iterável e associar a ele o número de vezes em que aquele valor ocorre.
res = Counter(lista)
print(res)
print(type(res)) # Imprime <class 'collections.Counter'>

texto = '''Jerry (Jerrald) King Goldsmith was born on February 10th 1929 in Pasadena California, growing up in Los Angeles. Jerry Goldsmith was the son of Tessa 
and Morris Goldsmith. Tessa was an Artist and Morris a Structural Engineer. Jerry Goldsmith began studying piano at the age of 6 and by the age of 14 was studying 
composition, theory and counterpoint privately with Jacob Gimpel and Mario Castelnuovo-Tedesco. After graduating from Dorsey High School Goldsmith went to Los Angeles
 City College where he worked on a lot of Opera, Dance and coaching of singers. He became assistant conductor for the opera and chorus as well as accompanist and found 
 time to write music for the drama department for various plays.  During this period he became acquainted with legendary composer Miklos Rosza and attended one semester 
 in film music composition at the University of Southern California. This involved re-scoring Flesh And Fantasy (1943) and new music for a documentary on the summer arts school. 
 It was Rosza's own score to Spellbound and the film's star Ingrid Bergman that had captivated Goldsmith back in 1945. Goldsmith recalled wanting to marry Ingrid 
 Bergman and have a career in writing music for film. Saying that one out of two wasn't bad. Jerry Goldsmith had originally intended to become a concert pianist, 
 but he soon realised that the infrequency of concert hall commissions would never satisfy his hunger to write music.'''

palavras = texto.split()
# Identifica as 5 palavras que mais ocorrem no texto
print(Counter(palavras).most_common(10))