# Сеть задана IP-адресом одного из входящих в неё узлов 191.128.66.83 и сетевой маской 255.192.0.0.

ip = [191, 128, 66, 83]
mask = [255, 192, 0, 0]

network = []
for i in range(4):
    network.append(ip[i] & mask[i])

print('mask', [bin(b) for b in mask])
# mask ['0b11111111', '0b11000000', '0b0', '0b0']
print('ip  ', [bin(b) for b in network])
# ip   ['0b10111111', '0b10000000', '0b0', '0b0']

print(191, int('10111111', 2), int('11111111', 2), int('11111111', 2) - 1)