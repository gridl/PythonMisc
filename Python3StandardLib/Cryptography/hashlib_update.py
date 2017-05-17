import hashlib

lorem = '''Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.'''


h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()

def chunkize(size, text):
    "Return parts of the the text in size-based increments"
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return

h = hashlib.md5()

# Update() method of the hash calculators can be called repeatedly.
# Each time the digest is updated based on additional text fed in.
# Updating incrementally is more efficient than reading an entire file into memory

for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)
line_by_line = h.hexdigest()

print('All at once:', all_at_once)
print('Line by line:', line_by_line)
print('Same :', (all_at_once == line_by_line))