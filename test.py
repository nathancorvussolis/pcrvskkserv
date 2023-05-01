import codecs
import sys
import socket
import time

IPADDR = '127.0.0.1'
PORT = 1178
ENCODING = 'euc_jis_2004'
#ENCODING = 'utf_8'

def server_test(f):
  print('addr: ' + IPADDR)
  print('port: %d' % PORT)

  sock = socket.socket(socket.AF_INET)
  sock.connect((IPADDR, PORT))

  count = 0
  comment = ';;'
  for line in codecs.open(f, 'r', ENCODING):
    if (line.startswith(comment)):
        continue
    si = line.find(' /')
    if (si < 0):
        continue
    key = line[:si + 1]
    candidates = line[si + 1:]

    sstr = '1' + key
    sdata = sstr.encode(ENCODING)
    sock.send(sdata)
    rdata = sock.recv(4096)
    rstr = rdata.decode(ENCODING)

    if rstr != '1' + candidates:
      print(key + candidates)
      print('S: ' + sstr)
      print('R: ' + rstr)
      sys.exit(1)

    count += 1

  print('entry: %d' % count)

if __name__ == "__main__":
    print('encoding: ' + ENCODING)
    if (len(sys.argv) != 2):
        print('usage: python test.py <skk dic file>')
        sys.exit(1)
    server_test(sys.argv[1])
