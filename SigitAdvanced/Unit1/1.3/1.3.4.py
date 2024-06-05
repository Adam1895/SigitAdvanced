password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

print(''.join(chr((ord(c) - ord('a') + 2) % 26 + ord('a')) if 'a' <= c <= 'z' else c for c in password))