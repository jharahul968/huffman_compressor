import math


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

print("''Hello world'' in binary is ") 
print(toBinary("Huffman coding is a data compression algorithm."))