import zlib
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt','rb') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressor: {}'.format(binascii.hexlify(compressed)))
        else:
            print('buffering')
remaining = compressor.flush()
print('Flushed: {}'.format(binascii.hexlify(remaining)))

