import struct

b = bytes.fromhex('10 11 12 34 3f')
print(b)

p = struct.pack('3B',5,7,0)
print(p)

q = struct.unpack('3B',b'\x05\x07\x25')
print(q)
print(q[0],q[1],q[2])
arr = [0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

data1 =struct.pack('4B',arr[0],arr[1],arr[2],arr[3])
data2 =struct.pack('4B',arr[4],arr[5],arr[6],arr[7])
print(data1+data2)

# print(struct.pack('i',))


speed = 1
data1 = (speed & 0xff00)>>8
data2 = (speed & 0xff)
data = bytes([data1, data2])
print(data)
# speed_b = struct.pack('H',speed)
# print(speed_b)