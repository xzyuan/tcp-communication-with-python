import struct

b = bytes.fromhex('10 11 12 34 3f')
print(b)

p = struct.pack('3B',5,7,0)
print(p)

q = struct.unpack('3B',b'\x05\x07\x00')
print(q[0],q[1],q[2])

arr = [0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
data =struct.pack('8B',arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
print(data)