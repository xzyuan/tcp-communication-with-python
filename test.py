import struct

data = bytes('good','UTF-8')
q = len(data)
o = hex(len(data))
d = bytes(data)
print((4 == 0x4))
# bytes(hex(len(data)))
# p = struct.unpack('<hh', bytes(hex(len(data)), encoding="utf-8"))
print(bytes(hex(len(data)), encoding="utf-8"))
while True:
    pass

# print(bytes.decode(bytes(hex(len(data)))))
