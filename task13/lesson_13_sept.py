# Example

import ipaddress
network = ipaddress.ip_network("102.162.200.51/255.255.255.0", strict=False)
for ip in network:
    print(ip)
    print(int(ip))
    print()

# 102.162.200.255
print(bin(102), bin(162), bin(200), bin(255))
# 01100110 10100010 11001000 11111111
print(int("01100110101000101100100011111111", 2))
print(102+162+200+255)

# 

