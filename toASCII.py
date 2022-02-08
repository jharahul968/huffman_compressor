
def toBinary(a):
      
  import math
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return ''.join(map(str, m))




if __name__ == '__main__':
  print(toBinary("Huffman coding is a data compression algorithm."))